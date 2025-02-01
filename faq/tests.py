import pytest
from django.test import Client
from .models import FAQ

@pytest.mark.django_db
def test_create_faq():
    faq = FAQ.objects.create(question="Test?", answer="This is a test.")
    assert faq.question == "Test?"

@pytest.mark.django_db
def test_api_response():
    client = Client()
    response = client.get('/api/faqs/?lang=hi')
    assert response.status_code == 200
