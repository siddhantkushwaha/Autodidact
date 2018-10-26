from django.test import TestCase
from .models import Tag,Post,Answer,Comment


'''
Testing the Tag Model
'''

class TagModelTest(TestCase):
    def setUp(self):
        Tag.objects.create(name="Test_Tag",use_count=0,created_by=2)

    def test_tag(self):
        test_tag = Tag.objects.get(name="Test_Tag")
        self.assertEqual(str(test_tag),test_tag.name)

'''
Testing the Post Model
'''

# class PostModelTest(TestCase):
#     def setUp(self):
#         Post.objects.create(title="Test_Post",description="testing the post model",tags=1,created_by=2)
#
#     def test_post(self):
#         test_post = Post.objects.get(name="Test_Post")
#         self.assertEqual(str(test_post),test_post.title)

'''
Testing the Answer Model
'''

# class AnswerModelTest(TestCase):
#     def setUp(self):
#         Answer.objects.create(description="testing the answer model",post=13,created_by=2)
#
#     def test_answer(self):
#         test_answer = Answer.objects.get(created_by=2)
#         self.assertEqual(str(test_answer),test_answer.created_by)

'''
Testing the Comment Model

'''

# class CommentModelTest(TestCase):
#     def setUp(self):
#         Comment.objects.create(description="testing the comment model",post=13,created_by=2)
#
#     def test_comment(self):
#         test_comment = Tag.objects.get(name="Test_Tag")
#         self.assertEqual(str(test_comment),test_comment.created_by)
