from deep_translator import GoogleTranslator
text = input("Enter the text to translate: ")
language = input("Enter the target language (e.g., 'en' for English, 'es' for Spanish): ")
translated = GoogleTranslator(source="auto", target=language).translate(text)
print("\nTranslated text:", translated)