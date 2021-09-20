from django.conf.urls import url

from channels.routing import ChannelNameRouter, ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

# from gomoku.consumers import gomoku_WebSocketConsumer

# Consumer Imports
from .consumers import coreConsumer


application = ProtocolTypeRouter({

    # WebSocket handler
    "websocket": AuthMiddlewareStack(
        URLRouter([
            url(r"^ws/some_url/", coreConsumer.as_asgi()),
        ])
    ),
    "channel": ChannelNameRouter({
        "core": coreConsumer,
    })
})
