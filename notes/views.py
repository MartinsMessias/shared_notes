from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DeleteView, DetailView, UpdateView

from .forms import NoteForm
from .models import Note


class NoteListView(ListView):
    login_required = True
    model = Note
    template_name = 'notes/note_list.html'

    def get_queryset(self):
        return self.model.objects.filter(created_by=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(NoteListView, self).get_context_data(**kwargs)
        return context


class NoteUpdateView(UpdateView):
    login_required = True
    model = Note
    template_name = 'notes/note_form.html'
    fields = '__all__'
    success_url = reverse_lazy('list_notes')

    def get_queryset(self):
        return self.model.objects.filter(created_by=self.request.user)


class NoteDetailView(DetailView):
    login_required = True
    model = Note
    template_name = 'notes/note_detail.html'

    def get_queryset(self):
        return self.model.objects.filter(created_by=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(NoteDetailView, self).get_context_data(**kwargs)
        return context


class NoteDeleteView(DeleteView):
    login_required = True
    model = Note
    success_url = reverse_lazy('list_notes')
    template_name = 'notes/confirm_note_delete.html'

    def get_queryset(self):
        return self.model.objects.filter(created_by=self.request.user)


def get_note(request):
    try:
        note = Note.objects.order_by('?').first()
        return render(request, 'notes/note.html', {'note': note})
    except:
        return {'title': 'There are no phrases yet! Leave yours.'}


@login_required()
def create_note(request):
    if request.method == 'POST':
        form = NoteForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            created_by = User.objects.get(id=request.user.id)

            note = Note(title=title, content=content, created_by=created_by)
            note.save()

            return redirect('get_note')
    else:
        form = NoteForm()
    return render(request, 'notes/note_form.html', {'form': form})
