# RFC-868-Time-Protocol
Server and Client classes implementing RFC 868 in python

# Usage server

  >>> from rfc_868 import Server
  >>>
  >>> server = Server
  >>> Listening on port 37
  
  Remote host 127.0.0.1 connected, Response: 1011010100001011001001101011111
  Remote host 127.0.0.1 disconnected.

# Usage client

  >>> from rfc_868 import Client
  >>> Client(time_server=("192.168.1.0", 37))
  >>> Received time: 1011010100001011001010100101111
