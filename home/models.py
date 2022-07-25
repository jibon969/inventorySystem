from django.db import models


class Offer(models.Model):
    title = models.CharField(max_length=120, blank=True, null=True)
    largeDevices = models.ImageField(upload_to='offer/', null=True, blank=True)
    url_field = models.URLField(max_length=120, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ["-timestamp"]