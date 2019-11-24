from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length = 200)
    date = models.DateTimeField(auto_now=True)
    body = models.TextField()
    img = models.ImageField(upload_to="image_folder", null=True, blank=True)

    field1 = models.CharField(blank=True, null=True, max_length=10)
    field2 = models.CharField(blank=True, null=True, max_length=10)
    field3 = models.CharField(blank=True, null=True, max_length=10)
    field4 = models.CharField(blank=True, null=True, max_length=10)
    field5 = models.CharField(blank=True, null=True, max_length=10)
    field6 = models.CharField(blank=True, null=True, max_length=10)
    field7 = models.CharField(blank=True, null=True, max_length=10)
    field8 = models.CharField(blank=True, null=True, max_length=10)
    field9 = models.CharField(blank=True, null=True, max_length=10)
    field10 = models.CharField(blank=True, null=True, max_length=10)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    class Meta:
        ordering = ['-id']


