from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100)
    link = models.URLField(max_length=200)
    creation_date = models.DateTimeField(auto_now_add=True)
    upvotes_amount = models.PositiveIntegerField(default=0, editable=False)
    author = models.CharField(max_length=32)

    def upvote(self):
        self.upvotes_amount += 1
        self.save()

    def __str__(self):
        return f"{self.title}|{self.author}"

    class Meta:
        ordering = ["-creation_date"]


class Comment(models.Model):
    author = models.CharField(max_length=32)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")

    def __str__(self):
        return f"by {self.author} for {self.post.title}"

    class Meta:
        ordering = ["-creation_date"]
