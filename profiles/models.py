from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
from django_countries.fields import CountryField


class ProfileCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"


class Profile(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        '''
        You know that nowdays many people think that doesn't belong to Male or Female, 
        we left them 'Other' choice just to be politically correct :) / can remove it
        '''
        ('N', 'Select'),
    )
    USER_TYPE_CHOICES = (
        ('private', 'Private Account'),
        ('creator', 'Creator Account'),
        ('brand', 'Brand Account'),
    )
    username = models.CharField(
        max_length=50)  # removed blank/null=True so we can let the user choose to use email or username when logging in
    first_name = models.CharField(
        max_length=100, blank=True, null=True, default="")
    last_name = models.CharField(
        max_length=100, blank=True, null=True, default="")
    slug = models.SlugField(unique=True, blank=True)
    user_type = models.CharField(
        max_length=20, choices=USER_TYPE_CHOICES, default='private')
    profile_image = models.ImageField(
        default='', upload_to='profiles/profile_images/', blank=True, null=True)
    cover = models.ImageField(
        default='', upload_to='profiles/profile_cover/', blank=True, null=True)
    category = models.OneToOneField(
        ProfileCategory, blank=True, null=True, on_delete=models.CASCADE)
    gender = models.CharField(
        max_length=1, choices=GENDER_CHOICES, blank=True, null=True, default='N')
    headline = models.CharField(
        max_length=50, blank=True, null=True, default="")
    about = models.TextField(
        max_length=1000, blank=True, null=True, default="")
    about_image = models.ImageField(
        default='', upload_to='profiles/about_profile_images/', blank=True, null=True)
    # removed country choices (simpler solution with country field)
    country = CountryField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}"

    def save(self, *args, **kwargs):
        if not self.slug:  # Only generate slug if it's not already set
            # Generate slug from first_name and last_name
            self.slug = slugify(f'{self.first_name}-{self.last_name}')
        super().save(*args, **kwargs)


class Brand_Account(models.Model):
    user_profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    logo = models.ImageField(
        default='', upload_to='profiles/brand_logos/', blank=True, null=True)
    headline = models.TextField(max_length=200, blank=True, null=True)
    tagline = models.TextField(max_length=200, blank=True, null=True)
    website = models.URLField(max_length=100, blank=True, null=True)
    caption = models.CharField(max_length=100, blank=True, null=True)
    about_brand = models.TextField(max_length=2000, blank=True, null=True)


class Brand_Shop_Registration(models.Model):
    REGISTER_TYPE = (
        ('select', 'select'),
        ('plc', 'Public Limited Company'),
        ('pvt', 'Private Limited Company'),
        ('opc', 'One-person Company'),
        ('llp', 'Limited Liability Partnership'),
        ('pf', 'Partnership Firm'),
        ('sp', 'Sole Proprietorship'),
    )
    legal_name = models.CharField(max_length=150)
    register_type = models.CharField(
        max_length=50, choices=REGISTER_TYPE, default='select')
    gst_no = models.CharField(max_length=100)
    company_pan_no = models.CharField(max_length=100)
