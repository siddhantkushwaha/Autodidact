from django.db import models


class ForumUser(models.Model):
    user_id = models.IntegerField(null=False, unique=True)
    reputation = models.IntegerField(null=False, default=0)

    def __str__(self):
        return str(self.user_id)


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    use_count = models.IntegerField(default=0)
    creation_time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(ForumUser, on_delete=models.SET_NULL, null=True)

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
