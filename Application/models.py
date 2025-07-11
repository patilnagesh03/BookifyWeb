from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    summary = models.TextField()
    bookPDF_url = models.URLField(null=True,blank=True)

    def __str__(self):
        return self.title
    
class HindiVersion(models.Model):
    # book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='hindi_versions')
    hindi_title = models.CharField(max_length=100)
    hindi_author = models.CharField(max_length=100)
    hindi_description = models.TextField(blank=True, null=True)
    hindi_summary = models.TextField()

    def __str__(self):
        return self.hindi_title