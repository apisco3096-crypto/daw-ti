from django.db import models

# Create your models here.
class Portafolio(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    imagen = models.ImageField(upload_to='portfolio/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = 'Portafolio'
        verbose_name_plural = 'Portafolios'
        ordering = ['-created_at']
        db_table = 'portafolio'