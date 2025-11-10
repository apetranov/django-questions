# 🐍 Django Questions 💭

> A local Django web app for anonymous questions and answers.

## ⚙️ Features
- 📝 Post questions
- 💬 Add answers
- 💭 Comment on answers

## 🚀 Run Locally(you must have Python and pip installed)

### Step 1: Clone repo
```bash
git clone https://github.com/apetranov/django-questions.git
```
### Step 2: Open folder
```bash
cd django-questions
```
### Step 3: Create virtual environment
```bash
python -m venv venv
```

### Step 4: Activate virtual environment
```bash
venv\Scripts\activate
```

### Step 5: Install required packages
```bash
pip install -r requirements.txt
```

### Step 6: Enter app folder
```bash
cd mysite
```

### Step 6.5: Create your .env file
  # Copy the example environment file and edit it:
  ```bash
  cp .env.example .env
  ```
  # Then open .env and set your secret key (you can generate one using Python):
    ```bash
    python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
    ```
  # Paste that key into .env:
  ```bash
  SECRET_KEY=your-generated-secret-key
  DEBUG=True
```

### Step 7: Apply migrations
```bash
python manage.py migrate
```

### Step 8: Run app and enjoy :) (app runs on http://127.0.0.1:8000)
```bash
python manage.py runserver
```
