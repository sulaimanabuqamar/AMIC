from .models import *
from itertools import chain
from django.shortcuts import render, get_object_or_404

# Create your views here.

def Home(request):
    return render(request, "Home.html", {"timelines": Timeline.objects.all()})

def About(request):
    photos = aboutUsPhoto.objects.first()
    context = {
        'photos': photos,
        "timelines": Timeline.objects.all()
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
        "timelines": Timeline.objects.all()
    }    
    return render(request, "Leaderboard.html", context)

def Contact(request):
    return render(request, "Contact.html", {"timelines": Timeline.objects.all()})

def timelineDetail(request, timeline_id):
    timeline_data = Timeline.objects.get(timeline_id=timeline_id).activities.all()
    context = {'timeline_data': timeline_data,"timelines": Timeline.objects.all()}
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
        "timelines": Timeline.objects.all()
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
        "timelines": Timeline.objects.all()
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
        "timelines": Timeline.objects.all()
    }
    return render(request, 'Team/Alumni.html', team_data)

def activity_detail(request, activity_id):
    entry = get_object_or_404(Activity, activity_id=activity_id)
    photos = entry.photos.all()
    return render(request, 'TimelineDetail.html', {'entry': entry, 'photos': photos,"timelines": Timeline.objects.all()})