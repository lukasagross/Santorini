"""
Module to simplify reading and writing JSON with sockets
"""

import json
import socket


def write_json(sock, data):
    """
    Writes JSON object to socket. Blocks until data is written.
    :param sock: socket to write to
    :param data: JSON object to write
    :return: None
    """
    msg = json.dumps(data)
    sock.sendall(bytes(msg, encoding='utf8'))


def read_json(sock):
    """
    Reads a JSON object from socket. Blocks while data is read from the socket.
    :param sock: socket to read from
    :return: JSON object
    :raise: JSONDecodeError if read data is not valid JSON
    """
    data = b''
    buf = sock.recv(4096)
    data += buf

    try:
        return json.loads(data.decode('utf-8'))
    except json.JSONDecodeError:
        # If the buffer does not hold a valid JSON object,
        # keep reading until the socket times out
        sock.settimeout(0.5)
        while buf:
            try:
                data += buf
                buf = sock.recv(4096)
            except socket.timeout:
                break
        sock.settimeout(None)
        return json.loads(data.decode('utf-8'))
