from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.

class Categories(models.Model):
    cat_name = models.CharField(max_length=120)
    description = models.CharField(max_length=400)
    slug = models.SlugField(max_length=120, unique=True, default='page-slug', blank=True)

    class Meta:
        ordering = ["-cat_name"]

    def __str__(self):
        return self.cat_name

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'slug': self.slug})

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if instance.slug == 'page-slug' or instance.slug == "":
        slug = slugify(instance.cat_name)
        exits = Categories.objects.filter(slug=slug).exists()
        if exits:
            slug = "%s-%s" % (slug, instance.id)
        instance.slug = slug


pre_save.connect(pre_save_post_receiver, sender=Categories)


class Language1(models.Model):
    language = models.CharField(max_length=20)
    slug = models.SlugField(max_length=20, unique=True, default='page-slug', blank=True)

    class Meta:
        ordering = ["-language"]

    def __str__(self):
        return self.language

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'slug': self.slug})

def pre_save_post_receiver1(sender, instance, *args, **kwargs):
    if instance.slug == 'page-slug' or instance.slug == "":
        slug = slugify(instance.language)
        exits = Language1.objects.filter(slug=slug).exists()
        if exits:
            slug = "%s-%s" % (slug, instance.id)
        instance.slug = slug


pre_save.connect(pre_save_post_receiver1, sender=Language1)



class Subcategories(models.Model):
    cat_name = models.CharField(max_length=120)
    slug = models.SlugField(max_length=120, unique=True, default='page-slug', blank=True)

    class Meta:
        ordering = ["-cat_name"]

    def __str__(self):
        return self.cat_name

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'slug': self.slug})


def pre_save_post_receiver2(sender, instance, *args, **kwargs):
    if instance.slug == 'page-slug' or instance.slug == "":
        slug = slugify(instance.cat_name)
        exits = Subcategories.objects.filter(slug=slug).exists()
        if exits:
            slug = "%s-%s" % (slug, instance.id)
        instance.slug = slug


pre_save.connect(pre_save_post_receiver2, sender=Subcategories)


class Blog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    language2 = models.ForeignKey(Language1)
    title = models.CharField(max_length=163)
    image = models.FileField(blank=True)
    categories = models.ForeignKey(Categories)
    sub_cat = models.ForeignKey(Subcategories)
    description = RichTextUploadingField()
    datetime = models.DateField('date_published', auto_now_add=True)
    sort_desc = models.CharField(max_length=160)
    keywords = models.CharField(max_length=4000)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    share = models.IntegerField(default=0)
    slug = models.SlugField(max_length=168, unique=True, default='page-slug', blank=True)

    class Meta:
        ordering = ["-datetime"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog-detail', kwargs={'slug': self.slug})


def pre_save_post_receiver3(sender, instance, *args, **kwargs):
    if instance.slug == 'page-slug' or instance.slug == "":
        slug = slugify(instance.title)
        exits = Blog.objects.filter(slug=slug).exists()
        if exits:
            slug = "%s-%s" % (slug, instance.id)
        instance.slug = slug


pre_save.connect(pre_save_post_receiver3, sender=Blog)


class ContactForm1(models.Model):
    name = models.CharField(max_length=25)
    email1 = models.EmailField(blank=True)
    subject = models.CharField(max_length=250)
    desc = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('contact1', kwargs={'id': self.id})


class Advertisement1(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ads_title = models.CharField(max_length=25)
    cat_g = models.ForeignKey(Categories)
    ads = models.ImageField(blank=True)
    ads_url = models.CharField(max_length=200)
    clicks = models.IntegerField(default=0)
    slug = models.SlugField(max_length=25, unique=True, default='page-slug', blank=True)

    def __str__(self):
        return self.ads_title

    def get_absolute_url(self):
        return reverse('advertise', kwargs={'slug': self.slug})


def pre_save_post_receiver4(sender, instance, *args, **kwargs):
    if instance.slug == 'page-slug' or instance.slug == "":
        slug = slugify(instance.ads_title)
        exits = Advertisement1.objects.filter(slug=slug).exists()
        if exits:
            slug = "%s-%s" % (slug, instance.id)
        instance.slug = slug


pre_save.connect(pre_save_post_receiver4, sender=Advertisement1)


class Newsletter(models.Model):
    Email = models.EmailField(unique=True)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.Email
