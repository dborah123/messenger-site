from statistics import mode
from django.db import models
from django.urls import reverse

class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    contacts = models.ManyToManyField("self")

    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"

    def __str__(self) -> str:
        return f"Person: {self.first_name} {self.last_name}"

    def get_absolute_url(self):
        return reverse("Person_detail", kwargs={"pk": self.pk})