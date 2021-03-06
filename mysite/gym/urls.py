from django.urls import path
from . import views
from django.http import StreamingHttpResponse
from .camera import VideoCamera, gen
from customer.views import OrderConfirmation


urlpatterns = [
    path('', views.shalom, name="shalom"),
    path('monitor/', lambda r: StreamingHttpResponse(gen(VideoCamera()),
        content_type='multipart/x-mixed-replace; boundary=frame')),

    
]


