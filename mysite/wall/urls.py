from django.urls import path
from . import views

urlpatterns = [
    path("", views.question_list, name="question_list"),
    path("question/<int:question_id>/", views.question_detail, name="question_detail"),
    path("ask/", views.create_question, name="create_question"),
    
    # Answers
    path("questions/<int:question_id>/answer/", views.create_answer, name="create_answer"),

    # Comments (for answers)
    path("answer/<int:answer_id>/create_comment/", views.create_comment, name="create_comment"),
    path("answer/<int:answer_id>/comments/", views.comment_page, name="comment_page"),
]
