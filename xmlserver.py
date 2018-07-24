from xmlrpc.server import SimpleXMLRPCServer
import datetime
import xmlrpc.client

 
def is_even(n):
     return n % 2 == 0

def today():
    today = datetime.datetime.today()
    return xmlrpc.client.DateTime(today)

server = SimpleXMLRPCServer(("localhost", 8000))
print("Listening on port 8000...")
server.register_function(is_even, "is_even")
server.register_function(today, "today")
server.serve_forever()
