from channels.routing import route
from example.consumers import ws_add, ws_message, ws_disconnect

channel_routing = [
    route("websocket.connect", ws_add ,path=r"^/chat/$"),
    route("websocket.receive", ws_message,path=r"^/chat/$"),
    route("websocket.disconnect", ws_disconnect,path=r"^/chat/$"),
    route("websocket.connect", ws_add ,path=r"^/user/$"),
    route("websocket.receive", ws_message,path=r"^/user/$"),
    route("websocket.disconnect", ws_disconnect,path=r"^/user/$"),
]