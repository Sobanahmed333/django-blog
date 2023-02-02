from django.db import models


class BaseTimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']


class Post(BaseTimeStamp):
    title = models.CharField(max_length=255, unique=True)
    created_by = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='post_created_by')
    liked_by = models.ManyToManyField('user.User', related_name='post_liked_by', blank=True)

    REQUIRED_FIELDS = ['title', 'description']

    def __str__(self):
        return self.title


class Comment(BaseTimeStamp):
    created_by = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='comment_created_by')
    post = models.ForeignKey('post.Post', on_delete=models.CASCADE, related_name='comment_post')
    context = models.TextField()

    def __str__(self):
        return f'from: {self.created_by.email} - post: {self.post.title}'
