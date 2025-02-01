from django.db import models
from ckeditor.fields import RichTextField
from django.utils.translation import gettext_lazy as _

class FAQ(models.Model):
    question = models.TextField(_("Question (English)"))
    answer = RichTextField(_("Answer (English)"))

    def __str__(self):
        return self.question
