from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
import datetime


def Index(request):
    today = datetime.date.today()
    return render(request, 'general/index.html', {'today': today})

@login_required
def Home(request):
    today_tasks = Task.objects.filter(of=request.user, start_date=datetime.date.today(), status='Uncompleted')
   
    context = {
        'today_tasks': today_tasks,
    }

    return render(request, 'general/home.html', context=context)


class TaskCreateView(LoginRequiredMixin, generic.CreateView):
    model = Task
    fields = [
        'name',
        'details',
        'start_date',
        'end_date',
        'start_time',
        'end_time',
        'status'
    ]
    template_name = 'tasks/task_form.html'

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        form.instance.of = self.request.user
        return super().form_valid(form)


@login_required
def TaskListView(request):
    tasks = Task.objects.filter(of=request.user)

    context = {
        'tasks': tasks
    }

    return render(request, 'tasks/task_list.html', context=context)


class TaskDetailView(LoginRequiredMixin, generic.DetailView):
    model = Task
    template_name = 'tasks/task_detail.html'


class TaskUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Task
    fields = [
        'name',
        'details',
        'start_date',
        'end_date',
        'start_time',
        'end_time',
        'status'
    ]
    template_name = 'tasks/task_update.html'

    def get_success_url(self):
        return reverse('home')

    def form_valid(self, form):
        form.instance.of = self.request.user
        return super().form_valid(form)


@login_required
def UpcomingTaskView(request):
    today = datetime.date.today() + datetime.timedelta(days=1)
    end = today + datetime.timedelta(weeks=64)
    upcoming_tasks = Task.objects.filter(of=request.user, start_date__range=[today, end])

    context ={
        'upcoming_tasks': upcoming_tasks
    }

    return render(request, 'tasks/tasks_upcoming.html', context=context)


@login_required
def CompletedTaskView(request):
    tasks = Task.objects.filter(of=request.user, status__exact='Completed')

    context = {
        'tasks': tasks
    }

    return render(request, 'tasks/task_completed.html', context=context)


class TaskDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Task
    template_name = 'tasks/task_delete.html'

    def get_success_url(self):
        return reverse('tasks')
