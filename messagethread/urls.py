from django.urls import path
from messagethread.views import MessageThreadDetailView, MessageThreadListView, get_threads_by_user


app_name = "thread"

urlpatterns = [
    path('', MessageThreadListView.as_view(), name='threads'),
    path('<int:pk>/', MessageThreadDetailView.as_view(), name='thread'),
    path('threads-by-person/<int:pk>/', get_threads_by_user, name="thread-by-user")
]