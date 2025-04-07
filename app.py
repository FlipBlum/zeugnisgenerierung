import streamlit as st
from zeugnis_generator import generate_zeugnis

st.set_page_config(page_title="Zeugnisgenerator", layout="centered")
st.title("📝 Zeugnisgenerator")

# Zeugnistyp Auswahl
zeugnis_typ = st.selectbox("Zeugnistyp", ["Arbeitszeugnis", "Praktikumszeugnis", "Ausbildungszeugnis"])

# Basisdaten
st.subheader("Allgemeine Informationen")
anrede = st.selectbox("Anrede", ["Herr", "Frau"])
vorname = st.text_input("Vorname")
nachname = st.text_input("Nachname")
geburtsdatum = st.date_input("Geburtsdatum")
eintrittsdatum = st.date_input("Eintrittsdatum")
austrittsdatum = st.date_input("Austrittsdatum")
position = st.text_input("Position")
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
        "anrede": anrede,
        "vorname": vorname,
        "nachname": nachname,
        "geburtsdatum": geburtsdatum.strftime("%d.%m.%Y"),
        "eintrittsdatum": eintrittsdatum.strftime("%d.%m.%Y"),
        "austrittsdatum": austrittsdatum.strftime("%d.%m.%Y"),
        "position": position,
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
