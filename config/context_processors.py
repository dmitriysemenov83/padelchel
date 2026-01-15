from django.conf import settings

def region_context(request):
    """Добавляет региональные данные во все шаблоны"""
    return {
        'REGION': settings.REGION,
        'SITE_NAME': settings.CURRENT_REGION['site_name'],
        'AREA': settings.CURRENT_REGION['area'],
        'TELEGRAM': settings.CURRENT_REGION['telegram'],
        'VK': settings.CURRENT_REGION['vk'],
        'INSTAGRAM': settings.CURRENT_REGION['instagram'],
    }
