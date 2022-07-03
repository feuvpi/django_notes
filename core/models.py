from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Note(models.Model):
    note = models.TextField()
    note_date = models.DateTimeField(auto_now=True, verbose_name='Note Date')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'note'

    def __str_(self):
        return self.note

    def get_data_note(self):
        return self.note_date.strftime('%d/%m/%Y %H:%M')


