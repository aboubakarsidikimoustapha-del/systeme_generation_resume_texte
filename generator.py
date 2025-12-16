# Ce fichier contiendra la fonction pour la génération de texte.

import streamlit as st
import torch
from transformers import pipeline

# Utilisation du cache pour éviter de recharger le modèle à chaque appel
@st.cache_resource
def get_text_generator():
    """Charge et retourne le pipeline de génération de texte."""
    return pipeline(
        "text-generation",
        model="dbddv01/gpt2-french-small",
        torch_dtype=torch.bfloat16 # Utiliser bfloat16 pour de meilleures performances si supporté
    )

def generate_text(prompt, max_length=100):
    """
    Génère du texte à partir d'un prompt en utilisant un modèle GPT-2.
    """
    generator = get_text_generator()
    # Nous utilisons num_return_sequences=1 pour n'avoir qu'une seule proposition
    generated_text = generator(prompt, max_length=max_length, num_return_sequences=1)
    return generated_text[0]['generated_text']
