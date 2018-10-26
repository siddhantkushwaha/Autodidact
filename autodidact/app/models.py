from django.contrib.auth.models import User
from django.db import models


class ForumUser(models.Model):
    django_user = models.OneToOneField(User)
    reputation = models.IntegerField(default=0)

    def __str__(self):
        return str(self.django_user.username)


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    use_count = models.IntegerField(default=0)
    creation_time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(ForumUser)

    def __str__(self):
        return str(self.name) + ' ;' + str(self.created_by)


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    tags = models.ManyToManyField(Tag)
    view_count = models.IntegerField(default=0)
    upvote_count = models.IntegerField(default=0)
    downvote_count = models.IntegerField(default=0)
    creation_time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(ForumUser)

    def __str__(self):
        return str(self.title) + ' ;' + str(self.creation_time)


class Answer(models.Model):
    description = models.CharField(max_length=1000)
    post = models.ForeignKey(Post)
    upvote_count = models.IntegerField(default=0)
    downvote_count = models.IntegerField(default=0)
    creation_time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(ForumUser)

    def __str__(self):
        return str(self.description)[:20] + ' ;' + str(self.creation_time)


class Comment(models.Model):
    description = models.CharField(max_length=100)
    post = models.ForeignKey(Post, null=True)
    answer = models.ForeignKey(Answer, null=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(ForumUser)

    def __str__(self):
        return str(self.description)[:20] + ' ;' + str(self.creation_time)
