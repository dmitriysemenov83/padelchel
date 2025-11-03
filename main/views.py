from django.shortcuts import render
from .models import AboutSection, InfoBlock, AboutPage, ContactInfo, Tournaments


def home(request):
    about_section = AboutSection.objects.first()
    contact = ContactInfo.objects.first()
    return render(request, 'main/home.html',
        {
            'about_section': about_section,
            'contact': contact
        }
    )

def tournaments(request):
    tournaments = Tournaments.objects.all().order_by('-id')
    contact = ContactInfo.objects.first()
    return render(request, 'main/tournaments.html',
        {
            'contact': contact,
            'tournaments': tournaments
        }
    )


def more(request):
    blocks = InfoBlock.objects.first()
    contact = ContactInfo.objects.first()
    return render(request, 'main/more.html',
        {
            'blocks': blocks,
            'contact': contact
        }
    )


def about(request):
    about_page = AboutPage.objects.first()
    contact = ContactInfo.objects.first()
    return render(request, 'main/about.html',
        {
            'about_page': about_page,
            'contact': contact
        }
    )


def contacts(request):
    contact = ContactInfo.objects.first()
    return render(request, 'main/contacts.html',
        {
            'contact': contact
         }
    )
