from django.db import models
from django.conf import settings
from django.urls import reverse

# pip install misaka
import misaka

from groups.models import Group

from django.contrib.auth import get_user_model
User = get_user_model()


class Post(models.Model):
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) # Changed auto_now to auto_now_add
    updated_at = models.DateTimeField(auto_now=True) # Added for tracking updates
    message = models.TextField()
    message_html = models.TextField(editable=False)
    group = models.ForeignKey(Group, related_name="posts", null=True, blank=True, on_delete=models.CASCADE)

    POST_TYPES = [
        ('observation', 'Observation'),
        ('astrophoto', 'Astrophoto'),
        ('question', 'Question'),
        ('discussion', 'Discussion'),
        ('guide', 'Guide/Tutorial'),
    ]
    post_type = models.CharField(
        max_length=20,
        choices=POST_TYPES,
        default='discussion',
    )
    image = models.ImageField(upload_to='posts_images/', blank=True, null=True)
    observation_date = models.DateField(blank=True, null=True)
    location_description = models.CharField(max_length=255, blank=True, null=True)
    equipment_used = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.get_post_type_display()} by {self.user.username}: {self.message[:50]}"

    def save(self, *args, **kwargs):
        self.message_html = misaka.html(self.message)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse(
            "posts:single",
            kwargs={
                "username": self.user.username,
                "pk": self.pk
            }
        )

    class Meta:
        ordering = ["-created_at"]
        # unique_together = ["user", "message"] # Removed for more flexibility
