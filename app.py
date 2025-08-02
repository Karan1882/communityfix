from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "✅ Flask is working! Hello from CommunityFix."

if __name__ == '__main__':
    app.run(debug=True)
