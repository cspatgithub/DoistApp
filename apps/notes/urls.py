from django.urls import path
from . import views

urlpatterns = [
    path('notes', views.NoteListView, name='notes'),
    path('notes/create', views.NoteCreateView.as_view(), name='note-create'),
    path('notes/<slug:slug>', views.NoteDetailView.as_view(), name='note-detail'),
    path('notes/<slug:slug>/update', views.NoteUpdateView.as_view(), name='note-update'),
    path('notes/<slug:slug>/delete', views.NoteDeleteView.as_view(), name='note-delete'),
]