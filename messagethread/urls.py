from django.urls import path
from messagethread.views import MessageThreadDetailView, MessageThreadListView


app_name = "thread"

urlpatterns = [
    path('', MessageThreadListView.as_view(), name='threads'),
    path('<int:pk>/', MessageThreadDetailView.as_view(), name='thread'),
]