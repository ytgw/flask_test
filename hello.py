from typing import Any, Literal
from flask import Flask, request, abort
from dataclasses import dataclass

app = Flask(__name__)

@app.route('/')     # type:ignore
def index():
    return 'Index Page'

@app.route('/login', methods=['GET', 'POST'])   # type:ignore
def login():
    if request.method == 'POST':    # type:ignore
        return 'login post'
    else:
        return 'login get'

@app.route('/post_json', methods=['POST'])  # type:ignore
def post_json() -> dict[str, Any]:
    json_data = request.get_json()
    if json_data is None:
        abort(400)
    return {'key1': json_data['key1'], 'key2': json_data['key2']}

@dataclass(frozen=True)
class PortPair:
    protocol: Literal['tcp', 'udp']
    original: int
    translated: int

@app.route('/post_port_numbers', methods=['POST'])  # type:ignore
def post_port_numbers():
    json_data = request.get_json()
    if json_data is None:
        abort(400)

    tcp_ports: list[int] = json_data['tcp_ports']
    udp_ports: list[int] = json_data['udp_ports']
    if (len(tcp_ports) == 0) and (len(udp_ports) == 0):
        abort(400)

    port_pairs: list[PortPair] = []
    for port in tcp_ports:
        port_pairs.append(PortPair(protocol='tcp', original=20000+port, translated=port))
    for port in udp_ports:
        port_pairs.append(PortPair(protocol='udp', original=30000+port, translated=port))

    return {
        'username': 'namae',
        'password': 'himitsu',
        'port_pairs': port_pairs
    }
