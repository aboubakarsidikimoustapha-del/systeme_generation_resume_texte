import streamlit as st
import torch
from transformers import pipeline

@st.cache_resource
def get_text_generator():
    """Charge le modèle de génération de texte et le met en cache."""
    return pipeline(
        "text-generation",
        model="dbddv01/gpt2-french-small",
        torch_dtype=torch.bfloat16
    )

def generate_text(prompt, max_length=150):
    """Génère du texte à partir d'un prompt."""
    generator = get_text_generator()
    generated_text = generator(prompt, max_length=max_length, num_return_sequences=1)
    return generated_text[0]['generated_text']