# Intro 🚪

HTTP proxies have a lot of use cases, from caching, authentication and preventing users from accessing malicious websites. They’re widely used in the world wide web and in business settings. Businesses use proxies to prevent their employees from surfing malicious websites, and enforce authentication and logging. Websites use proxies to provide caching and load balancing that shrinks websites load time.
* Before you start, an introduction to HTTP
Read this section from the original project spec. but try those steps on your computer
```code 
telnet info.cern.ch 80
``` 
Now, this will open a TCP connection to this website on port 80. You should see something like
``` code 
Trying 188.184.64.53...
Connected to info.cern.ch.
Escape character is '^]'. 
```
Now you're connected to this website, to make a GET request type in (note: the host header is required to get a correct answer)
```code
GET /hypertext/WWW/TheProject.html HTTP/1.1
Host: info.cern.ch
```
# Starting up
After starting the proxy, it will wait for an incoming request using TCP connections. Upon receiving a HTTP request. The proxy parses the request and verifies that it’s valid. An  invalid request would return a bad request with status code 400 to the client. 

# Logic Flow
* Your proxy server is expected to do the following (assuming you’re single threaded)
Open a listening TCP socket, and binds it to the port specified by the first command line argument
* Use TCP for communication with both clients and servers.
* Open a TCP connection for every HTTP request to be proxied. 
* After the client’s HTTP request is parsed. Open a TCP connection with the asked website, * making the request and return the response back to the client if successful.
* Close the TCP connection with both client and requested website’s server. (because HTTP 1.0 doesn’t have persistent connections)
Testing Your Code 🤔
# Wireshark
Wireshark is the simplest method to make sure you're at least emitting HTTP packets, the packet type will appear as HTTP if your packets are correctly formatted. This is the first good sign you're on the right track.
#Testing your proxy 
Open a terminal, then run your proxy (assuming that you’re using Python), your proxy will run on 127.0.0.1 as always.
``` code 
~ python proxy.py 2233
```
Now, leave your proxy running then issue the telnet command (we’re telnetting to the proxy now -not a website-)
``` code 
~ telnet 127.0.0.1 2233
Trying 127.0.0.1...
Connected to localhost.localdomain (127.0.0.1).
Escape character is '^]'.
GET http://info.cern.ch:80/ HTTP/1.0
# hit enter twice
```
# Using Telnet to verify your output
A good sanity check of proxy behavior would be to compare the HTTP response (headers and body) obtained via your proxy by calling telnet to your proxy, then making an HTTP request from the command line with the response from a direct telnet connection to the re
mote server. Check that by capturing the HTTP GET packet and compare the result.
``` code 
~ telnet info.cern.ch 80
Trying 188.184.64.53...
Connected to info.cern.ch.
Escape character is '^]'.
GET /hypertext/WWW/TheProject.html HTTP/1.0
Host: info.cern.ch # hit enter twice
```
