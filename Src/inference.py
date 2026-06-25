from pathlib import Path
import spacy

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "Models" / "spacy_baseline" / "model-best"

nlp = spacy.load(MODEL_PATH)


def extract_entities(text):
    doc = nlp(text)

    entities = []

    for ent in doc.ents:
        entities.append(
            {
                "text": ent.text,
                "label": ent.label_
            }
        )

    return entities
