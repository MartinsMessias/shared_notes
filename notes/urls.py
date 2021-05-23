from django.urls import path

from . import views
from .views import NoteListView, NoteUpdateView, NoteDeleteView, NoteDetailView

urlpatterns = [
    path('', views.get_note, name='get_note'),
    path('create/', views.create_note, name='create_note'),
    path('notes/', NoteListView.as_view(), name='list_notes'),
    path('update/<pk>', NoteUpdateView.as_view(), name='update_note'),
    path('delete/<pk>', NoteDeleteView.as_view(), name='delete_note'),
    path('note/<pk>', NoteDetailView.as_view(), name='detail_note'),

]
