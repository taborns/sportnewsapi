from django.db import models
from django.utils import timezone

class Upcomingpredictions( models.Manager ):
    def get_queryset(self):
        return super().get_queryset().filter(match__schedule__gte = timezone.now() )

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField()
    thumbnail = models.FileField(upload_to='thumbs/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering ='-created_at',
        verbose_name_plural = 'News'

class League(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name 

class Team(models.Model):
    name = models.CharField(max_length = 100) 
    logo = models.FileField(upload_to='logos/') 

    def __str__(self):
        return self.name 

class Standing(models.Model):

    league = models.ForeignKey('League', related_name = 'standings', on_delete=models.CASCADE) 
    team = models.ForeignKey('Team',  related_name = 'standings', on_delete=models.CASCADE) 
    rank = models.IntegerField() 
    played = models.IntegerField() 
    goal = models.IntegerField() 
    points = models.IntegerField() 


    class Meta:
        ordering = 'rank',
        unique_together = ('league', 'team')
class Match(models.Model):
    league = models.ForeignKey('League', related_name = 'fixtures', on_delete=models.CASCADE) 
    local_team = models.ForeignKey('Team',  related_name = 'local_matches', on_delete=models.CASCADE) 
    away_team = models.ForeignKey('Team',  related_name = 'away_matches', on_delete=models.CASCADE) 
    schedule = models.DateTimeField() 
    status = models.IntegerField(
        choices = (
            (1, 'Open'),
            (2, 'Finished')
        ),
        default = 1
    )

    def __str__(self):
        return "%s Vs %s" %( self.local_team, self.away_team)

    class Meta:
        verbose_name_plural = 'Matches'

class PredictionList(models.Model):
    
    match = models.ForeignKey("Match", related_name='predictionlist', on_delete=models.CASCADE)
    objects = Upcomingpredictions()

    def __str__(self):

        return '%s' %(self.match)

class Prediction(models.Model):
    
    local_result = models.IntegerField(null=True, blank=True)
    away_result = models.IntegerField(null=True, blank=True) 
    predictionlist = models.ForeignKey('PredictionList', related_name='predictions', on_delete=models.CASCADE)

    status = models.IntegerField(
        choices = (
            (1, 'Open'),
            (2, 'Resolved')
        ),
        default = 1
    )

    def resolve(self):

        if self.match.status == 2:
            if predictionlist.match.local_result == self.local_result and predictionlist.match.away_result == self.away_result:
                self.status = 2
            else:
                self.status = 1
        
        self.save()






    


