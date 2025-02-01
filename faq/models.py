from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _
from googletrans import Translator

translator = Translator()

class FAQ(models.Model):
    question = models.TextField(verbose_name=_("Question"))
    answer = RichTextField(verbose_name=_("Answer")) 
    language = models.CharField(
        max_length=10, choices=[('en', 'English'), ('hi', 'Hindi'), ('bn', 'Bengali')], default='en'
    )
    question_hi = models.TextField(blank=True, null=True)
    question_bn = models.TextField(blank=True, null=True)
    answer_hi = RichTextField(blank=True, null=True)
    answer_bn = RichTextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        """Auto-translate fields on save"""
        if not self.question_hi:
            self.question_hi = translator.translate(self.question, src='en', dest='hi').text
        if not self.question_bn:
            self.question_bn = translator.translate(self.question, src='en', dest='bn').text
        if not self.answer_hi:
            self.answer_hi = translator.translate(self.answer, src='en', dest='hi').text
        if not self.answer_bn:
            self.answer_bn = translator.translate(self.answer, src='en', dest='bn').text
        super().save(*args, **kwargs)

    def get_translated_text(self, lang='en'):
        """Retrieve translated question & answer based on language selection"""
        return {
            "question": getattr(self, f'question_{lang}', self.question),
            "answer": getattr(self, f'answer_{lang}', self.answer)
        }

    def __str__(self):
        return self.question[:50]
