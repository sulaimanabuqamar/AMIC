from django.shortcuts import render
from .models import Timeline, headTeam, organizingcommitteeTeam, memberTeam, advisorTeam
# Create your views here.

def Home(request):
    return render(request, "Home.html")

def About(request):
    return render(request, "About.html")

def timelineDetail(request):
    timeline_data = Timeline.objects.all()
    context = {'timeline_data': timeline_data}
    return render(request, 'Timeline.html', context)

from django.shortcuts import render
from .models import headTeam, organizingcommitteeTeam, memberTeam, advisorTeam

def teamDetail(request):
    head_members = headTeam.objects.all()
    org_committee_members = organizingcommitteeTeam.objects.all()
    members = memberTeam.objects.all()
    advisors = advisorTeam.objects.all()

    team_data = {
        'head_members': head_members,
        'org_committee_members': org_committee_members,
        'members': members,
        'advisors': advisors,
    }
    return render(request, 'Team.html', team_data)



