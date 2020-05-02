from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .models import Note
from django.contrib.auth.mixins import LoginRequiredMixin

class NoteCreateView(LoginRequiredMixin, generic.CreateView):
    model = Note
    fields = [
        'title',
        'text'
    ]
    template_name = 'notes/note_form.html'

    def get_success_url(self):
        return reverse('notes')

    def form_valid(self, form):
        form.instance.of = self.request.user
        return super().form_valid(form)


def NoteListView(request):
    notes = Note.objects.filter(of=request.user)

    context = {
        'notes': notes
    }

    return render(request, 'notes/note_list.html', context=context)


class NoteDetailView(LoginRequiredMixin, generic.DetailView):
    model = Note
    template_name = 'notes/note_detail.html'


class NoteUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Note
    fields = [
        'title',
        'text'
    ]
    template_name = 'notes/note_update.html'

    def get_success_url(self):
        return reverse('notes')

    def form_valid(self, form):
        form.instance.of = self.request.user
        return super().form_valid(form)


class NoteDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Note
    template_name = 'notes/note_delete.html'

    def get_success_url(self):
        return reverse('notes')
