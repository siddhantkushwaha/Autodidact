from django.contrib.auth.models import User
from django.db import models

'''The ForumUser class is used to create a One To One Field Mapping between the default User Class provided by Django
and a Forum User exteding the User class as needed in the discussion forum schema'''


class ForumUser(models.Model):
    django_user = models.OneToOneField(User)
    reputation = models.IntegerField(default=0)

    def __str__(self):
        return str(self.django_user.username)


'''The Tag Class is needed for creating tags for each post being added on the discussion forum,one or more tags can be
associated with a post,so a Many To Many Feold Mapping exists between a Post and Tag'''


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    use_count = models.IntegerField(default=0)
    creation_time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(ForumUser)

    def __str__(self):
        return str(self.name) + ' ;' + str(self.created_by)


'''The Post Class is needed for creating posts which can be added by a user on the forum, the class contains attributes as
stated in the database schema for the discussion forum'''


class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    tags = models.ManyToManyField(Tag)
    up_voters = models.ManyToManyField(ForumUser, related_name='up_voted_post')
    down_voters = models.ManyToManyField(ForumUser, related_name='down_voted_post')
    viewers = models.ManyToManyField(ForumUser, related_name='viewed_post')
    closed = models.BooleanField(default=False)
    creation_time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(ForumUser, related_name='created_post')

    def __str__(self):
        return str(self.title) + ' ;' + str(self.creation_time)


'''The Answer Class is needed for creating answers to posts submitted by users on the forum, as each answer exists for a 
particular post, it is dependant on it hence a foreign key of the Post Class.'''


class Answer(models.Model):
    description = models.CharField(max_length=1000)
    post = models.ForeignKey(Post)
    up_voters = models.ManyToManyField(ForumUser, related_name='up_voted_answer')
    down_voters = models.ManyToManyField(ForumUser, related_name='down_voted_answer')
    accepted = models.BooleanField(default=False)
    creation_time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(ForumUser, related_name='created_answer')

    def __str__(self):
        return str(self.description)[:20] + ' ;' + str(self.creation_time)


'''The Comment Class is needed for adding comments on posts and answers submitted by users on the forum,each comment exists
for a particular post or answer, it is dependant on it hence a foreign key exists with the Post Class and the Answer Class.'''


class Comment(models.Model):
    description = models.CharField(max_length=100)
    post = models.ForeignKey(Post, null=True)
    answer = models.ForeignKey(Answer, null=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(ForumUser, related_name='created_comment')

    def __str__(self):
        return str(self.description)[:20] + ' ;' + str(self.creation_time)