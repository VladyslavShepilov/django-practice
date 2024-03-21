from django.urls import path, include

from .views import (
    TaskListView,
    TaskCreateView,
    TaskUpdateView,
    TaskDeleteView,
    TagListView,
    TagCreateView,
    TagUpdateView,
    TagDeleteView,
)

app_name = "tasks"
urlpatterns = [
    path("", TaskListView.as_view(), name="home"),
    path("tags", TagListView.as_view(), name="tag-list"),
    path(
        "task/create/",
        TaskCreateView.as_view(),
        name="task-create"
    ),
    path(
        "task/<int:pk>/update/",
        TaskUpdateView.as_view(),
        name="task-update"
    ),
    path(
        "task/<int:pk>/delete/",
        TaskDeleteView.as_view(),
        name="task-delete"
    ),
    path(
      "tag/create/",
      TagCreateView.as_view(),
      name="tag-create"
    ),
    path(
        "tag/<int:pk>/update/",
        TagUpdateView.as_view(),
        name="tag-update"
    ),
    path(
        "tag/<int:pk>/delete/",
        TagDeleteView.as_view(),
        name="tag-delete"
    ),
]
