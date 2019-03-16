import os
import json
import time
from django.core.management.base import BaseCommand
from std_bounties.client import BountyClient
from analytics.client import AnalyticsClient
from django.conf import settings
from slackclient import SlackClient
from bounties.redis_client import redis_client
from bounties.sqs_client import sqs_client
import logging

logger = logging.getLogger('django')


class Command(BaseCommand):
    help = 'Listen to SQS queue for contract events'

    def handle(self, *args, **options):
        try:
            bounty_client = BountyClient()
            analytics_client = AnalyticsClient()
            sc = SlackClient(settings.SLACK_TOKEN)

            # poll by the second
            if not settings.LOCAL:
                time.sleep(1)

            response = sqs_client.receive_message(
                QueueUrl=settings.QUEUE_URL,
                AttributeNames=['MessageDeduplicationId'],
                MessageAttributeNames=['All'],
            )

            messages = response.get('Messages')

            message = messages[0]

            analytics_client.receive_message(message)

        except Exception as e:
            # goes to rollbar
            logger.exception(e)
            raise e
