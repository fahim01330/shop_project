# Simple Product API - Module 12

Built from the supplied assignment.

## Setup
```bash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate # Linux/macOS
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py create_test_user
python manage.py runserver
```

## API
GET/POST `http://127.0.0.1:8000/api/products/`

GET is public. POST requires `Authorization: Token YOUR_TOKEN`.
Pagination is 5 products/page; page 2: `/api/products/?page=2`.

Example JSON:
```json
{"name":"Notebook","description":"A notebook with 100 pages.","price":"120.00","stock":25}
```

Validation rejects empty names, price <= 0, negative stock, and non-integer stock.
