from django.contrib import admin
from .models import AboutSection, InfoBlock, AboutPage, ContactInfo, Tournaments, GalleryImage, GallerySection

admin.site.site_header = 'Административная панель'
admin.site.site_title = 'Административная панель'
admin.site.index_title = 'Добро пожаловать в административную панель'


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)

    class Meta:
        model = AboutSection


@admin.register(InfoBlock)
class InfoBlockAdmin(admin.ModelAdmin):
    list_display = ("order", "title", "image_side")
    list_display_links = ("title",)
    list_editable = ("order", "image_side")


@admin.register(AboutPage)
class AboutPageAdmin(admin.ModelAdmin):
    list_display = ("title",)


@admin.register(Tournaments)
class TournamentsAdmin(admin.ModelAdmin):
    list_display = ("title", "text", "image")


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ("title", "email", "phone", "address")


class GalleryImageInline(admin.TabularInline):
    model = GalleryImage
    extra = 1


@admin.register(GallerySection)
class GallerySectionAdmin(admin.ModelAdmin):
    list_display = ("title", "text")
    inlines = (GalleryImageInline,)
