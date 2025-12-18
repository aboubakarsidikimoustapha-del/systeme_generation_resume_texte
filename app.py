import streamlit as st
from summarizer import extractive_summary, abstractive_summary
from generator import generate_text

# CORRECTION : st.set_page_config() doit être la première commande Streamlit.
st.set_page_config(
    page_title="Générateur & Résumeur",
    layout="wide"
)

def check_password():
    """Affiche un formulaire de connexion et gère l'authentification."""
    st.title("🔐 Connexion")
    st.markdown("Veuillez entrer le mot de passe pour accéder à l'application.")
    
    password = st.text_input("Mot de passe", type="password")

    if st.button("Se connecter"):
        expected_password = st.secrets.get("APP_PASSWORD", "default_password")
        
        if password == expected_password:
            st.session_state["password_correct"] = True
            # CORRECTION : Utilisation de st.rerun()
            st.rerun()
        else:
            st.error("Le mot de passe fourni est incorrect.")
    return False

def run_app():
    """Exécute l'application principale après une connexion réussie."""
    i18n = {
        "fr": {
            "title": "🤖 Système de Génération et Résumé de Texte NLP",
            "description": "Une application pour générer et résumer des textes, basée sur des modèles Transformers.",
            "sidebar_lang": "Langue",
            "sidebar_nav": "Navigation",
            "feature_summary": "Résumé de Texte",
            "feature_generation": "Génération de Texte",
            "summary_header": "Résumé de Texte",
            "summary_desc": "Collez un texte ci-dessous pour le résumer.",
            "summary_type_label": "Choisissez le type de résumé",
            "summary_type_abs": "Abstractif (avancé, plus lent)",
            "summary_type_ext": "Extractif (baseline, plus rapide)",
            "summary_text_area": "Texte à résumer",
            "summary_placeholder": "Entrez votre texte ici...",
            "summary_button": "Lancer le résumé",
            "summary_result": "Résultat",
            "warning_empty_text": "Veuillez entrer un texte à résumer.",
            "generation_header": "Génération de Texte",
            "generation_desc": "Entrez un début de phrase (prompt)...",
            "generation_prompt": "Votre prompt",
            "generation_placeholder": "Le futur de l'IA est...",
            "generation_button": "Générer le texte",
            "footer_info": "Projet DSC559 – PROJET 3"
        },
        "en": {
            "title": "🤖 NLP Text Generation and Summarization System",
            "description": "An application to generate and summarize texts, based on Transformer models.",
            "sidebar_lang": "Language",
            "sidebar_nav": "Navigation",
            "feature_summary": "Text Summary",
            "feature_generation": "Text Generation",
            "summary_header": "Text Summary",
            "summary_desc": "Paste a text below to summarize it.",
            "summary_type_label": "Choose the summary type",
            "summary_type_abs": "Abstractive (advanced, slower)",
            "summary_type_ext": "Extractive (baseline, faster)",
            "summary_text_area": "Text to summarize",
            "summary_placeholder": "Enter your text here...",
            "summary_button": "Run Summary",
            "summary_result": "Result",
            "warning_empty_text": "Please enter a text to summarize.",
            "generation_header": "Text Generation",
            "generation_desc": "Enter a starting phrase (prompt)...",
            "generation_prompt": "Your prompt",
            "generation_placeholder": "The future of AI is...",
            "generation_button": "Generate Text",
            "footer_info": "DSC559 Project – PROJECT 3"
        }
    }
    
    st.sidebar.title(i18n["fr"]["sidebar_lang"] + " / " + i18n["en"]["sidebar_lang"])
    lang_choice = st.sidebar.selectbox("", ("Français", "English"))
    lang_code = "fr" if lang_choice == "Français" else "en"
    T = i18n[lang_code]

    st.title(T["title"])
    st.markdown(T["description"])

    st.sidebar.title(T["sidebar_nav"])
    app_mode = st.sidebar.radio("", (T["feature_summary"], T["feature_generation"]))

    if app_mode == T["feature_summary"]:
        st.header(T["summary_header"])
        st.markdown(T["summary_desc"])
        summary_type = st.selectbox(T["summary_type_label"], (T["summary_type_abs"], T["summary_type_ext"]))
        text_to_summarize = st.text_area(T["summary_text_area"], height=250, placeholder=T["summary_placeholder"])
        if st.button(T["summary_button"]):
            if text_to_summarize:
                st.subheader(T["summary_result"])
                is_abstractive = "Abstractif" in summary_type or "Abstractive" in summary_type
                with st.spinner("Génération en cours..."):
                    if is_abstractive:
                        summary = abstractive_summary(text_to_summarize, lang=lang_code)
                    else:
                        summary = extractive_summary(text_to_summarize, lang=lang_code)
                    st.success(summary)
            else:
                st.warning(T["warning_empty_text"])

    elif app_mode == T["feature_generation"]:
        st.header(T["generation_header"])
        st.markdown(T["generation_desc"])
        prompt = st.text_input(T["generation_prompt"], placeholder=T["generation_placeholder"])
        if st.button(T["generation_button"]):
            if prompt:
                st.subheader(T["summary_result"])
                with st.spinner("Génération en cours..."):
                    generated_text = generate_text(prompt, lang=lang_code)
                    st.success(generated_text)
            else:
                st.warning("Veuillez entrer un prompt.")

    st.sidebar.markdown("---")
    st.sidebar.info(T["footer_info"])

# --- Point d'Entrée ---
if "password_correct" not in st.session_state:
    st.session_state["password_correct"] = False

if not st.session_state["password_correct"]:
    check_password()
else:
    run_app()