# 📝 Arbeitszeugnis Generator

Ein interaktives Tool zur Erstellung professioneller Arbeits-, Praktikums- und Ausbildungszeugnisse – powered by **Streamlit**, **LangChain** und **OpenAI GPT-4**.

## 🚀 Features

- ✍️ Erzeugung von Arbeits-, Praktikums- und Ausbildungszeugnissen
- 🎛️ Dynamisches Eingabeformular mit Schulnoten & Freitextfeldern
- 🧠 Automatische Textgenerierung via GPT-4
- 🧾 Zeugnistext im professionellen Fließtext-Stil
- 🔁 Auswahl zwischen mehreren Templates je nach Zeugnistyp
- 📤 Exportierbarer Text zur Weiterverarbeitung

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
├── requirements.txt        # Abhängigkeiten
└── README.md               # Projektdokumentation
```

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
