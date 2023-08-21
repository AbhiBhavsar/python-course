from django.http import HttpResponseRedirect
from django.shortcuts import render
from .form import ReviewForm

# Create your views here.


def review(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        # print(form.cleaned_data)
        if form.is_valid():
            return HttpResponseRedirect('/thank-you')
    else:
        form = ReviewForm()
    return render(request, 'reviews/review.html', {"form": form})


def thank_you(request):
    return render(request, 'reviews/thank-you.html')
