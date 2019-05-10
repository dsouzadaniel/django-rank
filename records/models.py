from django.db import models

# Create your models here.
class Record(models.Model):
    title = models.CharField(max_length=30)
    abstract = models.TextField()

    feature_a = models.IntegerField()
    feature_b = models.IntegerField()
    feature_c = models.IntegerField()
    feature_d = models.IntegerField()
    feature_e = models.IntegerField()

    def __str__(self):
        return str(self.title)