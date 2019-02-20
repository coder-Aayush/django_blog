from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from blog import views
from django.conf.urls import handler404,handler500
import blog



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('news/',views.news,name='news'),
    path('support/',views.support,name='support'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('blog/', include('blog.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

handler404 = 'blog.views.handler404'
handler500 = 'blog.views.handler500'
