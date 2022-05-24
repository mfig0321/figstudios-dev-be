
"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import include
from django.contrib import admin
from django.urls import path

from chatbot import views as chatbot_views
from health import views as health_views
from user import views as user_views


# Setup the URLs and include login URLs for the browsable API.
urlpatterns = [
    path('admin/', admin.site.urls),

    # Applications Urls
    path('', health_views.HealthCheckEndpoint.as_view(), name='health'),
    path('chatbot/', chatbot_views.ChatterBotApiView.as_view()),
    path('health/', health_views.HealthCheckEndpoint.as_view(), name='health'),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    path('users/', user_views.UserList.as_view()),
    path('users/<pk>/', user_views.UserDetails.as_view()),
    path('groups/', user_views.GroupList.as_view()),
    path('train/', chatbot_views.ChatterBotTrain.as_view()),
]
