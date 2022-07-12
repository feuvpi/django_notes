from django.contrib import admin
from core.models import Note

# Register your models here.

class NoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'note', 'note_date')
    list_filter = ('note_date',)

admin.site.register(Note, NoteAdmin)