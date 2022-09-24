from django.db import models
from category.models import CategoryMain, SubCategory
from accounts.models import Account

# Create your models here.
class Product(models.Model):
    product_name  = models.CharField(max_length=50, unique=True)
    slug          = models.SlugField(max_length=100, unique=True)
    Category_Main = models.ForeignKey('category.CategoryMain', on_delete=models.CASCADE)
    sub_category  = models.ForeignKey('category.SubCategory', on_delete=models.CASCADE)
    mrp_price     = models.DecimalField(max_digits=10, decimal_places=2)
    price         = models.DecimalField(max_digits=10, decimal_places=2)
    short_desp    = models.CharField(max_length=150)
    description   = models.TextField(blank=True)
    images        = models.ImageField(upload_to='Product/product_img', blank=True)
    stock         = models.IntegerField(default=0)
    is_available  = models.BooleanField(default=True)
    
    created_date  = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product_name
    
    def get_url(self):
            return reverse('product_detail', args=[self.slug])

class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(Variation_category='Color', is_active=True)

    def sizes(self):
        return super(VariationManager, self).filter(Variation_category='Size', is_active=True)


# vartion realted codes here start
variation_category_choice=(
    ('Size', 'Size'),
    ('Color', 'Color'),
)


class Variation(models.Model):
    Product            = models.ForeignKey(Product, on_delete=models.CASCADE)
    Variation_category = models.CharField(max_length=100, choices=variation_category_choice)
    Variation_value    = models.CharField(max_length=100)
    is_active          = models.BooleanField(default=True)
    created_date       = models.DateTimeField(auto_now_add=True)

    objects            = VariationManager()

    def __str__(self):
        return self.Variation_value


class ReviewRating(models.Model):
    product     = models.ForeignKey(Product, on_delete=models.CASCADE)
    user        = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject     = models.CharField(max_length=100, blank=True)
    review      = models.TextField(max_length=250, blank=True)
    rating      = models.FloatField(default=0)
    ip          = models.CharField(max_length=20, blank=True)
    status      = models.BooleanField(default=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject 
    

    