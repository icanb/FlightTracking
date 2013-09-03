

from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render, render_to_response
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from webapp.emailer import send_email, send_template_email
from webapp.forms import Create_Flight, Create_House, Edit_Flight, LoginForm, ShortSignupForm
from webapp.models import Flight, House, User
from webapp.utils import JsonResponse


@require_POST
def login(request):
    """
    Handles the login action.
    """
    form = LoginForm(None, data=request.POST)
    if form.is_valid():
        auth_login(request, form.get_user())
        return JsonResponse(data={'redirect_to': reverse('webapp.pages.my_flights')})

    return JsonResponse(errors=form.errors)


@require_POST
def create_flight(request):
    form = Create_Flight(request.POST)
    if form.is_valid():
        flight = form.save(commit=False)

        # set foreign keys
        flight.flyer = request.user

        flight.save()  # persist the object to the DB

        redirect_url = reverse('webapp.pages.my_flights')
        return JsonResponse(data={'redirect_to': redirect_url})

    return JsonResponse(errors=form.errors)


@require_POST
def edit_flight(request, flight_id):
    flight2 = get_object_or_404(Flight, pk=flight_id)
    form = Edit_Flight(request.POST, instance=flight2)
    if form.is_valid():
        flight = form.save()

        redirect_url = reverse('webapp.pages.homepage')
        return JsonResponse(data={'redirect_to': redirect_url})

    return JsonResponse(errors=form.errors)


@require_POST
def create_house(request):
    form = Create_House(request.POST)
    if form.is_valid():
        house = form.save()

        redirect_url = reverse('webapp.pages.houses')
        return JsonResponse(data={'redirect_to': redirect_url})

    return JsonResponse(errors=form.errors)


@require_POST
def sign_up(request):
    """Create a User object"""
    form = ShortSignupForm(request.POST)
    if form.is_valid():
        user = form.save()
        user = authenticate(username=request.POST['email'],
                            password=request.POST['password'])
        auth_login(request, user)

        redirect_url = reverse('webapp.pages.homepage')
        return JsonResponse(data={'redirect_to': redirect_url})

    return JsonResponse(errors=form.errors)
