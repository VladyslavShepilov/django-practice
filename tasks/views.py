from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from .models import Task, Tag
from .forms import TaskForm


class TaskListView(generic.ListView):
    model = Task
    template_name = "tasks/homepage.html"
    context_object_name = "tasks"
    paginate_by = 5

    def get_queryset(self):
        return Task.objects.prefetch_related("tags")

    def post(self, request, *args, **kwargs):
        task = Task.objects.get(pk=request.POST.get("task_id"))
        task.done = not task.done
        task.save()
        return self.get(request, *args, **kwargs)


class TaskCreateView(generic.CreateView):
    model = Task
    template_name = "tasks/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("tasks:home")


class TaskUpdateView(generic.UpdateView):
    model = Task
    template_name = "tasks/task_form.html"
    form_class = TaskForm
    success_url = reverse_lazy("tasks:home")


class TaskDeleteView(generic.DeleteView):
    model = Task
    template_name = "tasks/task_confirm_delete.html"
    success_url = reverse_lazy("tasks:home")


class TagListView(generic.ListView):
    model = Tag
    template_name = "tasks/tag_list.html"
    context_object_name = "tags"
    paginate_by = 5


class TagCreateView(generic.CreateView):
    model = Tag
    template_name = "tasks/tag_form.html"
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    template_name = "tasks/tag_form.html"
    fields = "__all__"
    success_url = reverse_lazy("tasks:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    template_name = "tasks/tag_confirm_delete.html"
    success_url = reverse_lazy("tasks:tag-list")
