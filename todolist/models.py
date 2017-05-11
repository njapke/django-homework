from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Todo(models.Model):
    task = models.CharField(max_length=160)
    due_date = models.DateTimeField('date due') #optional human readable name
    completion = models.IntegerField(default=0,
                                     validators=[MaxValueValidator(100), #we can remove this. validation doesn't work that way. validation in forms
                                                 MinValueValidator(0)]
                                     )

    def __str__(self):
        return self.task
