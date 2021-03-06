from django.db import models

# Create your models here.
class Task(models.Model):
  name = models.CharField(max_length=100)
  description = models.CharField(max_length=250)
  priority = models.IntegerField()

  class Meta:
    app_label = "tasks_register"

  def __str__(self):
    return self.name