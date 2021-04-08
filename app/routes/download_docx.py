import docx
import os
from app import app
from flask import request, send_from_directory, abort, redirect, url_for

@app.route("/save", methods = ["POST"])
def save_docx():
    try:
        data = request.form["data"]
        doc = docx.Document()
        doc.add_paragraph(data)
        filename = str(request.form["docname"])
        path = os.path.join(app.config["CLIENT_DOCX"], filename)
        doc.save(path)
        return '/static/userdocuments/'+filename
    except FileNotFoundError:
        abort(404)

    