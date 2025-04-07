import os
import openai
from dotenv import load_dotenv
from string import Template
from langchain.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model_name="gpt-4", temperature=0.2)

def generate_zeugnis(user_data):
    zeugnistyp = user_data["zeugnis_typ"]
    anrede = user_data["anrede"]
    vorname = user_data["vorname"]
    nachname = user_data["nachname"]
    geburtsdatum = user_data["geburtsdatum"]
    eintrittsdatum = user_data["eintrittsdatum"]
    austrittsdatum = user_data["austrittsdatum"]
    position = user_data["position"]
    ort = user_data["ort"]
    datum = user_data["datum"]
    aufgaben = user_data["taetigkeiten"]
    fachwissen = user_data["fachwissen"]
    auffassungsgabe = user_data["auffassungsgabe"]
    arbeitsweise = user_data["arbeitsweise"]
    arbeitserfolg = user_data["arbeitserfolg"]
    belastbarkeit = user_data["belastbarkeit"]
    motivation = user_data["motivation"]
    leistung = user_data["leistung"]
    verhalten = user_data["verhalten"]
    ausscheidungsgrund = user_data["ausscheidungsgrund"]
    kontakt = user_data["kontakt"]
    empfehlung = user_data["empfehlung"]
    wiederbewerbung = user_data["wiederbewerbung"]
    erfolge = user_data["erfolge"]
    zusaetze = user_data["zusaetze"]

    struktur_vorgabe = """
Bitte verwende beim Formulieren des Zeugnisses folgende Struktur:

1. Einleitung:
   - Name, Geburtsdatum, Zeitraum und Position
2. Aufgabenbeschreibung:
   - Auflistung und Beschreibung der Tätigkeiten
3. Fachliche Leistung:
   - Bewertung von Fachwissen, Auffassungsgabe, Motivation etc.
4. Arbeitsweise und Arbeitserfolg:
   - Qualität, Effizienz, Sorgfalt
5. Sozialverhalten:
   - Verhalten gegenüber Vorgesetzten, Kolleg:innen und Kund:innen
6. Optional:
   - Erwähnung besonderer Erfolge, Zusatzkompetenzen, Empfehlung
7. Schlussformulierung:
   - Dank, Bedauern, Zukunftswünsche, Ort und Datum
"""

    prompt = PromptTemplate(
    input_variables=[
        "zeugnis_typ",
        "anrede",
        "vorname",
        "nachname",
        "geburtsdatum",
        "eintrittsdatum",
        "austrittsdatum",
        "position",
        "ort",
        "datum",
        "taetigkeiten",
        "fachwissen",
        "auffassungsgabe",
        "arbeitsweise",
        "arbeitserfolg",
        "belastbarkeit",
        "motivation",
        "leistung",
        "verhalten",
        "ausscheidungsgrund",
        "kontakt",
        "empfehlung",
        "wiederbewerbung",
        "erfolge",
        "zusaetze",
    ],
    template="""
Erstelle ein professionelles, gut formuliertes und vollständiges {zeugnis_typ} auf Deutsch basierend auf den folgenden Informationen. Verwende eine klare, strukturierte und typische Zeugnissprache. Das Zeugnis soll alle wichtigen Komponenten enthalten: Einleitung, Tätigkeiten, Leistungsbeurteilung, Sozialverhalten, ggf. Erfolge, Schlussteil mit Austrittsgrund und Empfehlung.

Hier sind die Angaben:

- Anrede: {anrede}
- Vorname: {vorname}
- Nachname: {nachname}
- Geburtsdatum: {geburtsdatum}
- Position: {position}
- Eintrittsdatum: {eintrittsdatum}
- Austrittsdatum: {austrittsdatum}
- Tätigkeiten:
{taetigkeiten}

Leistungsbeurteilung:
- Fachwissen: {fachwissen}
- Auffassungsgabe: {auffassungsgabe}
- Arbeitsweise: {arbeitsweise}
- Arbeitserfolg: {arbeitserfolg}
- Belastbarkeit: {belastbarkeit}
- Motivation: {motivation}
- Gesamtleistung: {leistung}
- Sozialverhalten: {verhalten}

Weitere Angaben:
- Erfolge: {erfolge}
- Zusätzliche Eigenschaften / Stärken: {zusaetze}
- Kontakt zu Kunden und Geschäftspartnern: {kontakt}
- Empfehlung: {empfehlung}
- Wiederbewerbung erwünscht: {wiederbewerbung}
- Ausscheidungsgrund: {ausscheidungsgrund}

Ort und Datum:
- Ort: {ort}
- Datum: {datum}

Bitte achte auf:
- überprüfe deinen Text auf Inkonsistenzen in den Notenformulierungen.
- achte auf Dopplungen in den Formulierungen.
- einen natürlichen, fließenden Stil.
- professionelle Formulierungen entsprechend dem Zeugnisstil.
- konsistente Notenformulierungen entsprechend den Bewertungen.
- eine Länge von ca. 300–500 Wörtern.
"""
)

    final_prompt = prompt.format(
    zeugnis_typ=user_data["zeugnis_typ"],
    anrede=user_data["anrede"],
    vorname=user_data["vorname"],
    nachname=user_data["nachname"],
    geburtsdatum=user_data["geburtsdatum"],
    eintrittsdatum=user_data["eintrittsdatum"],
    austrittsdatum=user_data["austrittsdatum"],
    position=user_data["position"],
    ort=user_data["ort"],
    datum=user_data["datum"],
    taetigkeiten="\n".join(user_data["taetigkeiten"]),
    fachwissen=user_data["fachwissen"],
    auffassungsgabe=user_data["auffassungsgabe"],
    arbeitsweise=user_data["arbeitsweise"],
    arbeitserfolg=user_data["arbeitserfolg"],
    belastbarkeit=user_data["belastbarkeit"],
    motivation=user_data["motivation"],
    leistung=user_data["leistung"],
    verhalten=user_data["verhalten"],
    ausscheidungsgrund=user_data["ausscheidungsgrund"],
    kontakt=user_data["kontakt"],
    empfehlung=user_data["empfehlung"],
    wiederbewerbung=user_data["wiederbewerbung"],
    erfolge=user_data["erfolge"],
    zusaetze=user_data["zusaetze"],
)

    response = llm.invoke(final_prompt)
    return response.content
