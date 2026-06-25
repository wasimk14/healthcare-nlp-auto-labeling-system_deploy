#Importing Libraries

from collections import Counter
import json
from pathlib import Path
import random
import pandas as pd
import spacy


# Confirming and setting project path

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR / "Data" / "Raw" #Contains datasets csv
PROJECT_ROOT = BASE_DIR / "Data" / "Processed"
SPLIT_DATA = BASE_DIR / "Data" / "Splits"
SRC = BASE_DIR / "Src" / "Training"
MODEL_PATH = BASE_DIR / "Models" / "spacy_baseline"
TEMPLATE_PATH = BASE_DIR / "templates"
# print(BASE_DIR)
# print(RAW_DIR)
# print(PROJECT_ROOT)
# print(SPLIT_DATA)
# print(SRC)
# print(MODEL_PATH)
# print(TEMPLATE_PATH)

from flask import Flask, render_template, request
from pathlib import Path
try:
    from .inference import extract_entities
except ImportError:
    from inference import extract_entities

app = Flask(__name__, template_folder=str(TEMPLATE_PATH))


@app.route("/", methods=["GET", "POST"])
def home():

    entities = []
    text = ""

    if request.method == "POST":

        text = request.form["clinical_note"]

        entities = extract_entities(text)

    return render_template(
        "index.html",
        entities=entities,
        clinical_note=text
    )

if __name__ == "__main__":
    app.run()