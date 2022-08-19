from .models import CategoryMain, SubCategory

def menu_links(request):
    cat_main_links = CategoryMain.objects.all()
    cat_sub_links = SubCategory.objects.all()

    return dict(cat_main_links=cat_main_links, cat_sub_links=cat_sub_links)