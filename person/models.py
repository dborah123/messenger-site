from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Person(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contacts = models.ManyToManyField("self", blank=True)

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"

    def __str__(self) -> str:
        return f"Person: {self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("Person_detail", kwargs={"pk": self.pk})