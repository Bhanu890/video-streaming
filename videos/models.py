from django.db import models

# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(
        upload_to="videos/",
        blank=True,
        null=True,
    )
    thumbnail = models.ImageField(
        upload_to="thumbnails/",
        blank=True,
        null=True,
    )
    hls_playlist = models.CharField(max_length = 500, blank=True, null = True,)
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