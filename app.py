from flask import Flask
# from flask_bootstrap import Bootstrap

app = Flask(__name__)


def wrap_html(message):
    html = """
        <html>
        <body>
            <div style='font-size:50px;'>
            <center>
                <image height="700" width="800" src="https://i.imgur.com/eFqAqd7.jpg">
                <br>
                {0}<br>
            </center>
            </div>
        </body>
        </html>""".format(message)
    return html

@app.route('/')
def hello_world():
	f = open("VERSION", "r")
	version = f.read()
	message = f"My Awesome App running version {version}"
	html = wrap_html(message)
	return html


if __name__ == "__main__":
	app.run(host ='0.0.0.0', port = 5001, debug = True)
