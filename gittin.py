# Test file for practicing git and git-hub in VS Code.

import socket
import os
import pprint as pprint

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print(f'\nHostname is {hostname}')
print(f'\nIP address is {ip_address}')

path = os.environ.get("PATH")
print(f'\nPath is: {path}')

def addition(*args):
    total = sum(args)
    
    print(f'\nSum of {args} is: {total}')
    
addition(3, 5, 80)