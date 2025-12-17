import streamlit as st
from summarizer import extractive_summary, abstractive_summary
from generator import generate_text

# Configuration de la page (titre de l'onglet, icône, layout)
st.set_page_config(
    page_title="Générateur & Résumeur de Texte",
    page_icon="✍️",
    layout="wide"
)

# Titre principal et description
st.title("🤖 Système de Génération et Résumé de Texte NLP")
st.markdown("Une application pour générer et résumer des textes en français, basée sur des modèles Transformers.")

# Barre latérale de navigation
st.sidebar.title("Navigation")
app_mode = st.sidebar.radio("Choisissez une fonctionnalité", ["Résumé de Texte", "Génération de Texte"])

# --- PAGE RÉSUMÉ DE TEXTE ---
if app_mode == "Résumé de Texte":
    st.header("Résumé de Texte")
    st.markdown("Collez un texte ci-dessous pour le résumer.")

    summary_type = st.selectbox(
        "Choisissez le type de résumé",
        ("Abstractif (avancé, plus lent)", "Extractif (baseline, plus rapide)")
    )
    
    text_to_summarize = st.text_area("Texte à résumer", height=250, placeholder="Entrez votre texte ici...")

    if st.button("Lancer le résumé"):
        if text_to_summarize:
            st.subheader("Résultat")
            if "Abstractif" in summary_type:
                with st.spinner("Génération du résumé abstractif en cours..."):
                    summary = abstractive_summary(text_to_summarize)
                    st.success(summary)
            else:
                with st.spinner("Génération du résumé extractif en cours..."):
                    summary = extractive_summary(text_to_summarize)
                    st.info(summary)
        else:
            st.warning("Veuillez entrer un texte à résumer.")

# --- PAGE GÉNÉRATION DE TEXTE ---
elif app_mode == "Génération de Texte":
    st.header("Génération de Texte")
    st.markdown("Entrez un début de phrase (prompt) pour que le modèle génère la suite.")

    prompt = st.text_input("Votre prompt", placeholder="Par exemple : 'Le futur de l'intelligence artificielle est...'")

    if st.button("Générer le texte"):
        if prompt:
            st.subheader("Résultat")
            with st.spinner("Génération du texte en cours..."):
                generated_text = generate_text(prompt)
                st.success(generated_text)
        else:
            st.warning("Veuillez entrer un prompt.")

# Pied de page dans la barre latérale
st.sidebar.markdown("---")
st.sidebar.info("Projet DSC559 – PROJET 3")