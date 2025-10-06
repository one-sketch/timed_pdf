from flask import Flask, render_template, send_file, abort
from datetime import datetime

app = Flask(__name__)

# set release time
RELEASE_TIME = datetime(2025, 10, 7, 12, 0)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get-pdf")
def get_pdf():
    now = datetime.now()
    if now >= RELEASE_TIME:
        return send_file("secret.pdf", as_attachment=True)
    else:
        abort(403)  # this will trigger your custom 403 page

# custom 403 error page
@app.errorhandler(403)
def forbidden(e):
    return render_template("403.html"), 403

if __name__ == "__main__":
    app.run(debug=True)
# Note: Ensure you have 'secret.pdf' in the same directory as this script
# and create 'templates/index.html' and 'templates/403.html' for rendering.
