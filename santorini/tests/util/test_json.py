import pytest
import socket
from json import JSONDecodeError

from santorini.util._json import read_json, write_json

host = "localhost"
port = 8888


@pytest.fixture
def connections():
    global port
    while True:
        try:
            admin = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            admin.bind((host, port))
            admin.listen()

            client_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_conn.connect((host, port))

            server_conn = admin.accept()[0]

            yield client_conn, server_conn

            client_conn.close()
            server_conn.close()
            admin.close()
            break

        except OSError:
            port += 1


def test_one_valid(connections):
    client_conn, server_conn = connections

    server_json = {"test": [1, 2, 3, "foo"], "test2": True}
    client_json = [False, 0.5, {"bar": -2}]

    write_json(server_conn, server_json)
    write_json(client_conn, client_json)

    assert read_json(client_conn) == server_json
    assert read_json(server_conn) == client_json


def test_many_valid(connections):
    client_conn, server_conn = connections

    server_msgs = [{"command": "register"},
                   {"command": "place",
                    "board": [[0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0]]},
                   {"command": "play",
                    "board": [[0, 0, 0, 0, 0],
                              [0, ["white1", 0], ["blue1", 0], 0, 0],
                              [0, ["white2", 0], ["blue2", 0], 0, 0],
                              [0, 0, 0, 0, 0],
                              [0, 0, 0, 0, 0]]},
                   {"command": "gameover",
                    "winner": "player-one"}]

    client_msgs = ["player-one",
                   [[1, 1], [1, 2]],
                   ["white1", ["N", "S"]],
                   "OK"]

    for server_json, client_json in zip(server_msgs, client_msgs):
        write_json(server_conn, server_json)
        assert read_json(client_conn) == server_json

        write_json(client_conn, client_json)
        assert read_json(server_conn) == client_json


def test_invalid(connections):
    client_conn, server_conn = connections

    json = {"hello": True, client_conn: False}

    with pytest.raises(TypeError):
        write_json(server_conn, json)

    json_str = '{"hello": true, 0: false}'

    server_conn.sendall(bytes(json_str, encoding='utf-8'))

    with pytest.raises(JSONDecodeError):
        read_json(client_conn)


def test_close(connections):
    client_conn, server_conn = connections
    json = {"end of message": True}

    write_json(server_conn, json)
    server_conn.close()

    assert read_json(client_conn) == json
