from flask import Flask, request, redirect
import requests
import os

app = Flask(__name__)

CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")

@app.route("/")
def home():
    return f"""
    <a href="https://discord.com/oauth2/authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}&scope=identify guilds.join">
    Login With Discord
    </a>
    """

@app.route("/callback")
def callback():
    code = request.args.get("code")
    return f"Authorized! Code: {code}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
