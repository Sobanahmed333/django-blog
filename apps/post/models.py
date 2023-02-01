from django.db import models


class BaseTimeStamp(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']


class Post(BaseTimeStamp):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()

    created_by = models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='post_created_by')

    REQUIRED_FIELDS = ['title', 'description']

    def __str__(self):
        return self.title
