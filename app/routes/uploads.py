import os

from app import app
from flask import render_template, request, redirect, abort, url_for
from werkzeug.utils import secure_filename


def allowed_image(filename):
    if not "." in filename:
        return False
    ext = filename.rsplit(".", 1)[1]
    if ext.upper() in app.config["ALLOWED_IMAGE_EXTENSIONS"]:
        return True
    else:
        return False

images = []
@app.route("/uploads", methods=["POST"])
def upload_file():
    try:
        if request.method == "POST":
            if request.files:
                image = request.files["image"]
                if image.filename == "":
                    return redirect(request.url)
                if not allowed_image(image.filename):
                    return redirect(request.url)
                    
                else:
                    filename = secure_filename(image.filename)
                    image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
                return url_for("check", imagename=filename)
        return render_template("index.html")
    except:
        abort(400)