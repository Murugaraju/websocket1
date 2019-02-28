from channels.routing import route
from example.consumers import *

channel_routing = [
    route("websocket.connect", ws_add ,path=r"^/chat/$"),
    route("websocket.receive", ws_message,path=r"^/chat/$"),
    route("websocket.disconnect", ws_disconnect,path=r"^/chat/$"),
    route("websocket.connect", ws1_add ,path=r"^/user/$"),
    route("websocket.receive", ws1_message,path=r"^/user/$"),
    route("websocket.disconnect", ws1_disconnect,path=r"^/user/$"),
]