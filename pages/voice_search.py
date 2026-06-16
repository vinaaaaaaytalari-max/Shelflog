import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import streamlit as st
import speech_recognition as sr
import pyttsx3
from i18n import t

# ---------------- PRODUCTS ----------------

products = [
    {
        "name": "Rice",
        "price": 60,
        "stock": 120
    },
    {
        "name": "Milk",
        "price": 35,
        "stock": 8
    },
    {
        "name": "Laptop",
        "price": 55000,
        "stock": 15
    },
    {
        "name": "Mouse",
        "price": 799,
        "stock": 4
    }
]

# ---------------- TTS ----------------

def _safe_decode(value):
    if isinstance(value, bytes):
        try:
            return value.decode("utf-8", errors="ignore")
        except Exception:
            return str(value)
    return str(value)


def _choose_english_voice(engine):
    try:
        voices = engine.getProperty("voices") or []
        for voice in voices:
            voice_id = _safe_decode(getattr(voice, "id", ""))
            voice_name = _safe_decode(getattr(voice, "name", ""))
            languages = getattr(voice, "languages", []) or []
            languages_text = " ".join(_safe_decode(lang) for lang in languages)

            if (
                "english" in voice_name.lower()
                or "en" in voice_id.lower()
                or "en" in languages_text.lower()
            ):
                engine.setProperty("voice", voice_id)
                break
    except Exception:
        pass


def init_tts_engine():
    try:
        engine = pyttsx3.init("espeak")
    except Exception:
        try:
            engine = pyttsx3.init()
        except Exception:
            return None

    _choose_english_voice(engine)
    return engine

engine = init_tts_engine()

if not engine:
    st.warning("TTS engine unavailable: voice playback disabled.")


def speak(text):
    if not engine:
        return
    try:
        engine.say(text)
        engine.runAndWait()
    except Exception:
        return

# ---------------- UI ----------------

st.title(t("voice_title"))

language = st.selectbox(
    t("language_label"),
    [
        "en-IN",
        "hi-IN",
        "te-IN",
        "pa-IN"
    ]
)

st.write(t("commands_label"))
st.info("""
Search Milk

Search Rice

Show low stock products
""")

# ---------------- BUTTON ----------------

def _handle_query(query: str):
    query = query.lower()

    # LOW STOCK COMMAND
    if "low stock" in query:
        st.subheader("⚠ Low Stock Products")

        found = False

        for p in products:
            if p["stock"] < 10:
                found = True
                st.error(f"{p['name']} ({p['stock']} left)")

        speak("Showing low stock products")
        return

    # SEARCH PRODUCT
    found = False

    for p in products:

        if p["name"].lower() in query:

            found = True

            st.subheader(f"📦 {p['name']}")

            st.write(f"💰 Price : ₹{p['price']}")
            st.write(f"📦 Stock : {p['stock']}")

            if p["stock"] > 50:
                st.success(t("in_stock"))

            elif p["stock"] > 10:
                st.warning(t("running_low"))

            else:
                st.error(t("critical_stock"))

            speak(
                f"{p['name']} available. Stock is {p['stock']}"
            )

    if not found:
        st.error("Product not found")
        speak("Product not found")


if st.button(t("start_listening")):

    r = sr.Recognizer()

    # Try using the microphone; if PyAudio / PortAudio isn't installed,
    # fall back to a typed input so the page remains functional.
    try:
        with sr.Microphone() as source:

            st.info(t("listening"))

            audio = r.listen(source)

            try:
                query = r.recognize_google(
                    audio,
                    language=language
                )

                st.success(t("you_said").format(text=query))
                _handle_query(query)

            except Exception:
                st.error(t("could_not_understand"))

    except AttributeError:
        st.warning("Microphone backend (PyAudio) not available — please type a command instead.")
        text_query = st.text_input(t("type_command"))
        if text_query:
            st.success(t("you_typed").format(text=text_query))
            _handle_query(text_query)

    except Exception as e:
        st.warning(f"Microphone unavailable: {e}. Falling back to text input.")
        text_query = st.text_input(t("type_command"))
        if text_query:
            st.success(t("you_typed").format(text=text_query))
            _handle_query(text_query)