from django.db import models

class Team(models.Model):
    username = models.CharField(max_length=255)
    bio = models.TextField()
    website = models.CharField(max_length=255)

    def __unicode__(self):
        return self.username

    class Meta:
        verbose_name_plural = "Team"
