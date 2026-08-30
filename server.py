from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Create a list called 'events' with a couple of sample event dictionaries
# Each dictionary should have an 'id' and a 'title'
events = [
    {"id": 1, "title": "Yoga in the Park"},
    {"id": 2, "title": "Lake 5K Run"}
]
next_id = 3  # used to assign unique IDs to new events

# TASK: Create a route for "/"
# This route should return a JSON welcome message
@app.route("/", methods=["GET"])
def welcome():
    return jsonify({"message": "Welcome!"}), 200

# TASK: Create a GET route for "/events"
# This route should return the full list of events as JSON
@app.route("/events", methods=["GET"])
def get_events():
    return jsonify(events), 200

# TASK: Create a POST route for "/events"
# This route should:
# 1. Get the JSON data from the request
# 2. Validate that "title" is provided
# 3. Create a new event with a unique ID and the provided title
# 4. Add the new event to the events list
# 5. Return the new event with status code 201
@app.route("/events", methods=["POST"])
def add_event():
    # 1. Get JSON data
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400

    data = request.get_json()

    # 2. Validate that "title" is provided (and not empty)
    if "title" not in data or not data["title"].strip():
        return jsonify({"error": "Missing or empty 'title' field"}), 400

    # 3. Create a new event with a unique ID and title
    global next_id
    new_event = {"id": next_id, "title": data["title"].strip()}
    # 4. Add it to the list
    events.append(new_event)
    next_id += 1

    # 5. Return the new event with status 201
    return jsonify(new_event), 201

if __name__ == "__main__":
    app.run(debug=True)