from django.db import models

# Create your models here.


class GoldenThougthData(models.Model):

    CHOICES = (('Motywacja', 'Motywacja'),('Melancholia', 'Melancholia'), ('Na poprawę nastroju', 'Na poprawę nastroju'))

    name = models.CharField(max_length=80)
    category = models.CharField(max_length=50 ,choices=CHOICES)
    body = models.TextField()
    added_by = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Golden Thougth"
        verbose_name_plural = "Golden Thougths"

    def __repr__(self):
        return f'{self.body}'







