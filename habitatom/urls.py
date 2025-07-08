from django.urls import path

from habitatom.views import (HabitListView, HabitDetailView,
                             HabitCreateView, HabitUpdateView, HabitDeleteView)

urlpatterns = [
    path('', HabitListView.as_view(), name='habit_list'),
    path('<int:pk>/', HabitDetailView.as_view(), name='habit_detail'),
    path('new/', HabitCreateView.as_view(), name='habit_create'),
    path('<int:pk>/edit/', HabitUpdateView.as_view(), name='habit_edit'),
    path('<int:pk>/delete/', HabitDeleteView.as_view(), name='habit_confirm_delete'),
]
