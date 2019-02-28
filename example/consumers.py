from channels import Group

# Connected to websocket.connect
def ws_add(message):
    # Accept the connection
    message.reply_channel.send({"accept": True})
    # Add to the chat group
    Group("chat/check/").add(message.reply_channel)

# Connected to websocket.receive
def ws_message(message):
    Group("chat/check/").send({
        "text": "[user] %s" % message.content['text'],
    })

# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("chat/check/").discard(message.reply_channel)




def ws_add(message):
    # Accept the connection
    message.reply_channel.send({"accept": True})
    # Add to the chat group
    Group("user").add(message.reply_channel)

# Connected to websocket.receive
def ws_message(message):
    Group("user").send({
        "text": "[user] %s" % message.content['text'],
    })

# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("user").discard(message.reply_channel)