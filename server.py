import xmlrpc.server

def hello():
    ''' hello method
    This method says hello.
    '''
    return 'Hello XML-RPC!'

# create server
server = xmlrpc.server.SimpleXMLRPCServer(('127.0.0.1', 8080))

# register function
server.register_function(hello)

# ready to help message
server.register_introspection_functions()

# listen
server.serve_forever()

