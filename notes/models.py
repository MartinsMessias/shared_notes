from django.db import models
from django_currentuser.db.models import CurrentUserField


class Note(models.Model):
    title = models.CharField('Title', max_length=30, null=False, blank=False)
    content = models.TextField('Content', null=False, blank=False)
    created_by = CurrentUserField(default=1, editable=False)
    created_date = models.DateTimeField(auto_now=True)
    modify_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title