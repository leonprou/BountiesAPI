from django.db import models

# Create your models here.


class BountyStats(models.Model):
    stats_date = models.DateField()
    bounties_issued = models.IntegerField(default=0)
    fulfillments_submitted = models.IntegerField(default=0)
    fulfillments_accepted = models.IntegerField(default=0)
    fulfillments_not_accepted = models.IntegerField(default=0)
    draft_bounties = models.IntegerField(default=0)
    active_bounties = models.IntegerField(default=0)
    dead_bounties = models.IntegerField(default=0)
    completed_bounties = models.IntegerField(default=0)
    exprired_bounties = models.IntegerField(default=0)


    # rest of statitics
