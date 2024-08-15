# CODXO-Autocorrect-Tool

# Grammar Correction using Transformer Pre-trained Model and SpellChecker

This project demonstrates how to perform grammar correction on sentences using a pre-trained transformer model and a spell checker. The process involves two main steps: 1) Correcting grammatical errors using a pre-trained transformer model, and 2) Correcting spelling errors using a spell checker.

## Prerequisites

- Python 3.11
- PyTorch
- Transformers (from Hugging Face)
- Nltk
- Pyspellchecker

## Installation

1. **Clone the repository**:
   ```bash
   https://github.com/HashamAkram18/CODXO_Autocorrect_Tool.git
   ```

2. **Navigate to the project directory**:
   ```bash
   cd Autocorrect Tool
   ```

3. **Create a virtual environment (optional but recommended)**:
   ```bash
   python -m venv Auto_Correct
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Import the necessary libraries**:
   ```python
   import torch
   from transformers import pipeline
   from nltk.tokenize import sent_tokenize
   from spellchecker import SpellChecker
   import transformers
   from transformers import pipeline
   from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
   ```

2. **Load the pre-trained transformer model for grammar correction**:
   ```python
    tokenizer = AutoTokenizer.from_pretrained("Unbabel/gec-t5_small")
    model = AutoModelForSeq2SeqLM.from_pretrained("Unbabel/gec-t5_small")
     ```

3. **Define a function to correct grammar using the transformer model**:
   ```python
   def correct_grammar_transformer(sentence):
    tokenized_sentence = tokenizer('gec: ' + sentence, max_length=128, truncation=True, padding='max_length', return_tensors='pt')
    corrected_sentence = tokenizer.decode(
        model.generate(
            input_ids = tokenized_sentence.input_ids,
            attention_mask = tokenized_sentence.attention_mask, 
            max_length=128,
            num_beams=5,
            early_stopping=True,
        )[0],
        skip_special_tokens=True, 
        clean_up_tokenization_spaces=True
    )
    return corrected_sentence
   ```

4. **Create an instance of the spell checker**:
   ```python
   spell = SpellChecker()
   ```

5. **Define a function to correct spelling using the spell checker**:
   ```python
   def correct_spelling(sentence):
    words = sentence.split()
    misspelled = spell.unknown(words)
    for word in misspelled:
      corrected_word = spell.correction(word)
      sentence = sentence.replace(word, corrected_word)
    return sentence
   ```

6. **Combine the grammar and spelling correction functions**:
   ```python
   def correct_sentence(sentence):
    # Transformer correction
    grammar_corrected = correct_grammar_transformer(sentence)
    # Spell checking
    final_corrected = correct_spelling(grammar_corrected)
    return final_corrected
   ```

7. **Test the correction process**:
   ```python
   original_text = "I am goin to the park to play with my frends."
   corrected_text = correct_sentence(input_sentence)
   print("Original text:", original_text)
   print("Corrected text:", corrected_text)
   ```

   Output:
   ```
   Original text: I am goin to the park to play with my frends.
   Corrected text: I am going to the park to play with my friends.
   ```

## Limitations

- The grammar correction model may not always provide perfect results, especially for complex sentences or context-dependent errors.
- The spell checker may not correct all spelling errors, especially for words that are valid but used incorrectly in the context.

## Future Improvements

- Explore other pre-trained models for grammar correction to improve accuracy.
- Implement more advanced error detection and correction techniques.
- Provide a user-friendly interface for easy text correction.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
