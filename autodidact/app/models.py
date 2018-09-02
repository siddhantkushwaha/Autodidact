from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=20)
    use_count = models.IntegerField(default=0)
    creation_time = models.TimeField()

    def __str__(self):
        return str(self.name) + ' ;' + str(self.use_count) + ' ;' + str(self.creation_time)


class Thread(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100000)
    view_count = models.IntegerField(default=0)
    upvote_count = models.IntegerField(default=0)
    downvote_count = models.IntegerField(default=0)
    creation_time = models.TimeField()

    def __str__(self):
        return str(self.title) + ' ;' + str(self.creation_time)


class Answer(models.Model):
    description = models.CharField(max_length=100000)
    upvote_count = models.IntegerField(default=0)
    downvote_count = models.IntegerField(default=0)
    creation_time = models.TimeField()

    def __str__(self):
        return str(self.description)[:20] + ' ;' + str(self.creation_time)


class Comment(models.Model):
    description = models.CharField(max_length=100)
    creation_time = models.TimeField()

    def __str__(self):
        return str(self.description)[:20] + ' ;' + str(self.creation_time)
