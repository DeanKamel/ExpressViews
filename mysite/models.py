from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Article (models.Model):
    body = models.TextField()
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    slug = models.SlugField(max_length=200)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='article_likes')
    dislikes = models.ManyToManyField(User, related_name='article_dislikes')

    TOPIC_CHOICES = (
        ("Politics", "Politics"),
        ("Sports", "Sports"),
        ("Tech", "Tech"),
        ("Travel", "Travel"),
        ("Food", "Food"),
        ("Music", "Music"),
    )
    topic = models.CharField(max_length=350, choices=TOPIC_CHOICES, default='...')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('mysite:Politics_detail', args=[self.slug])

    def total_likes(self):
        return self.likes.count()

    def total_dislikes(self):
        return self.dislikes.count()


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    #user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user', null=True)
    name = models.CharField(max_length=200)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.name)


class Report(models.Model):
    title = models.CharField(max_length=350)
    email = models.EmailField()
    reason = models.TextField()

    def __str__(self):
        return self.title






