from spell_checker import correct_spelling
from transformer_corrector import correct_grammar_transformer
import streamlit as st

def correct_sentence(sentence):
  # Transformer correction
  grammar_corrected = correct_grammar_transformer(sentence)
  # Spell checking
  final_corrected = correct_spelling(grammar_corrected)
  return final_corrected

# Streamlit app
st.title("Sentence Correction App")

input_sentence = st.text_area("Enter a sentence to correct:")
if st.button("Correct"):
    # Correct grammar and Correct spelling
    grammar_corrected = correct_sentence(input_sentence)
    
    st.write("Corrected Sentence:", grammar_corrected) 