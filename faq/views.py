from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from googletrans import Translator
from .models import FAQ
from .serializers import FAQSerializer

translator = Translator()

class FAQListView(APIView):
    def get(self, request):
        lang = request.GET.get('lang', 'en')
        cache_key = f"faq_{lang}"

        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data, status=status.HTTP_200_OK)

        faqs = FAQ.objects.all()
        data = []

        for faq in faqs:
            translated_question = faq.question
            translated_answer = faq.answer

            if lang != 'en':
                try:
                    translated_question = translator.translate(faq.question, src='en', dest=lang).text
                    translated_answer = translator.translate(faq.answer, src='en', dest=lang).text
                except Exception as e:
                    print(f"Translation failed: {e}")

            data.append({
                "id": faq.id,
                "question": translated_question,
                "answer": translated_answer
            })

        cache.set(cache_key, data, timeout=3600) 
        return Response(data, status=status.HTTP_200_OK)


class FAQCreateView(APIView):
    def post(self, request):
        serializer = FAQSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            cache.delete_pattern("faq_*")
            return Response({"message": "FAQ created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
