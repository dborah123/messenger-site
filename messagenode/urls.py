from django.urls import path

from messagenode.views import MessagenodeDetailView, MessagenodeListView


app_name="messagenode"

urlpatterns = [
    path('', MessagenodeListView.as_view(), name="messagenodes"),
    path('<int:pk>', MessagenodeDetailView.as_view(), name='messagenode')
]
