from django.conf.urls import url, include
from rest_framework.routers import SimpleRouter

from . import views


router = SimpleRouter()
router.register(r'^task',views.TaskView)

urlpatterns = [
    url(r'^', include(router.urls))
]