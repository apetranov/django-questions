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
  #### Copy the example environment file and edit it:
  ```bash
  cp .env.example .env
  ```
  #### Then open .env and set your secret key (you can generate one using Python):
    ```bash
    python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
    ```
  #### Paste that key into .env:
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
## 🤔 How to use the app?

### 1. Ask a question
Click "Ask a question" button to open the question creation page.
![askquestion](https://github.com/user-attachments/assets/1d6f6b5a-42b1-4de0-aab2-c78b640e124d)

### 2. Question creation
To create a question fill both the title and content fields and click "Ask". You can also click "Back to questions" to go back to the questions page.
![createquestion](https://github.com/user-attachments/assets/e53ea28d-8260-4f2b-9923-9d4f1b14c6eb)

### 3. Answers
Click on a question to open up the answers for that question.
![questioncreated](https://github.com/user-attachments/assets/768a7c40-4364-46e9-a5b4-3e491e51e174)

### 4. Add answer
Click on "Add answer" to open the answer creation page or "Back to questions" to go back to the questions page.
![answer](https://github.com/user-attachments/assets/f141ad41-14fb-4995-8b05-51629ffd6904)

### 5. Answer creation
Fill up the content field and click on "Submit Answer" to create an answer. You can also click "Back to answers" to go back to the answers page for this question.
![answercreation](https://github.com/user-attachments/assets/d607ba9e-ffd5-4508-835c-56ee4700ddc7)


