from flask import Flask
from redis import Redis


app = Flask(__name__)
redis = Redis(host='redis', port=6379)


@app.route('/')
def hello():
    redis.incr('hits')
    return 'This Compose/Flask demo has been viewed {hits:d} time(s).'.format(hits=int(redis.get('hits')))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500, debug=True)
