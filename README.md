# Utilities for socket communication

Some examples of code in C and Python for socket communication

-----------------

### C examples

To compile the C examples type 

    $ make
    
on the command line.
Then run first the `server` on a terminal on some port number (5000 in the example below)

    $ ./server 5000
    
And run the `client` with domain and port on another terminal:

    $ ./client localhost 5000
    
-----------------------

### Python examples

To run the python server/client socket examples, run the server and client on different terminals

    $ python server.py
    
and

    $ python client.py
    
----------------------

To run the XML RPC run server and client on different terminals:

    $ python xmlserver.py

and

    $ python xmlclient.py
    
