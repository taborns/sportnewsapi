from rest_framework import serializers 
from sportnews import models 

class NewsSerializer(serializers.ModelSerializer):
    contents = serializers.SerializerMethodField()
    
    def get_contents(self, obj):
        return obj.content.split("\n")

    class Meta:
        model = models.News 
        exclude = 'id',

class LeagueSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.League
        fields = '__all__'

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Team 
        fields = 'name', 'logo'

class StandingSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Standing
        fields = '__all__'

class MatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Match
        exclude = 'status','league'

class MatchTeamSerializer(MatchSerializer):

    local_team = TeamSerializer()
    away_team = TeamSerializer() 

class PredictionListSerializer(serializers.ModelSerializer):

    match = MatchTeamSerializer()

    class Meta:
        model = models.PredictionList
        fields = '__all__'

class PredictionSerializer(serializers.ModelSerializer):

    predictionlist = PredictionListSerializer()

    class Meta:
        model = models.Prediction 
        exclude = 'status','local_result','away_result'

class StandingTeamSerializer(StandingSerializer):
    team = TeamSerializer()