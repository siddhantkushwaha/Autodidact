from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='UserProfile')
    #TODO add uer image field

    def __str__(self):
        return self.user.username


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    use_count = models.IntegerField(default=0)
    creation_time = models.TimeField(auto_now_add=True)
    created_by = models.IntegerField(default=1)

    def __str__(self):
        return str(self.name) + ' ;' + str(self.use_count) + ' ;' + str(self.creation_time)


class Thread(models.Model):
    title = models.CharField(max_length=100)
    description = models.IntegerField()
    view_count = models.IntegerField(default=0)
    upvote_count = models.IntegerField(default=0)
    downvote_count = models.IntegerField(default=0)
    creation_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return str(self.title) + ' ;' + str(self.creation_time)


class Answer(models.Model):
    description = models.IntegerField()
    upvote_count = models.IntegerField(default=0)
    downvote_count = models.IntegerField(default=0)
    creation_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return str(self.description)[:20] + ' ;' + str(self.creation_time)


class Comment(models.Model):
    description = models.CharField(max_length=100)
    creation_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return str(self.description)[:20] + ' ;' + str(self.creation_time)