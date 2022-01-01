from typing import Any
from flask import Flask, request, abort

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
