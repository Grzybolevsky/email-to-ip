#!/usr/bin/env python
import sys
import socket
import dns.resolver
import re

email_count = len(sys.argv)

for i in range(1, email_count):
    email = sys.argv[i]
    if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", email):
        print(email, "is not valid e-mail.")
        continue

    print(email, "is valid e-mail.")
    domain = email.rsplit('@', 1)[-1]
    for x in dns.resolver.query(domain, 'MX'):

        host_name = str(x.exchange)
        host = socket.gethostbyname(host_name)
        port = 25
        address = (host, port)
        print("\nHost:", host_name, "IP:", host)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect(address)
            msg = s.recv(1024)
            s.close()

        print("--begin of server output--\n")
        print(msg.decode('ascii'))
        print("--end of server output--\n")
