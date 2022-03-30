from django.db import models
from django.urls import reverse
from messagenode.models import Messagenode

from person.models import Person

class Thread(models.Model):
    people = models.ManyToManyField("person.Person")
    messages = models.ManyToManyField(Messagenode)

    class Meta:
        verbose_name = "Thread"
        verbose_name_plural = "Threads"

    def __str__(self):
        return f"Thread #{self.pk} "

    def get_absolute_url(self):
        return reverse("Thread_detail", kwargs={"pk": self.pk})
