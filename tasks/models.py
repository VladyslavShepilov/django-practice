from django.db import models


class Task(models.Model):
    content = models.TextField(max_length=500)
    datetime = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(default=None, null=True, blank=True)
    done = models.BooleanField()
    tags = models.ManyToManyField("Tag", related_name="tags")


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
