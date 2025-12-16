# Ce fichier contiendra les fonctions pour le résumé de texte (extractif et abstractif).

import streamlit as st
import torch
from transformers import pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import nltk

# S'assurer que le tokeniseur de phrases de NLTK est téléchargé
try:
    nltk.data.find('tokenizers/punkt')
except nltk.downloader.DownloadError:
    nltk.download('punkt')

# ----- Modèle de résumé abstractif (Hugging Face) -----
# Utilisation du cache pour éviter de recharger le modèle à chaque appel
@st.cache_resource
def get_abstractive_summarizer():
    """Charge et retourne le pipeline de résumé abstractif."""
    return pipeline(
        "summarization",
        model="plguillou/t5-base-fr-sum-cnndm",
        torch_dtype=torch.bfloat16 # Utiliser bfloat16 pour de meilleures performances si supporté
    )

def abstractive_summary(text, min_length=30, max_length=150):
    """
    Génère un résumé abstractif du texte en utilisant un modèle T5.
    """
    summarizer = get_abstractive_summarizer()
    summary = summarizer(text, min_length=min_length, max_length=max_length, truncation=True)
    return summary[0]['summary_text']


# ----- Modèle de résumé extractif (Baseline TF-IDF) -----
def extractive_summary(text, num_sentences=3):
    """
    Génère un résumé extractif en sélectionnant les phrases les plus importantes
    via le score TF-IDF.
    """
    # 1. Séparer le texte en phrases
    sentences = nltk.sent_tokenize(text, language='french')

    if len(sentences) <= num_sentences:
        return text

    # 2. Créer une représentation TF-IDF des phrases
    vectorizer = TfidfVectorizer(stop_words='french')
    try:
        tfidf_matrix = vectorizer.fit_transform(sentences)
    except ValueError:
        # Peut arriver si le texte ne contient que des stop words
        return "Le texte fourni est trop court ou ne contient pas de mots significatifs pour générer un résumé."


    # 3. Calculer le score de chaque phrase (somme des scores TF-IDF de ses mots)
    sentence_scores = np.array(tfidf_matrix.sum(axis=1)).ravel()

    # 4. Sélectionner les indices des N phrases avec les meilleurs scores
    top_sentence_indices = sentence_scores.argsort()[-num_sentences:][::-1]

    # Ordonner les phrases sélectionnées selon leur ordre d'apparition original
    top_sentence_indices.sort()

    # 5. Concaténer les phrases pour former le résumé
    summary = " ".join([sentences[i] for i in top_sentence_indices])
    return summary
