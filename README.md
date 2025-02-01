# FAQ-Management-System

## Features

- FAQ storage
- WYSIWYG editor for rich text answers
- API with language support
- Caching for performance boost
- Auto-translation using Google Translate API
- Admin panel for easy management

## Environment Setup & Activate

```sh
python -m venv env

python env/bin/activate

```

## Installation

```sh
git clone https://github.com/NikhilSinghj/FAQ-s-Management-System.git
cd FAQ_MS
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## API & URL's

# Create FAQ -

    -- URL : http://localhost:8000/api/faqs/add/
    -- Request POST :
                 ```sh
                 {
                    "question": "This is a test question",
                    "answer": "This is a test answer"
                 }
                 ```

# Get FAQ -

    -- URL : default - http://localhost:8000/api/faqs/
             hindi -   http://localhost:8000/api/faqs/?lang=hi
             bengali - http://localhost:8000/api/faqs/?lang=bn
    -- Respone :
             [
                {
                    "id": 1,
                    "question": "This is a test question",
                    "answer": "This is a test answer"
                }
             ]

             [
                {
                    "id": 1,
                    "question": "यह एक परीक्षण प्रश्न है",
                    "answer": "यह एक परीक्षण उत्तर है"
                }
             ]

             [
                {
                    "id": 1,
                    "question": "এটি একটি পরীক্ষার প্রশ্ন",
                    "answer": "এটি একটি পরীক্ষার উত্তর"
                },

             ]

# Username & Password (Admin)

username : Faqadmin
password : Admin_9580
