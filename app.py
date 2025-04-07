import streamlit as st
from zeugnis_generator import generate_zeugnis
from fpdf import FPDF

st.title("📝 Arbeitszeugnis Generator")

with st.form("zeugnis_form"):
    art = st.selectbox("Zeugnistyp", ["Arbeitszeugnis", "Praktikumszeugnis", "Ausbildungszeugnis"])
    zwischenzeugnis = st.checkbox("Zwischenzeugnis?")
    anrede = st.selectbox("Anrede", ["Herr", "Frau", "Divers"])
    titel = st.text_input("Titel")
    vorname = st.text_input("Vorname")
    nachname = st.text_input("Nachname")
    geburtsdatum = st.date_input("Geburtsdatum")

    firmenname = st.text_input("Firmenname")
    firmenbeschreibung = st.text_area("Firmenbeschreibung")

    berufsbezeichnung = st.text_input("Berufsbezeichnung")
    beschaeftigung = st.selectbox("Beschäftigungsart", ["Vollzeit", "Teilzeit"])
    beginn = st.date_input("Beschäftigungsbeginn")
    ende = st.date_input("Beschäftigungsende")
    abteilung = st.text_input("Abteilung")
    einsatzort = st.text_input("Einsatzort")
    taetigkeiten = st.text_area("Tätigkeiten")

    st.subheader("Fachliche Bewertung")
    fachwissen = st.slider("Fachwissen", 1, 5, 3)
    belastbarkeit = st.slider("Belastbarkeit", 1, 5, 3)
    auffassungsgabe = st.slider("Auffassungsgabe", 1, 5, 3)
    arbeitsweise = st.slider("Arbeitsweise", 1, 5, 3)
    arbeitserfolg = st.slider("Arbeitserfolg", 1, 5, 3)
    motivation = st.slider("Motivation", 1, 5, 3)
    leistung = st.slider("Leistungszusammenfassung", 1, 5, 3)

    erfolge = st.checkbox("Berufliche Erfolge hervorheben?")
    zusaetze = st.multiselect("Zusätzliche Eigenschaften", [
        "IT-Kenntnisse", "Marktkenntnisse", "Zuverlässigkeit", "Motivation und Begeisterung",
        "Eigeninitiative und Proaktivität", "Anpassungsfähigkeit, Resilienz und Flexibilität",
        "Lernbereitschaft und Kreativität", "Kommunikationsfähigkeit",
        "Verantwortungsbewusstsein und Selbstorganisation", "Teamfähigkeit",
        "Problemlösungskompetenz", "Anerkennung und Wertschätzung"
    ])

    verhalten = st.slider("Verhalten gegenüber Führungskräften & Kolleg:innen", 1, 5, 3)
    kontakt = st.checkbox("Kontakt zu Kunden oder Partnern?")
    grund = st.text_area("Grund für das Ausscheiden")
    wiederbewerbung = st.checkbox("Wiederbewerbung erwünscht?")
    empfehlung = st.checkbox("Empfehlung aussprechen?")

    submitted = st.form_submit_button("Zeugnis generieren")

if submitted:
    user_data = {
        "art": art,
        "anrede": anrede,
        "titel": titel,
        "vorname": vorname,
        "nachname": nachname,
        "geburtsdatum": geburtsdatum.strftime("%d.%m.%Y"),
        "firmenname": firmenname,
        "firmenbeschreibung": firmenbeschreibung,
        "berufsbezeichnung": berufsbezeichnung,
        "beschaeftigung": beschaeftigung,
        "beginn": beginn.strftime("%d.%m.%Y"),
        "ende": ende.strftime("%d.%m.%Y"),
        "abteilung": abteilung,
        "einsatzort": einsatzort,
        "taetigkeiten": taetigkeiten,
        "fachwissen": fachwissen,
        "belastbarkeit": belastbarkeit,
        "auffassungsgabe": auffassungsgabe,
        "arbeitsweise": arbeitsweise,
        "arbeitserfolg": arbeitserfolg,
        "motivation": motivation,
        "leistung": leistung,
        "erfolge": "Ja" if erfolge else "Nein",
        "zusaetze": ", ".join(zusaetze),
        "verhalten": verhalten,
        "kontakt": "Ja" if kontakt else "Nein",
        "grund": grund,
        "wiederbewerbung": "Ja" if wiederbewerbung else "Nein",
        "empfehlung": "Ja" if empfehlung else "Nein"
    }

    zeugnis_text = generate_zeugnis(user_data)

    # PDF export
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    for line in zeugnis_text.split("\n"):
        pdf.multi_cell(0, 10, line)

    pdf.output("zeugnis.pdf")
    with open("zeugnis.pdf", "rb") as f:
        st.download_button("📄 Zeugnis herunterladen", f, "zeugnis.pdf")

