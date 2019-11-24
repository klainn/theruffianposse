from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect
import datetime
from time import mktime
import urllib.request
import json
from .models import WarcraftLogsSettings, RaiderIOSettings, GuildNews, HelpfulGuildLinks, GuildAddonLinks, GuildApplications
from .forms import ApplicationForm
from .blizzard_api import get_character_information


def get_json_data(json_url):
    req = urllib.request.Request(
        json_url,
        data=None,
        headers={'User-Agent': 'Mozilla/5.0'}
    )
    with urllib.request.urlopen(req) as url:
        data = json.loads(url.read().decode())
        return data


def home(request):
    warcraftlog_settings = WarcraftLogsSettings.objects.all().values('days_to_show', 'api_url')
    raiderio_settings = RaiderIOSettings.objects.all().values('api_url')
    guild_news = GuildNews.objects.filter(active=True).order_by('-added_on')
    helpful_links = HelpfulGuildLinks.objects.filter(link_active=True)
    addon_links = GuildAddonLinks.objects.all()

    now = datetime.datetime.now()
    a_month_ago_in_seconds = mktime(
        (now - datetime.timedelta(days=int(warcraftlog_settings[0]['days_to_show']))).timetuple()) * 1000.0

    warcraft_logs_api = warcraftlog_settings[0]['api_url'].format(a_month_ago_in_seconds)
    warcraft_logs_json = get_json_data(warcraft_logs_api)

    guild_raid_rankings = raiderio_settings[0]['api_url']
    guild_raid_rankings = get_json_data(guild_raid_rankings)

    return render(request, 'front_page.html', {'warcraft_logs': warcraft_logs_json, 'guild_raid_rankings': guild_raid_rankings, 'guild_news': guild_news, 'helpful_links': helpful_links, 'addon_links': addon_links})


def read_news(request, id):
    news_post = GuildNews.objects.get(pk=id)
    return render(request, 'read_news.html', {'news_post': news_post})


def apply_to_guild(request):

    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            armory_data = str(data['character_armory_link']).split('/')
            character_details = get_character_information(armory_data[6], armory_data[7])
            print(character_details)
            applicant = GuildApplications(
                character_armory_link=data['character_armory_link'],
                discord_username=data['discord_username'],
                character_image_url=character_details['character_image_url'],
                character_name=character_details['character_name'],
                character_realm=character_details['character_realm'],
                character_class=character_details['character_class'],
                character_level=character_details['character_level'],
                character_item_level_equipped=character_details['character_item_level_equipped']
            )
            try:
                applicant.save()
            except IntegrityError:
                message = 'Looks like you have already applied once.'
                return render(request, 'oops.html', {'message': message})
            return redirect('home')
    else:
        current_applicants = GuildApplications.objects.filter(application_status='Pending')
        form = ApplicationForm()

    return render(request, 'apply.html', {'form': form, 'current_applicants': current_applicants})
