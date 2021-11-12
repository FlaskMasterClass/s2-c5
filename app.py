import os

from flask import Flask
from flask import flash
from flask import render_template
from flask import request
from flask_uploads import IMAGES
from flask_uploads import UploadSet
from flask_uploads import configure_uploads

app = Flask(__name__)
photos = UploadSet("photos", IMAGES)
app.config["UPLOADED_PHOTOS_DEST"] = "static/img"
app.config["SECRET_KEY"] = os.urandom(24)
app.config["UPLOADS_AUTOSERVE"] = False
configure_uploads(app, photos)


@app.route("/", methods=["GET", "POST"])
def upload():
    if request.method == "POST" and "photo" in request.files:
        photos.save(request.files["photo"])
        flash("Photo saved successfully.")
        return render_template("upload.html")
    return render_template("upload.html")


if __name__ == "__main__":
    app.run()
