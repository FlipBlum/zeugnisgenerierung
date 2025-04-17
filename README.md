# 📝 Arbeitszeugnis Generator

Ein interaktives Tool zur Erstellung professioneller Arbeits-, Praktikums- und Ausbildungszeugnisse – powered by **Streamlit**, **LangChain** und **OpenAI GPT-4**.

## 🚀 Features

- ✍️ Erzeugung von Arbeits-, Praktikums- und Ausbildungszeugnissen
- 🎛️ Dynamisches Eingabeformular mit Schulnoten & Freitextfeldern
- 🧠 Automatische Textgenerierung via GPT-4
- 🧾 Zeugnistext im professionellen Fließtext-Stil
- 🔁 Auswahl zwischen mehreren Templates je nach Zeugnistyp
- 📤 Exportierbarer Text zur Weiterverarbeitung
- 🏢 Unternehmensbeschreibungen werden dynamisch aus einzelnen Textdateien geladen

## 🖥️ Vorschau

![App Screenshot](./screenshots/app_screenshot.png)

## ⚙️ Technologien

- [Streamlit](https://streamlit.io/) – für das UI
- [LangChain](https://www.langchain.com/) – zur Prompt-Verwaltung
- [OpenAI GPT-4](https://platform.openai.com/) – für natürliche Textgenerierung
- [Python](https://www.python.org/) – Backend-Logik

## 📂 Projektstruktur

```
├── app.py                  # Streamlit UI
├── zeugnis_generator.py    # Logik zur Textgenerierung
├── prompts/                # Prompt- und Template-Dateien
│   ├── arbeitszeugnis.txt
│   ├── ausbildungszeugnis.txt
│   ├── praktikumszeugnis.txt
│   └── zeugnis_template.txt
├── unternehmensbeschreibungen/ # Einzelne .txt-Dateien für jede Firma
│   ├── TERRAS_Bau_GmbH.txt
│   ├── ...
├── requirements.txt        # Abhängigkeiten
└── README.md               # Projektdokumentation
```

## 🏢 Unternehmensbeschreibungen pflegen

Die Beschreibungen der Unternehmen werden aus einzelnen Textdateien im Ordner `unternehmensbeschreibungen/` geladen. Jede Datei entspricht einem Unternehmen (z.B. `TERRAS_Bau_GmbH.txt`).

**So fügst du ein neues Unternehmen hinzu:**
1. Lege eine neue `.txt`-Datei im Ordner `unternehmensbeschreibungen/` an.
2. Der Dateiname sollte dem Unternehmensnamen entsprechen (Leerzeichen durch Unterstriche ersetzen).
3. Schreibe die gewünschte Beschreibung (zwei Sätze empfohlen) in die Datei.
4. Nach dem Speichern steht das Unternehmen automatisch in der App zur Auswahl.

## 🛠️ Installation

```bash
# 1. Repository klonen
git clone https://github.com/dein-nutzername/zeugnis-generator.git
cd zeugnis-generator

# 2. Virtuelle Umgebung (optional aber empfohlen)
python -m venv venv
source venv/bin/activate   # oder .\venv\Scripts\activate auf Windows

# 3. Abhängigkeiten installieren
pip install -r requirements.txt

# 4. .env-Datei anlegen
echo "OPENAI_API_KEY=dein-openai-api-key" > .env

# 5. App starten
streamlit run app.py
```

---

**Hinweis:**
- Für die Nutzung wird ein OpenAI API Key benötigt.
- Unternehmensbeschreibungen können jederzeit durch Bearbeiten oder Hinzufügen von .txt-Dateien im Ordner `unternehmensbeschreibungen/` angepasst werden.
