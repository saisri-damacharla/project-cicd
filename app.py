from flask import Flask, render_template
import redis

app = Flask(__name__)
redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route('/')
def home():
    # Increment visitor count
    visitor_count = redis_client.incr('visitor_count')
    return render_template('index.html', count=visitor_count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
