from channels import Group

# Connected to websocket.connect
def ws_add(message):
    # Accept the connection
    message.reply_channel.send({"accept": True})
    # Add to the chat group
    Group("chat").add(message.reply_channel)
    print("I am printing from chat url")

# Connected to websocket.receive
def ws_message(message):
    Group("chat").send({
        "text": "[user] %s" % message.content['text'],
    })

# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)




def ws1_add(message):
    # Accept the connection
    message.reply_channel.send({"accept": True})
    # Add to the chat group
    print("I am printing because user url")
    Group("user").add(message.reply_channel)

# Connected to websocket.receive
def ws1_message(message):
    Group("user").send({
        "text": "[user] %s" % message.content['text'],
    })

# Connected to websocket.disconnect
def ws1_disconnect(message):
    Group("user").discard(message.reply_channel)