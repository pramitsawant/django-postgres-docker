from django.urls import path

from django.urls.conf import include


urlpatterns = [
    path('task/', include('api.task.urls')),
    path('post/', include('api.post.urls')),
]