import socket as s

while True:
    print("Type your url here")
    host = input()
    print("")
    print(f'the IP from {host} is {s.gethostbyname(host)}')
    print("")