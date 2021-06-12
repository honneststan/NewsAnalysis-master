from django.shortcuts import render, redirect
from .forms import UpdateProfileForm
from .models import Reader


def update_profile(request):
    required_user = request.user
    required_reader = Reader.objects.get(user=required_user)
    if request.method == "POST":
        form = UpdateProfileForm(instance=required_reader, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('reader:view-reader')
    else:
        form = UpdateProfileForm(instance=required_reader)
    context = {
        'form': form
    }
    return render(request, "reader/update.html", context)


def view_profile(request):
    required_user = request.user
    required_reader = Reader.objects.get(user=required_user)
    context = {
        'reader': required_reader
    }
    return render(request, "reader/view.html", context)