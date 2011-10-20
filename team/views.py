from team.models import Team

from django.shortcuts import render_to_response

def index(request):
    return render_to_response('team/index.html', {
        'team': Team.objects.all(),
    })


