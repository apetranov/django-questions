from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Question, Answer, Comment


def question_list(request):
    questions = Question.objects.all()
    output = ", ".join([q.title for q in questions])
    return render(request, "wall/index.html", {"questions": questions})

def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    answers = question.answers.all()
    return render(request, "wall/question_detail.html", {"question": question, "answers": answers})

def create_question(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")

        if not title or not content:
            error = "Please fill out all fields."
            return render(request, "wall/create_question.html", {"error": error})

        Question.objects.create(title=title, content=content)
        return redirect("question_list")

    return render(request, "wall/create_question.html")

def create_answer(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    if request.method == "POST":
        content = request.POST.get("content")

        if not content:
            error = "Please write an answer."
            return render(request, "wall/create_answer.html", {"question": question, "error": error})

        Answer.objects.create(question=question, content=content)
        return redirect("question_detail", question_id=question.id)  # assuming you have a question detail view

    return render(request, "wall/create_answer.html", {"question": question})


def comment_page(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    comments = answer.comments.all()
    return render(request, "wall/comment_page.html", {"answer": answer, "comments": comments})

def create_comment(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    question = answer.question

    if request.method == "POST":
        content = request.POST.get("content")

        if not content:
            error = "Please write a comment."
            return render(request, "wall/create_comment.html", {"answer": answer, "error": error})

        Comment.objects.create(answer=answer, content=content)
        return redirect("comment_page", answer_id=answer.id)  # assuming you have a question detail view

    return render(request, "wall/create_comment.html", {"answer": answer, "question": question})
