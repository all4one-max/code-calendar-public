from django.shortcuts import render, redirect
import requests, json
from datetime import datetime, timedelta
from selenium import webdriver
from django.contrib import messages
from .models import *
from django.http import HttpResponseRedirect
import os
from apiclient.discovery import build
from google_auth_oauthlib.flow import Flow
import re
from dateutil import tz
from django.contrib import messages

d = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

md = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12,
}

ltz = ""
# Create your views here.
def is_today_or_tomorrow(contest_date):
    nowtime = datetime.now()
    # contest_time = datetime.strptime(contest_date, "%Y-%m-%dT%H:%M:%S.%fz")
    if contest_date.month == nowtime.month and contest_date.year == nowtime.year:
        if contest_date.day - nowtime.day == 0:
            return 1
        elif contest_date.day - nowtime.day == 1:
            return 2
    return 0


def make_api_calls():
    # response = requests.get("https://www.kontests.net/api/v1/all")
    # python_data = json.loads(response.text)
    today, tomorrow = list(), list()
    python_data = []
    for contests in all_contest.objects.all():
        st = re.split("\W+", contests.start_time)
        if md.get(st[1], -1) != -1:
            start_time = datetime(
                int(st[2]), md[st[1]], int(st[0]), int(st[3]), int(st[4]), 0
            )
        et = re.split("\W+", contests.end_time)
        if md.get(et[1], -1) != -1:
            end_time = datetime(
                int(et[2]), md[et[1]], int(et[0]), int(et[3]), int(et[4]), 0
            )
        # print(contests.name,start_time,end_time)
        dic = {
            "name": contests.name,
            "url": contests.url,
            "start_time": start_time,
            "end_time": end_time,
        }
        python_data.append(dic)
    for contests in python_data:
        if contests["start_time"] != "-":
            if is_today_or_tomorrow(contests["start_time"]) == 1:
                contests["start_time"] = str(contests["start_time"])
                contests["end_time"] = str(contests["end_time"])
                today.append(contests)
            elif is_today_or_tomorrow(contests["start_time"]) == 2:
                contests["start_time"] = str(contests["start_time"])
                contests["end_time"] = str(contests["end_time"])
                tomorrow.append(contests)

        # getime = days(contests["start_time"])
        # # print(contests["name"], getime)
        # if getime == 0:
        #     today.append(contests)
        # elif getime == 1:
        #     tomorrow.append(contests)
    # print(today)
    # print(tomorrow)
    return today, tomorrow


def get_correct_url(cf_data):
    new = []
    for contest in cf_data:
        correct = contest
        if requests.get(correct["url"]).status_code != 200:
            correct["url"] = "https://codeforces.com/contests"
        new.append(correct)
    return new


def get_date_time(date_time):
    date = date_time[:10]
    time = date_time[11:16]
    # print(date)
    day = int(date[8:10])
    year = date[:4]
    month = d[int(date[5:7])]
    final = str(day) + " " + month + " " + year + " " + time
    return final


def get_date_time_helper(site_data):
    new = []
    for contests in site_data:
        correct = contests
        correct["start_time"] = get_local_time(get_date_time(correct["start_time"]))
        correct["end_time"] = get_local_time(get_date_time(correct["end_time"]))
        new.append(correct)
    return new


def get_date_time_helper_api_call(site_data):
    new = []
    for contests in site_data:
        correct = contests
        correct["start_time"] = get_date_time(correct["start_time"])
        correct["end_time"] = get_date_time(correct["end_time"])
        new.append(correct)
    return new


def home(request):
    global ltz
    ltz = datetime.now(tz.tzlocal()).tzname()
    today, tomorrow = make_api_calls()
    # if not (today) and not (tomorrow):
    # return render(request, "Kode_calendar/all.html")
    # today = get_correct_url(today)
    today = get_date_time_helper(today)
    # tomorrow = get_correct_url(tomorrow)
    tomorrow = get_date_time_helper(tomorrow)
    context = {"today": today, "tomorrow": tomorrow}
    return render(request, "Kode_calendar/home.html", context)


def call(url, site_model, name):
    global ltz
    ltz = datetime.now(tz.tzlocal()).tzname()
    responses = requests.get(url)
    site_data = json.loads(responses.text)
    if name == "cf":
        site_data = get_correct_url(site_data)
    site_data = get_date_time_helper_api_call(site_data)
    site_model.objects.all().delete()
    for contest in site_data:
        instance = site_model(
            name=contest["name"],
            url=contest["url"],
            start_time=contest["start_time"],
            end_time=contest["end_time"],
        )
        instance.save()
        instance2 = all_contest(
            name=contest["name"],
            url=contest["url"],
            start_time=contest["start_time"],
            end_time=contest["end_time"],
        )
        instance2.save()
    return


