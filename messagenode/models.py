from django.db import models
from django.urls import reverse

from person.models import Person

class Messagenode(models.Model):
    content = models.TextField()
    sender = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="receiver")

    class Meta:
        verbose_name = "Messagenode"
        verbose_name_plural = "Messagenodes"

    def __str__(self):
        return f"Messagenode #{self.pk} sent by Person #{self.person}"

    def get_absolute_url(self):
        return reverse("Messagenode_detail", kwargs={"pk": self.pk})
