from django.db import models

from tag.models import Tag


class Bookmark(models.Model):
    # user = models.ForeignKey(User)
    name = models.CharField(max_length=140)
    url = models.URLField(max_length=2000)
    tag = models.ManyToManyField(Tag)
    # thumbnail = models.ImageField()
    # star = models.BooleanField()
    # archived = models.BooleanField()
    # read_it_lator = models.BooleanField()

    def __str__(self):
        return self.name
