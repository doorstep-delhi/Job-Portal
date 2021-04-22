from django.shortcuts import render, HttpResponse
from .models import Job, Position
from .forms import JobForm


def home(request):
    form = JobForm()
    positions = Position.objects.all()
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("Form Saved Successfully")
    print(positions)
    context = {
        "form":form,
        "positions": positions,
    }
    return render(request, 'main_app/index.html', context)
