from .models import Timeline, head, committee, member, advisor, aboutUsPhoto
from itertools import chain
from django.shortcuts import render, get_object_or_404

# Create your views here.

def Home(request):
    return render(request, "Home.html")

def About(request):
    photos = aboutUsPhoto.objects.first()
    context = {
        'photos': photos
    }
    return render(request, 'About.html', context)

def Leaderboard(request):
    # Assuming you have the following models
    members = member.objects.all()
    committee_members = committee.objects.all()

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

def team_Highschool(request):
    head_members = head.objects.filter(team_type='highschool')
    org_committee_members = committee.objects.filter(team_type='highschool')
    members = member.objects.filter(team_type='highschool')
    advisors = advisor.objects.all()

    team_data = {
        'head_members': head_members,
        'org_committee_members': org_committee_members,
        'members': members,
        'advisors': advisors,
    }
    return render(request, 'Team/Highschool.html', team_data)

def team_Junior(request):
    head_members = head.objects.filter(team_type='junior')
    members = member.objects.filter(team_type='junior')
    advisors = advisor.objects.all()

    team_data = {
        'head_members': head_members,
        'members': members,
        'advisors': advisors,
    }
    return render(request, 'Team/Junior.html', team_data)

def team_Alumni(request):
    head_members = head.objects.filter(team_type='alumni')
    org_committee_members = committee.objects.filter(team_type='alumni')
    members = member.objects.filter(team_type='alumni')

    team_data = {
        'head_members': head_members,
        'org_committee_members': org_committee_members,
        'members': members,
    }
    return render(request, 'Team/Alumni.html', team_data)

def timeline_detail(request, timeline_id):
    entry = get_object_or_404(Timeline, timeline_id=timeline_id)
    photos = entry.photos.all()
    return render(request, 'TimelineDetail.html', {'entry': entry, 'photos': photos})
