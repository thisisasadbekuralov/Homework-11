from django.db import models


# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=100, unique=True, verbose_name='Category Name')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        db_table = 'category'



class Themes(models.Model):
    name = models.CharField(max_length=200)
    plan = models.CharField(max_length=100)
    category_theme = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Themes"
        verbose_name = "Themes"
        db_table = "themes"
