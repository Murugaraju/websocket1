# POC code on Websocket

1. Need redis server running i.e redis-server
2. Installation on ubuntu cmd sudo apt-get install redis-server
3. check the redis server status by the cmd redis-cli ping, it responds with PONG
4. landing html page url /test/ 
5. ws url to handshake to the status on model changes i.e. ws://localhost:8000/status/ 
6. Use https://websoket.org/echo.html to chek the socket connection 
7. Use daphne -b 127.0.0.1 -p 8000 websockett.asgi:application or normal django's runserver 


