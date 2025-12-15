from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route("/")
def results():
    a = r.get("Option A") or 0
    b = r.get("Option B") or 0
    return f"""
    <h2>Results</h2>
    <p>Option A: {a}</p>
    <p>Option B: {b}</p>
    """

app.run(host="0.0.0.0", port=80)
