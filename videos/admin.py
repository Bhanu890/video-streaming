from django.contrib import admin
from .models import Video
from .streaming import process_video

# Register your models here.
#admin.site.register(Video)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        old_file = None

        if change:
            old_file = (Video.objects.filter(pk = obj.pk)
                        .values_list("video_file", flat=True)
                        .first()
                        )

        super().save_model(request, obj, form, change)

        new_file = obj.video_file.name if obj.video_file else None

        if new_file and new_file != old_file:
            process_video(obj.pk)
            