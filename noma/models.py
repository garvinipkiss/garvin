from django.db import models

# Create your models here.

# Location model to enable us choose location


class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_catgory(self):
        self.save()


# renaming class Images to Photos due to error in terminal;


class Image(models.Model):
    image_name = models.CharField(max_length=20)
    image_description = models.CharField(max_length=30)
    location = models.ForeignKey(Location)
    category = models.ForeignKey(Category)
    image = models.ImageField(upload_to='gallery/', null="True", blank="True")

    # __str__ will return string representation of the image model
    # __str__ will enable us view our returned queries

    def __str__(self):
        return self.image_name

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def search_by_category(cls, search_term):
        display = cls.objects.filter(category__name__icontains=search_term)
        return display

    # @classmethod
    # def location(cls):
    #     display = cls.objects.filter(location__name__icontains=cls)
    #     return display

    class Meta:
        ordering = ['image_name']
