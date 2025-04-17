import os
from dotenv import load_dotenv
from string import Template
from langchain_community.chat_models import ChatOpenAI

load_dotenv()

llm = ChatOpenAI(model_name="gpt-4o", temperature=0.2)

PROMPT_PATHS = {
    "Arbeitszeugnis": "prompts/arbeitszeugnis.txt",
    "Ausbildungszeugnis": "prompts/ausbildungszeugnis.txt",
    "Praktikumszeugnis": "prompts/praktikumszeugnis.txt"
}

def generate_zeugnis(user_data):
    zeugnistyp = user_data["zeugnis_typ"]
    prompt_path = PROMPT_PATHS.get(zeugnistyp, "prompts/arbeitszeugnis.txt")
    with open(prompt_path, "r", encoding="utf-8") as f:
        prompt_template = Template(f.read())

    # Die Platzhalter in den Prompt-Dateien werden mit den Userdaten ersetzt
    prompt_filled = prompt_template.safe_substitute({
        "anrede": user_data.get("anrede", ""),
        "vorname": user_data.get("vorname", ""),
        "nachname": user_data.get("nachname", ""),
        "geburtsdatum": user_data.get("geburtsdatum", ""),
        "eintrittsdatum": user_data.get("eintrittsdatum", ""),
        "austrittsdatum": user_data.get("austrittsdatum", ""),
        "position": user_data.get("position", ""),
        "ort": user_data.get("ort", ""),
        "datum": user_data.get("datum", ""),
        "taetigkeiten": "\n".join(user_data.get("taetigkeiten", [])),
        "fachwissen": user_data.get("fachwissen", ""),
        "auffassungsgabe": user_data.get("auffassungsgabe", ""),
        "arbeitsweise": user_data.get("arbeitsweise", ""),
        "arbeitserfolg": user_data.get("arbeitserfolg", ""),
        "belastbarkeit": user_data.get("belastbarkeit", ""),
        "motivation": user_data.get("motivation", ""),
        "leistung": user_data.get("leistung", ""),
        "verhalten": user_data.get("verhalten", ""),
        "ausscheidungsgrund": user_data.get("ausscheidungsgrund", ""),
        "kontakt": user_data.get("kontakt", ""),
        "empfehlung": user_data.get("empfehlung", ""),
        "wiederbewerbung": user_data.get("wiederbewerbung", ""),
        "erfolge": user_data.get("erfolge", ""),
        "zusaetze": user_data.get("zusaetze", "")
    })

    response = llm.invoke(prompt_filled)
    return response.content
