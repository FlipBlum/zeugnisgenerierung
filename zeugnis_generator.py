import os
import openai
from dotenv import load_dotenv
from string import Template
from langchain.chat_models import ChatOpenAI

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-4", temperature=0.5)


def map_note(note, mapping):
    return mapping.get(note, "")


note_map = {
    1: "stets zur vollsten Zufriedenheit",
    2: "stets zur vollen Zufriedenheit",
    3: "zur vollen Zufriedenheit",
    4: "im Großen und Ganzen zur Zufriedenheit",
    5: "nicht zur Zufriedenheit"
}

verhalten_map = {
    1: "nicht zufriedenstellend",
    2: "ausbaufähig",
    3: "insgesamt zufriedenstellend",
    4: "gut",
    5: "stets vorbildlich"
}

def generate_zeugnis(user_data):
    template_path = f"prompts/{user_data['zeugnis_typ'].lower().replace('ü', 'ue').replace('ä', 'ae').replace('ö', 'oe')}.txt"

    with open(template_path, "r", encoding="utf-8") as f:
        template = Template(f.read())

    # Bewertungen in Textform bringen
    user_data.update({
        "fachwissen_text": map_note(user_data["fachwissen"], note_map),
        "auffassungsgabe_text": map_note(user_data["auffassungsgabe"], note_map),
        "arbeitsweise_text": map_note(user_data["arbeitsweise"], note_map),
        "arbeitserfolg_text": map_note(user_data["arbeitserfolg"], note_map),
        "belastbarkeit_text": map_note(user_data["belastbarkeit"], note_map),
        "motivation_text": map_note(user_data["motivation"], note_map),
        "leistung_text": map_note(user_data["leistung"], note_map),
        "verhalten_text": verhalten_map.get(user_data["verhalten"], ""),
        "kontakt_text": f"{user_data['anrede']} {user_data['nachname']} pflegte stets einen professionellen Kontakt zu unseren Kunden." if user_data["kontakt"] else "",
        "erfolge_text": f"{user_data['anrede']} {user_data['nachname']} konnte in ihrer/seiner Tätigkeit besondere Erfolge erzielen." if user_data["erfolge"] else "",
        "wiederbewerbung_text": f"Wir würden uns freuen, {user_data['anrede']} {user_data['nachname']} erneut im Unternehmen begrüßen zu dürfen." if user_data["wiederbewerbung"] else "",
        "empfehlung_text": f"Wir empfehlen {user_data['anrede']} {user_data['nachname']} uneingeschränkt für neue berufliche Herausforderungen." if user_data["empfehlung"] else "",
        "zusaetze_text": ", ".join(user_data["zusaetze"]) if user_data["zusaetze"] else ""
    })

    # Tätigkeitstext vorbereiten
    user_data["taetigkeiten_formatiert"] = "\n".join(f"- {t}" for t in user_data["taetigkeiten"])

    # Prompt an LLM schicken
    prompt_input = template.substitute(user_data)

    response = llm.predict(prompt_input)

    return response
