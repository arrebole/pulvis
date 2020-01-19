from flask import Flask
from pkg.auth import setup as authSetup

app = authSetup(Flask(__name__))


if __name__ == "__main__":
    app.run(debug=True)
