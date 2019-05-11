from django.db import models
from django.urls import reverse_lazy
# Create your models here.
class Record(models.Model):
    title = models.CharField(max_length=30)
    abstract = models.TextField()

    adverse_effect = models.PositiveSmallIntegerField()
    identifiable_patient = models.PositiveSmallIntegerField()
    identifiable_drug = models.PositiveSmallIntegerField()
    precondition = models.PositiveSmallIntegerField()
    mah = models.PositiveSmallIntegerField()

    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse_lazy('home')