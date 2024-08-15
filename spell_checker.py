
from spellchecker import SpellChecker

spell = SpellChecker()

def correct_spelling(sentence):
  words = sentence.split()
  misspelled = spell.unknown(words)
  for word in misspelled:
    corrected_word = spell.correction(word)
    sentence = sentence.replace(word, corrected_word)
  return sentence