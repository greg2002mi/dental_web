from django.shortcuts import render

# Main Navigation.
def index(request):
    return render (request, "index.html", context={})

def clinic(request):
    return render (request, "clinic.html", context={})

def dentists(request):
    return render (request, "dentists.html", context={})

def team(request):
    return render (request, "team.html", context={})

def testimonials(request):
    return render (request, "testimonials.html", context={})

def services(request):
    return render (request, "services.html", context={})

def service_details(request):
    return render (request, "service_details.html", context={})

def gallery(request):
    return render (request, "gallery.html", context={})

def blog(request):
    return render (request, "blog.html", context={})

def blog_details(request):
    return render (request, "blog_details.html", context={})

def contact_us(request):
    return render (request, "contact_us.html", context={})


# general functions 
def appointment(request):
    return render (request, "appointment.html", context={})

def directions(request):
    return render (request, "directions.html", context={})




# add or delete information for only administration





