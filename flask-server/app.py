from flask import Flask, render_template

app = Flask(__name__, static_folder="../static/static",
            template_folder="../static")


@app.route("/hello")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    app.run()
