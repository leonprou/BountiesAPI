from rest_framework import serializers
from analytics.models import BountyStats

class BountyStatsSerializer(serializers.ModelSerializer):

    class Meta:
        model = BountyStats
        fields = '__all__'
