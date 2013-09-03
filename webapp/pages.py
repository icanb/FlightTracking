

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, render_to_response
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from webapp.models import Flight, House, User
from webapp.utils import get_results


@require_GET
def homepage(request):
    page_context = {}

    return render(request, "homepage.html", page_context)


@login_required
@require_GET
def my_flights(request):
    page_context = {}

    page_context['flights'] = Flight.objects.all().order_by('-date_created')

    return render(request, "my_flights.html", page_context)


@login_required
@require_GET
def edit_flight(request, flight_id):
    page_context = {}
    page_context['flight'] = get_object_or_404(Flight, pk=flight_id)

    return render(request, "edit_flight.html", page_context)


@require_GET
def all_flights(request):
    page_context = {}

    page_context['flights'] = Flight.objects.all().order_by('-date_created')

    return render(request, "all_flights.html", page_context)


@require_GET
def houses(request):
    page_context = {}

    page_context['houses'] = House.objects.all().order_by('-date_created')

    return render(request, "houses.html", page_context)


@require_GET
def house_page(request, house_id):
    page_context = {}
    page_context['house'] = get_object_or_404(House, pk=house_id)

    return render(request, "house_page.html", page_context)


@require_GET
def sdf_page(request):
    page_context = {}

    return render(request, "sdf_page.html", page_context)


@require_GET
def signup_page(request):
    page_context = {}

    return render(request, "signup_page.html", page_context)


@require_GET
def about_us(request):
    page_context = {}

    return render(request, "about_us.html", page_context)


@require_GET
def people(request):
    page_context = {}

    search_user(request, page_context)

    return render(request, "people.html", page_context)


@require_GET
def profile_page(request, user_id):
    page_context = {}
    page_context['user'] = get_object_or_404(User, pk=user_id)

    page_context['flights'] = Flight.objects.all().filter(
        flyer=page_context['user'].id).order_by('-date_created')

    return render(request, "profile_page.html", page_context)


def search_user(request, page_context):
    if 'query' not in request.GET:
        return
    query_string = request.GET['query']
    import HTMLParser
    h = HTMLParser.HTMLParser()
    unescaped_field_json = h.unescape(request.GET['field_json'])
    try:
        field_names = simplejson.loads(unescaped_field_json)
    except Exception:
        field_names = []
    page_context['results'] = get_results(query_string, "User", field_names)


def search_user2(request, page_context):
    if 'query' not in request.GET:
        return
    query_string = request.GET['query']
    import HTMLParser
    h = HTMLParser.HTMLParser()
    unescaped_field_json = h.unescape(request.GET['field_json'])
    try:
        field_names = simplejson.loads(unescaped_field_json)
    except Exception:
        field_names = []
    page_context['results2'] = get_results(query_string, "User", field_names)
