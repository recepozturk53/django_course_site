from django.shortcuts import render, redirect

from .models import Meetup, Participant
from .forms import RegistrationForm

# Create your views here.

def index(request):
    meetups = Meetup.objects.all()
    return render(request, 'meetups/index.html', {
        'meetups': meetups
    })


def meetup_details(request, meetup_slug):
    try:
        selected_meetup = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET':
            registration_form = RegistrationForm()
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                user_email = registration_form.cleaned_data['email']
                participant, _ = Participant.objects.get_or_create(email=user_email)
                selected_meetup.participants.add(participant)
                return redirect('confirm-registration', meetup_slug=meetup_slug)

        return render(request, 'meetups/meetup-details.html', {
                'meetup_found': True,
                'meetup': selected_meetup,
                'form': registration_form
            })
    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False
        })


def confirm_registration(request, meetup_slug):
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registration-success.html', {
        'organizer_email': meetup.organizer_email
    })


# def meetup_details(request, meetup_slug):
#     """
#     Renders the details page for a specific meetup.

#     If the meetup is not found, renders a page with a message indicating that the meetup was not found.

#     :param request: The HTTP request object.
#     :param meetup_slug: The slug of the meetup to display.
#     :return: The rendered HTML template.
#     """
#     # Retrieve the Meetup object from the database using the provided slug
#     # If the Meetup object is not found, render a page with a message indicating that the meetup was not found
#     return render(request, 'meetups/meetup-details.html', {
#         'meetup_found': False
#     })


# def confirm_registration(request, meetup_slug):
#     """
#     Renders the registration success page for a specific meetup.

#     :param request: The HTTP request object.
#     :param meetup_slug: The slug of the meetup for which the registration was successful.
#     :return: The rendered HTML template.
#     """
#     # Retrieve the Meetup object from the database using the provided slug
#     # Set the organizer_email context variable to the email address of the meetup's organizer
#     return render(request, 'meetups/registration-success.html', {
#         'organizer_email': meetup.organizer_email
#     })