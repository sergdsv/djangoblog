from django.conf.urls import url
from .controllers import (
    AuthController,
)

urlpatterns = [
    url(r"^login/$", AuthController.login_user, name="login"),
    url(r"^logout/$", AuthController.logout_view, name="logout"),
    # url(r'^logout/$', 'django.contrib.auth.views.auth_logout', name='logout'),
]

