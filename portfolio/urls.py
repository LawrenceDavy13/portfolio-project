
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views, todolist.views, mathsgame.views, mathswebsite.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('wordcounter/', include('wordcounter.urls')),
    path('piglatintranslator/', include('piglatintranslator.urls')),
    path('mathsgame/', mathsgame.views.mathsgame, name='mathsgame'),
    path('todolist/', todolist.views.todolist, name='todolist'),
    path('mathswebsite/', mathswebsite.views.mathswebsite, name='mathswebsite')


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
