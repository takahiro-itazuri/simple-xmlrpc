import xmlrpc.client

# create client and set up server
client = xmlrpc.client.ServerProxy('http://127.0.0.1:8080')

# list methods
print(client.system.listMethods())

# show help for method
print(client.system.methodHelp('hello'))

# call method
print(client.hello())

