import datetime
import logging
from django.db import transaction

from std_bounties.models import Bounty, Fulfillment
from analytics.models import BountyStats




logger = logging.getLogger('django')

class BountyStatsClient:

    @transaction.atomic
    def issue_bounty(self, bounty_id, inputs, event_timestamp):
        bounty_date = datetime.datetime.fromtimestamp(
                int(event_timestamp)).date()
        bounty_stat, created = BountyStats.objects.get_or_create(stats_date=bounty_date)
        bounty_stat.bounties_issued += 1
        bounty_stat.draft_bounties += 1
        bounty_stat.save()

    def kill_bounty(self, bounty_id):
        bounty = Bounty.objects.get(bounty_id=bounty_id)

        bounty_date = bountiy.created.date()

        bounty_stat = BountyStats.objects.get(stats_date=bounty_date)

        #current state -= 1
        bounty_stat.dead_bounties += 1

    # def fulfill_bounty(
    #         self,
    #         bounty_id,
    #         fulfillment_id,
    #         inputs,
    #         event_timestamp,
    #         transaction_issuer):
    #     fulfillment = Fulfillment.objects.filter(
    #         fulfillment_id=fulfillment_id, bounty_id=bounty_id
    #     ).exists()
    #     if fulfillment:
    #         return
