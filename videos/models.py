from django.db import models

# Create your models here.
class videos(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    STATUS_CHOICES= [
        ('uploaded', 'Uploaded'),
        ('processing', 'Processing'),
        ('ready', 'Ready'),
        ('failed', 'Failed'),
        ]

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='uploaded')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Video'