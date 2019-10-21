from django.shortcuts import render
from sportnews import serializers, models 
from rest_framework import generics
from django.shortcuts import get_object_or_404 
from rest_framework.response import Response

# Create your views here.
class NewsView(generics.ListAPIView):

    queryset = models.News.objects.all() 
    serializer_class = serializers.NewsSerializer

class LeagueView(generics.ListAPIView):

    queryset = models.League.objects.all()
    serializer_class = serializers.LeagueSerializer
    
class StandingView(generics.ListAPIView):

    queryset = models.Standing.objects.all() 
    serializer_class = serializers.StandingTeamSerializer 
 
    def list(self, request, leagueID):
        league = get_object_or_404(models.League,pk=leagueID)
        standings = self.get_queryset().filter(league = league)
        serializer = self.serializer_class(standings, many=True)
        return Response( serializer.data )

class FixtureView(generics.ListAPIView):

    queryset = models.Match.objects.all() 
    serializer_class = serializers.MatchTeamSerializer 
 
    def list(self, request, leagueID):
        league = get_object_or_404(models.League,pk=leagueID)
        standings = self.get_queryset().filter(league = league)
        serializer = self.serializer_class(standings, many=True)
        return Response( serializer.data )


class PredictionView(generics.ListAPIView):

    queryset = models.PredictionList.objects.all() 
    serializer_class = serializers.PredictionListSerializer 


 
