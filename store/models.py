from django.db import models
from category.models import CategoryMain, SubCategory

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

    