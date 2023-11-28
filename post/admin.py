from django.contrib import admin

from post.models import Product, Category, Review


@admin.register(Product)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'create_at']
    list_editable = ['price']
    list_filter = ['create_at']
    list_per_page = 10
    search_fields = ['title', 'content']

    def has_add_permission(self, request):
        return True


admin.site.register(Category)
admin.site.register(Review)
