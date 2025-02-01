from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.cache import cache
from .models import FAQ
from .serializers import FAQSerializer

class FAQListView(APIView):
    def get(self, request):
        lang = request.GET.get('lang', 'en')
        cache_key = f"faq_{lang}"

        # Check if cached data exists
        cached_data = cache.get(cache_key)
        if cached_data:
            return Response(cached_data, status=status.HTTP_200_OK)

        faqs = FAQ.objects.all()
        serializer = FAQSerializer(faqs, many=True, context={'lang': lang})
        data = serializer.data

        # Cache the response for 1 hour
        cache.set(cache_key, data, timeout=3600)

        return Response(data, status=status.HTTP_200_OK)
