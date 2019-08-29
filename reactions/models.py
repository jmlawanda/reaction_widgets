from django.db import models


class reactions(models.Model):
    upvote = models.IntegerField(default=0)
    funny = models.IntegerField(default=0)
    love = models.IntegerField(default=0)
    last_session_id =models.TextField(default="")
