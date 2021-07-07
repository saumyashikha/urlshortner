from django.shortcuts import render, HttpResponseRedirect
from .forms import UrlForm
from .models import UrlShort
import pyshorteners

# Create your views here.
def home(request):
    if request.method == 'POST':
        fm = UrlForm(request.POST)
        if fm.is_valid():
            original = fm.cleaned_data['original_url']
            short = pyshorteners.Shortener().tinyurl.short(original)
            s = UrlShort(original_url=original, short_url=short)
            s.save()
            return render(request, 'home.html', {'form':fm, 'shorten': short})
    else:
        fm = UrlForm()
        return render(request, 'home.html', {'form':fm})

      