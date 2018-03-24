from django.db import models

# Create your models here.


class BountyStats(models.Model):
    id = models.IntegerField(primary_key=True)
    publish_date = models.DateTimeField()
    number_bounter_issued = models.IntegerField(default=18)
    number_bounter_submitted = models.IntegerField(default=18)
    # rest of statitics
