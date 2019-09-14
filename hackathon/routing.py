from channels.routing import ProtocolTypeRouter
from channels.routing import route
from chat_bot.conversations import ws_connect, ws_disconnect, ws_message

application = ProtocolTypeRouter({})

channel_routing = [
    route('websocket.connect', ws_connect),
    route('websocket.disconnect', ws_disconnect),
    route("websocket.receive", ws_message),
]