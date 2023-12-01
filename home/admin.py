from django.contrib import admin
from .models import Category, Tags, News, Contact

class NewAdmin(admin.ModelAdmin):
    list_display =['id', 'title', 'user','view_count' ]
    readonly_fields= ['view_count']
    prepopulated_fields = { "slug": ('title',), }
    
    
admin.site.register(News, NewAdmin)
admin.site.register(Category)
admin.site.register(Tags)
# admin.site.register(Contact)
admin.site.register(Contact)
# class ContactAdmin(admin.ModelAdmin):
#     list_display =['id','firstname','email'  ]

# Register your models here.
