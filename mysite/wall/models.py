from django.db import models
from django.utils import timezone 

class Question(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        related_name="answers",
        on_delete=models.CASCADE
    )
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Answer to: {self.question.title[:30]}..."
    
class Comment(models.Model):
    answer = models.ForeignKey(
        Answer,
        related_name="comments",
        on_delete=models.CASCADE
    )
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment on answer {self.id}"