class api_calling:
    def site_call(self):
        all_contest.objects.all().delete()
        call("https://www.kontests.net//api/v1/codeforces", codeforces, "cf")
        call("https://www.kontests.net//api/v1/at_coder", atcoder, "ac")
        call("https://www.kontests.net//api/v1/hacker_rank", hackerrank, "hr")
        call("https://www.kontests.net//api/v1/hacker_earth", hackerearth, "he")
        call("https://www.kontests.net//api/v1/leet_code", leetcode, "lc")
        call("https://www.kontests.net//api/v1/top_coder", topcoder, "tc")
        return


def get_local_time(time):
    global ltz
    # print(local_timezone,utc_timezone,time)
    ltz = datetime.now(tz.tzlocal()).tzname()
    utc_timezone = tz.gettz("UTC")
    local_timezone = tz.gettz(ltz)
    time = re.split("\W+", time)
    utc_time = datetime(
        int(time[2]), md[time[1]], int(time[0]), int(time[3]), int(time[4]), 0
    )
    utc_time = utc_time.replace(tzinfo=utc_timezone)
    local_time = utc_time.astimezone(local_timezone)
    return get_date_time(str(local_time))


def get_data(instance):
    li = []
    this = instance.objects.all()
    for contest in this:
        # print(contest.name)
        local_start_time = get_local_time(contest.start_time)
        local_end_time = get_local_time(contest.end_time)
        d = {
            "name": contest.name,
            "url": contest.url,
            "start_time": local_start_time,
            "end_time": local_end_time,
        }
        li.append(d)
    return li


def all(request):
    global ltz
    ltz = datetime.now(tz.tzlocal()).tzname()
    cf_data = get_data(codeforces)
    atc_data = get_data(atcoder)
    tc_data = get_data(topcoder)
    hrd_data = get_data(hackerrank)
    hed_data = get_data(hackerearth)
    lc_data = get_data(leetcode)
    context = {
        "cf_data": cf_data,
        "atc_data": atc_data,
        "hrd_data": hrd_data,
        "hed_data": hed_data,
        "lc_data": lc_data,
        "tc_data": tc_data,
    }
    return render(request, "Kode_calendar/all.html", context)


def about(request):
    return render(request, "Kode_calendar/about.html")


REDIRECT_URI = "http://127.0.0.1:8000/google_oauth/callback/"
service_account_email = "code-calendar@wise-bongo-308711.iam.gserviceaccount.com"
scopes = ["https://www.googleapis.com/auth/calendar.events"]
JSON_FILEPATH = os.path.join(os.getcwd(), "client_id.json")
flow = Flow.from_client_secrets_file(
    JSON_FILEPATH, scopes=scopes, redirect_uri=REDIRECT_URI
)
contest_name = ""

return_url = ""


def RedirectOauthView_all(request):
    global contest_name, return_url
    return_url = "all"
    contest_name = request.POST.get("reminder_button")
    auth_url, _ = flow.authorization_url()
    return HttpResponseRedirect(auth_url)


def RedirectOauthView_home(request):
    global contest_name, return_url
    return_url = "home"
    contest_name = request.POST.get("reminder_button")
    auth_url, _ = flow.authorization_url()
    return HttpResponseRedirect(auth_url)


def Callback(request):
    global return_url
    flow.fetch_token(code=request.GET["code"])
    credentials = flow.credentials
    service = build("calendar", "v3", credentials=credentials)
    create_event(service)
    messages.success(request, "Event was successfully added to your calendar")
    if return_url == "all":
        return redirect("all")
    else:
        return redirect("home")


def add_contest_to_calendar():
    global contest_name
    for contests in all_contest.objects.all():
        if contest_name == contests.name:
            return (
                contests.url,
                get_local_time(contests.start_time),
                get_local_time(contests.end_time),
            )


def create_event(service):
    url, st, et = add_contest_to_calendar()
    st = re.split("\W+", st)
    et = re.split("\W+", et)
    start_time = datetime(int(st[2]), md[st[1]], int(st[0]), int(st[3]), int(st[4]), 0)
    end_time = datetime(int(et[2]), md[et[1]], int(et[0]), int(et[3]), int(et[4]), 0)
    timezone = "Asia/Kolkata"
    event = {
        "summary": contest_name,
        "description": url,
        "start": {
            "dateTime": start_time.strftime("%Y-%m-%dT%H:%M:%S"),
            "timeZone": timezone,
        },
        "end": {
            "dateTime": end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            "timeZone": timezone,
        },
        "reminders": {
            "useDefault": False,
            "overrides": [
                {"method": "email", "minutes": 24 * 60},
                {"method": "popup", "minutes": 10},
            ],
        },
    }
    service.events().insert(calendarId="primary", body=event).execute()