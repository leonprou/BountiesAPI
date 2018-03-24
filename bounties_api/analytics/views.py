from django.shortcuts import render
from rest_framework import viewsets
from analytics.serializers import BountyStatsSerializer
from analytics.models import BountyStats
from rest_framework.views import APIView

# Create your views here.

class BountyStatsViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = BountyStatsSerializer
    queryset = BountyStats.objects.all()



class Leaderboard(APIView):
    def get(self, request):
        return ''
