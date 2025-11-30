import configparser
import json
from flask import Flask, jsonify

app = Flask(__name__)

def parse_config():
    config = configparser.ConfigParser()
    config.read("/Users/lilash/Practice Assignmnt01/Devops-Assignment01/config-parser/config.ini")

    data = {
        "Database": {
            "host": config.get("Database", "host"),
            "port": config.get("Database", "port"),
            "username": config.get("Database", "username"),
            "password": config.get("Database", "password"),
        },
        "Server": {
            "address": config.get("Server", "address"),
            "port": config.get("Server", "port"),
        }
    }

    return data


@app.route("/config", methods=["GET"])
def get_config():
    data = parse_config()
    return jsonify(data)


if __name__ == "__main__":
    # Save JSON output to a file (this simulates storing in a DB)
    parsed = parse_config()
    with open("output.json", "w") as f:
        json.dump(parsed, f, indent=4)
    
    print("Config parsed and saved as output.json")
    print("Starting API server at: http://127.0.0.1:5000/config")

    app.run(debug=True)
