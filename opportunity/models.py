from django.db import models

# Create your models here.

class opportunity_post(models.Model):
    opportunity_title = models.CharField(max_length=70)
    opportunity_story = models.TextField()
    opportunity_date = models.DateTimeField()
    opportunity_image = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.opportunity_title


class career_post(models.Model):
    career_title = models.CharField(max_length=20)
    career_description = models.TextField()
    career_payment = models.FloatField()
    career_starting_time = models.DateTimeField()
    career_finish_time = models.DateTimeField()

    def __str__(self):
        return self.career_title