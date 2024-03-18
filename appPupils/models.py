from django.db import models


class Pupil(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False, blank=False, verbose_name="Student name")
    score = models.IntegerField(default=0, null=False, blank=False, verbose_name="Student score")
    image = models.ImageField(upload_to='static/', null=True, blank=True, verbose_name="Student image")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
        db_table = "students"
