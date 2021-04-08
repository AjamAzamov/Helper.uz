from flask import Flask

app = Flask(__name__)
app.config.from_object("config.ProductionConfig")

from app.routes import root
from app.routes import uploads
from app.routes import check
from app.routes import download_docx