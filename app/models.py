from django.db import models

# Create your models here.
class Questions(models.Model):
    question = models.TextField(blank=False)
    wiki_terms = models.CharField(max_length=200,null=False)
    wiki_text = models.TextField(null=False)
    answer = models.CharField(max_length=200)
    prediction_score = models.FloatField(default=0)
