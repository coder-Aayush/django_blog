from django.contrib import admin
from .models import Blog, Contact,NewsSubscriber
# Register your models here.


admin.site.site_header = 'Programming World'




class EntryAdmin(admin.ModelAdmin):
    list_display = ("title","date")
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blog,EntryAdmin)
admin.site.register(Contact)
admin.site.register(NewsSubscriber)

