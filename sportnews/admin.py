from django.contrib import admin
from sportnews import models
# Register your models here.

class NewsModelAdmin(admin.ModelAdmin):
    list_display = ('title',)

class StandingModelAdmin(admin.ModelAdmin):
    list_display = ('rank', 'team', 'played', 'goal', 'points')
    list_editable = ('goal', 'played', 'points')
    list_filter = ('league',)


admin.site.register( models.News, NewsModelAdmin)
admin.site.register( models.Standing, StandingModelAdmin )

admin.site.register( models.League )
admin.site.register( models.Team )
admin.site.register( models.Match )
admin.site.register( models.PredictionList )
