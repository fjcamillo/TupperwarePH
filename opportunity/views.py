from django.shortcuts import render, get_object_or_404
from .models import opportunity_post, career_post
# Create your views here.


def index(request):
    # opportunity_objects = get_object_or_404(opportunity_post, id=id)
    object_list = opportunity_post.objects.all()
    career_list = career_post.objects.all()
    context_opp = {
        'object_list': object_list,
        'career_list': career_list,

    }
    return render(request, 'opportunity/opportunity.html', context_opp)