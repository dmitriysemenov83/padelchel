from django.db import models


class AboutSection(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        db_table = "about_section"
        verbose_name = "Блок «О нас»"
        verbose_name_plural = "Блок «О нас»"

    def __str__(self):
        return self.title


class InfoBlock(models.Model):
    SIDE_CHOICES = [
        ('left', 'Изображение слева'),
        ('right', 'Изображение справа'),
    ]
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    text = models.TextField(verbose_name="Текст")
    image = models.ImageField(upload_to='info_blocks/', verbose_name="Изображение")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")
    image_side = models.CharField(max_length=10, choices=SIDE_CHOICES, verbose_name="Расположение изображения")

    class Meta:
        db_table = "info_block"
        verbose_name = "Блок подробнее"
        verbose_name_plural = "Блоки подробнее"
        ordering = ['order']

    def __str__(self):
        return f'{self.title}. {self.order}'


class AboutPage(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Текст")

    class Meta:
        db_table = 'about_page'
        verbose_name = "Страница «О Федерации»"
        verbose_name_plural = "Страница «О Федерации»"

    def __str__(self):
        return self.title


class Tournaments(models.Model):
    title = models.CharField(max_length=200, verbose_name="заголовок")
    text = models.TextField(verbose_name="Текст")
    image = models.ImageField(upload_to='tournaments/', verbose_name="Изображение")

    class Meta:
        db_table = "tournaments"
        verbose_name = "Турниры"
        verbose_name_plural = "Турниры"

    def __str__(self):
        return self.title


class ContactInfo(models.Model):
    title = models.CharField (max_length=200, verbose_name="Заголовок")
    text = models.TextField (verbose_name="Текст приветствия")
    email = models.EmailField (verbose_name="Email")
    phone = models.CharField (max_length=20, verbose_name="Телефон")
    address = models.CharField (max_length=200, verbose_name="Адрес")

    class Meta:
        db_table = 'contact_info'
        verbose_name = "Контактная информация"
        verbose_name_plural = "Контактная информация"

    def __str__(self):
        return self.title


class GallerySection(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок секции")
    text = models.TextField(blank=True, verbose_name="Описание секции")

    class Meta:
        db_table = "gallery_section"
        verbose_name = "Секция галереи"
        verbose_name_plural = "Секция галереи"

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    section = models.ForeignKey(GallerySection, on_delete=models.CASCADE, related_name="images", verbose_name="Секция")
    image = models.ImageField(upload_to="gallery/", verbose_name="Изображение")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        db_table = "gallery_image"
        verbose_name = "Изображение галереи"
        verbose_name_plural = "Изображения галереи"
        ordering = ["order"]

    def __str__(self):
        return f"Изображение {self.id}"
