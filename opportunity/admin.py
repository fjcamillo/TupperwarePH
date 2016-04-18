from django.contrib import admin
from opportunity.models import opportunity_post, career_post
# Register your models here.


class opportunitymodel(admin.ModelAdmin):
    list_display = ['opportunity_title', 'opportunity_date']
    search_fields = ['opportunity_story']

    class Meta:
        model = opportunity_post



class careermodel(admin.ModelAdmin):
    list_display = ['career_title', 'career_starting_time', 'career_finish_time']
    search_fields = ['career_title']

    class Meta:
        model = career_post


admin.site.register(opportunity_post, opportunitymodel)
admin.site.register(career_post, careermodel)


