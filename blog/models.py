from django.db import models
from django.db.models import permalink
from django.contrib.auth.models import User

class Blog(models.Model):
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    body = models.TextField()
    posted = models.DateField(db_index=True, auto_now_add=True)
    author = models.ForeignKey(User)
    category = models.ForeignKey('blog.Category')

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, {'slug': self.slug})

    class Meta:
        verbose_name_plural = ("Entries")

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return self.title

    @permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, {'slug': self.slug})

    class Meta:
        verbose_name_plural = ("Categories")




