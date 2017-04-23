from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import redirect

from forms import zip_number
from models import District

def home(request):
    if request.method == 'POST':
        form = zip_number(data=request.POST)

        if form.is_valid():
            zip_c = request.POST.get('zip_code', '')

            for obj in District.objects.all():
                if obj.zip_code == int(zip_c):
                    print "found"
                    return render(request,'districts.html', {
                        'number':"You're in Congressional District " + str(obj.congressional_district) })

    else:
        form = zip_number()

    return render(request, 'home.html', {'form': form})

def districts(request):
	return render(request, 'districts.html', {'number': ''})

def districts-zoomed(request):
    return render(request, 'districts-zoomed.html', {'number': ''}) 

def about(request):
	return render(request, 'about.html', {})

def contact(request):
	return render(request, 'contact.html', {})