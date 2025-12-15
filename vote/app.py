from flask import Flask
import redis

app = Flask(__name__)
r = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.route("/vote/<option>")
def vote(option):
    if option not in ["A", "B"]:
        return "Invalid option", 400
    key = f"Option {option}"
    r.incr(key)
    return f"Voted for {option}"

@app.route("/")
def home():
    return """
    <h2>Voting App</h2>
    <p><a href="/vote/A">Vote Option A</a></p>
    <p><a href="/vote/B">Vote Option B</a></p>
    """

app.run(host="0.0.0.0", port=80)
