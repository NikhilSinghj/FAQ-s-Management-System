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

