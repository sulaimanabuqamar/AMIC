from .models import Timeline, headTeam, committeeTeam, memberTeam, advisorTeam
from itertools import chain
from django.shortcuts import render, get_object_or_404

# Create your views here.

def Home(request):
    return render(request, "Home.html")

def About(request):
    return render(request, "About.html")

def Leaderboard(request):
    # Assuming you have the following models
    members = memberTeam.objects.all()
    committee_members = committeeTeam.objects.all()

    # Combine both lists into a single list
    combined_members = list(chain(members, committee_members))

    # Sort the combined list based on Amicoins
    sorted_combined_members = sorted(combined_members, key=lambda x: x.amicoins, reverse=True)

    context = {
        'sorted_combined_members': sorted_combined_members,
    }    
    return render(request, "Leaderboard.html", context)

def Contact(request):
    return render(request, "Contact.html")

def timelineDetail(request):
    timeline_data = Timeline.objects.all()
    context = {'timeline_data': timeline_data}
    return render(request, 'Timeline.html', context)

def teamDetail(request):
    head_members = headTeam.objects.all()
    org_committee_members = committeeTeam.objects.all()
    members = memberTeam.objects.all()
    advisors = advisorTeam.objects.all()

    team_data = {
        'head_members': head_members,
        'org_committee_members': org_committee_members,
        'members': members,
        'advisors': advisors,
    }
    return render(request, 'Team.html', team_data)

def timeline_detail(request, timeline_id):
    entry = get_object_or_404(Timeline, timeline_id=timeline_id)
    photos = entry.photos.all()
    return render(request, 'TimelineDetail.html', {'entry': entry, 'photos': photos})
