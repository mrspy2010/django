from django.db import models
from django.db.models.signals import pre_save, post_save
from django.utils import timezone
from django.utils.text import slugify
# Create your models here.


class Articles(models.Model):
    title = models.CharField(max_length=70)
    slug = models.SlugField(blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    publish = models.DateField(
        auto_now=False, auto_now_add=False, default=timezone.now)

    def save(self, *args, **kwargs):
        # if self.slug is None:
        #     self.slug = slugify(self.title)
        super().save(*args, **kwargs)


def slugify_instance_title(instance, save=False):
    slug = slugify(instance.title)
    instance.slug = slug

    if save:
        instance.save


def article_pre_save(sender, instance, *args, **kwargs):
    print("pre_save")

    if instance.slug is None:
        slug = slugify(instance.title)
        instance.slug = slug

    # print(sender,instance,args, kwargs)


pre_save.connect(article_pre_save, sender=Articles)


def article_post_save(sender, instance, created, *args, **kwargs):
    print("post_save")

    if created:
        slug = slugify(instance.title)
        isinstance.slug = slug
        isinstance.save()


post_save.connect(article_post_save, sender=Articles)
