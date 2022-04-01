from django.urls import path
from person.views import PersonDetailView, PersonListView


app_name = "person"

urlpatterns = [
    path('', PersonListView.as_view(), name="people"),
    path('<int:pk>/', PersonDetailView.as_view(), name="person"),
]
