import os

from flask import Flask, send_from_directory
from flask_cors import CORS

from api.cassandra_keyspace import cassandra_keyspace

root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "portal", "build")

print('root path is ' + root)

app = Flask(__name__, static_url_path='', static_folder=root)
CORS(app)
app.register_blueprint(cassandra_keyspace, url_prefix='/api/cassandra/keyspaces')


@app.route('/', methods=['GET'])
def redirect_to_index():
    return send_from_directory(root, 'index.html')


if __name__ == '__main__':
    app.run()
