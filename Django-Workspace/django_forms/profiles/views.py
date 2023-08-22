from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from profiles.form import ProfileForm
from .models import UserProfile

# Create your views here.


def store_files(file):
    with open('temp/image.jpg', 'wb+') as dest:
        for chunk in file.chunks():
            dest.write(chunk)


class CreateProfileView(View):

    def get(self, request):
        form = ProfileForm()
        return render(request, "profiles/create_profile.html", {"form": form})

    def post(self, request):
        submitted_form = ProfileForm(request.POST, request.FILES)
        if submitted_form.is_valid():
            profile = UserProfile(image=request.FILES["user_image"])
            profile.save()
            # store_files(request.FILES['image'])
            return HttpResponseRedirect('/profiles')

class ProfilesView(ListView):
    model = UserProfile
    template_name = 'profiles/user_profiles.html'
    context_object_name="profiles"