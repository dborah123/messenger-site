from django.db import models
from django.urls import reverse
from messagenode.models import Messagenode
from person.models import Person

class MessageThread(models.Model):
    people = models.ManyToManyField(Person, blank=True)
    messages = models.ManyToManyField(Messagenode, blank=True)

    class Meta:
        verbose_name = "Thread"
        verbose_name_plural = "Threads"

    def __str__(self):
        return f"Thread #{self.pk} "

    def get_absolute_url(self):
        return reverse("Thread_detail", kwargs={"pk": self.pk})
