import transformers
from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

tokenizer = AutoTokenizer.from_pretrained("Unbabel/gec-t5_small")
model = AutoModelForSeq2SeqLM.from_pretrained("Unbabel/gec-t5_small")

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