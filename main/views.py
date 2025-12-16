from django.shortcuts import render
from .models import AboutSection, InfoBlock, AboutPage, ContactInfo, Tournaments
from django.views.decorators.cache import cache_page


@cache_page(60 * 15)
def home(request):
    about_section = AboutSection.objects.first()
    contact = ContactInfo.objects.first()
    return render(request, 'main/home.html',
        {
            'about_section': about_section,
            'contact': contact
        }
    )


@cache_page(60 * 5)
def tournaments(request):
    tournaments = Tournaments.objects.all().order_by('-id')
    contact = ContactInfo.objects.first()
    return render(request, 'main/tournaments.html',
        {
            'contact': contact,
            'tournaments': tournaments
        }
    )


@cache_page(60 * 60 * 6)
def more(request):
    blocks = InfoBlock.objects.first()
    contact = ContactInfo.objects.first()
    return render(request, 'main/more.html',
        {
            'blocks': blocks,
            'contact': contact
        }
    )


@cache_page(60 * 60 * 6)
def about(request):
    about_page = AboutPage.objects.first()
    contact = ContactInfo.objects.first()
    return render(request, 'main/about.html',
        {
            'about_page': about_page,
            'contact': contact
        }
    )


@cache_page(60 * 60 * 24)
def contacts(request):
    contact = ContactInfo.objects.first()
    return render(request, 'main/contacts.html',
        {
            'contact': contact
         }
    )
