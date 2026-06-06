from flask import Flask
import os, socket

app = Flask(__name__)

@app.route("/")
def home():
    version = os.getenv("APP_VERSION", "1.0")
    host = socket.gethostname()

    return (
        "<h1>Version 2 deployed successfully!</h1>"
        f"<p>Served by container host: {host}</p>"
        f"<p>App version: {version}</p>"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)