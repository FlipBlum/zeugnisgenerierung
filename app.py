import streamlit as st
from zeugnis_generator import generate_zeugnis
import os

st.set_page_config(page_title="Zeugnisgenerator", layout="centered")
st.title("📝 Zeugnisgenerator")

# Zeugnistyp Auswahl
zeugnis_typ = st.selectbox("Zeugnistyp", ["Arbeitszeugnis", "Praktikumszeugnis", "Ausbildungszeugnis"])
zwischenzeugnis = st.checkbox("Zwischenzeugnis")

# Basisdaten
st.subheader("Allgemeine Informationen")
anrede = st.selectbox("Anrede", ["Herr", "Frau"])
vorname = st.text_input("Vorname")
nachname = st.text_input("Nachname")
geburtsdatum = st.date_input("Geburtsdatum")
eintrittsdatum = st.date_input("Eintrittsdatum")
if not zwischenzeugnis:
    austrittsdatum = st.date_input("Austrittsdatum")
else:
    austrittsdatum = None
position = st.text_input("Position")

# Unternehmen der TERRAS-Gruppe und Beschreibungen aus Textdateien laden
def lade_unternehmensbeschreibungen(pfad="unternehmensbeschreibungen"):
    unternehmen_dict = {}
    if os.path.isdir(pfad):
        for datei in os.listdir(pfad):
            if datei.endswith(".txt"):
                name = datei.replace("_", " ").replace(".txt", "")
                with open(os.path.join(pfad, datei), "r", encoding="utf-8") as f:
                    unternehmen_dict[name] = f.read().strip()
    return unternehmen_dict

terras_unternehmen = lade_unternehmensbeschreibungen()
terras_unternehmen["Anderes Unternehmen (bitte angeben)"] = ""

unternehmen = st.selectbox(
    "Unternehmen (Firmenname)",
    list(terras_unternehmen.keys()),
    index=0
)

# Automatische Befüllung der Unternehmensbeschreibung
if unternehmen != "Anderes Unternehmen (bitte angeben)":
    unternehmensbeschreibung = st.text_area(
        "Unternehmensbeschreibung (wird automatisch ausgefüllt, kann angepasst werden)",
        value=terras_unternehmen[unternehmen],
        key="unternehmensbeschreibung"
    )
else:
    unternehmensbeschreibung = st.text_area(
        "Unternehmensbeschreibung (bitte selbst eingeben)",
        value="",
        key="unternehmensbeschreibung"
    )

abteilung = st.text_input("Abteilung/Einsatzort")
ort = st.text_input("Ort")
datum = st.date_input("Datum der Ausstellung")

# Tätigkeiten
st.subheader("Tätigkeiten")
taetigkeiten = st.text_area("Bitte listen Sie die wichtigsten Tätigkeiten stichpunktartig auf", height=200)

# Leistungsbeurteilung
st.subheader("Leistungsbeurteilung (1 = sehr gut, 5 = mangelhaft)")
fachwissen = st.slider("Fachwissen", 1, 5, 2)
auffassungsgabe = st.slider("Auffassungsgabe", 1, 5, 2)
arbeitsweise = st.slider("Arbeitsweise", 1, 5, 2)
arbeitserfolg = st.slider("Arbeitserfolg", 1, 5, 2)
belastbarkeit = st.slider("Belastbarkeit", 1, 5, 2)
motivation = st.slider("Motivation", 1, 5, 2)
leistung = st.slider("Gesamtleistung", 1, 5, 2)
verhalten = st.slider("Verhalten gegenüber Vorgesetzten & Kollegen", 1, 5, 3)

# Zusätzliche Felder
st.subheader("Zusatzinformationen")
kontakt = st.radio("Hatte die Person Kundenkontakt?", ["Ja", "Nein"])
empfehlung = st.radio("Soll eine Empfehlung ausgesprochen werden?", ["Ja", "Nein"])
wiederbewerbung = st.radio("Würden Sie die Person erneut einstellen?", ["Ja", "Nein"])
erfolge = st.checkbox("Gab es besondere Erfolge?")
zusaetze = st.multiselect("Zusätzliche positive Eigenschaften", [
    "Teamfähigkeit", "Lernbereitschaft", "Zuverlässigkeit", "Resilienz",
    "Flexibilität", "Problemlösungskompetenz", "Kreativität", "Eigeninitiative", "Anpassungsfähigkeit"
])

ausscheidungsgrund = st.text_input("Ausscheidungsgrund (optional)", placeholder="z. B. Das Arbeitsverhältnis endete auf eigenen Wunsch.")

if st.button("🔍 Zeugnis generieren"):
    user_data = {
        "zeugnis_typ": zeugnis_typ,
        "zwischenzeugnis": zwischenzeugnis,
        "anrede": anrede,
        "vorname": vorname,
        "nachname": nachname,
        "geburtsdatum": geburtsdatum.strftime("%d.%m.%Y"),
        "eintrittsdatum": eintrittsdatum.strftime("%d.%m.%Y"),
        "austrittsdatum": austrittsdatum.strftime("%d.%m.%Y") if austrittsdatum else "",
        "position": position,
        "unternehmen": unternehmen,
        "unternehmensbeschreibung": unternehmensbeschreibung,
        "abteilung": abteilung,
        "ort": ort,
        "datum": datum.strftime("%d.%m.%Y"),
        "taetigkeiten": taetigkeiten.split("\n"),
        "fachwissen": fachwissen,
        "auffassungsgabe": auffassungsgabe,
        "arbeitsweise": arbeitsweise,
        "arbeitserfolg": arbeitserfolg,
        "belastbarkeit": belastbarkeit,
        "motivation": motivation,
        "leistung": leistung,
        "verhalten": verhalten,
        "ausscheidungsgrund": ausscheidungsgrund,
        "kontakt": kontakt,
        "empfehlung": empfehlung,
        "wiederbewerbung": wiederbewerbung,
        "erfolge": erfolge,
        "zusaetze": zusaetze,
    }

    zeugnis_text = generate_zeugnis(user_data)

    st.subheader("📄 Generiertes Zeugnis")
    st.text_area("Zeugnis", zeugnis_text, height=600)
