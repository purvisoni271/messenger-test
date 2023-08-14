from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import re_path
from app.consumers import RoomConsumer


websocket_urlpatterns = [
    re_path(r'^ws/(?P<room_name>[^/]+)/$', RoomConsumer.as_asgi()),
]

application = ProtocolTypeRouter({
    'websocket':
        URLRouter(
            websocket_urlpatterns
        )
    ,
})
