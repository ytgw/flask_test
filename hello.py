from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'login post'
    else:
        return 'login get'

@app.route('/post_json', methods=['POST'])
def post_json():
    json_data = request.get_json()
    return {'key1': json_data['key1'], 'key2': json_data['key2']}
