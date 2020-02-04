from django.db import models


# Create your models here.
class Search(models.Model):

    objects = " "
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.search)  # print the exact search name instead of "object name"

    class Meta:
        verbose_name_plural = 'Searches'  # In the models the it spelled as Searchs to convert it we use this command
