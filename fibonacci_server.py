import socket
import pickle

import logging as log
log.basicConfig(format='[%(asctime)s] %(message)s',
                datefmt='%I:%M:%S %p',
                level=log.INFO)

AS_HOST = "localhost"
AS_PORT = 53533
AS_ADDR = (AS_HOST, AS_PORT)

BUFFER_SIZE = 1024

SERVER_UDP_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def send_mssg_to_server(msg):
    msg_bytes = pickle.dumps(msg)
    SERVER_UDP_SOCKET.sendto(msg_bytes, AS_ADDR)


def register(name, value, type, ttl):
    send_mssg_to_server((name, value, type, ttl))


def main():
    # dns_record = ("Hello from UDP Client", 123, )
    dns_record = ("A",
                  "fibonacci.com",
                  "localhost",
                  5)
    register(*dns_record)
    response = ""
    # while not response:
    for i in range(8):
        import time
        time.sleep(1)
        send_mssg_to_server(("A", "fibonacci.com"))
        response, _ = SERVER_UDP_SOCKET.recvfrom(BUFFER_SIZE)
        response = pickle.loads(response)
        log.info("Message from Server {}\n".format(response))

    send_mssg_to_server(("A", "fibonacci2.com"))


if __name__ == '__main__':
    main()
