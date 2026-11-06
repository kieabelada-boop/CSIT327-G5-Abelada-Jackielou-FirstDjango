# CSIT327-G5-Abelada-Jackielou-FirstDjango

Jackielou C. Abelada
G5

## How to Run the Project

1. **Clone the Repository**
   ```bash
   git clone <your-repository-url>
   cd campusconnect

   python -m venv .venv
# Windows (cmd):
.venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
