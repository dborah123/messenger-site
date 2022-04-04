from django.urls import path
from person.views import PersonDetailView, PersonListView, UserDetailView, UserListView

app_name = "person"

urlpatterns = [
    path('', PersonListView.as_view(), name="people"),
    path('<int:pk>/', PersonDetailView.as_view(), name="person"),
    path('user/', UserListView.as_view(), name="users"),
    path('user/<int:pk>', UserDetailView.as_view(), name="user")
]
