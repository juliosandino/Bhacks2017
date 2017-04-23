from __future__ import unicode_literals
from django.shortcuts import render
from django.shortcuts import redirect

from forms import zip_number
from models import District, CongressMan

def home(request):
    if request.method == 'POST':
        form = zip_number(data=request.POST)

        if form.is_valid():
            zip_c = request.POST.get('zip_code', '')

            for obj in District.objects.all():
                if obj.zip_code == int(zip_c):
                    print "found"

                    for congress_obj in CongressMan.objects.all():
                        if obj.congressional_district == congress_obj.district:

                            if (congress_obj.party == "D"):
                                party = "Democrat"
                            elif (congress_obj.party == "R"):
                                party = "Republic"
                            else:
                                party = "Independent"

                            if (congress_obj.stance == "F"):
                                stance = "Supports Action Against Climate Change"
                            else:
                                stance = "Climate Change Denier"

                            url = congress_obj.url

                            return render(request,'districts.html', {
                            'number': "You're in Congressional District " + str(obj.congressional_district),
                            'congressman': congress_obj.name,
                            'party': party,
                            'stance': stance,
                            'url': url })

    else:
        form = zip_number()

    return render(request, 'home.html', {'form': form})

def districts(request):
	return render(request, 'districts.html', {'number': ''})

def map(request):
    return render(request, 'map.html',{})

def zoomed(request):
    return render(request, 'zoomed.html', {'number': ''}) 

def about(request):
	return render(request, 'about.html', {})

def contact(request):
	return render(request, 'contact.html', {})