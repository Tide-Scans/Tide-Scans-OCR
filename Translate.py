from googletrans import Translator

def translateToEnglish(text = "defualt text"):
    # Initialize the translator
    translator = Translator()
    # Translate text from another language to English
    try:
        result = translator.translate(text, dest='en')
    except:
        return "There was an error during the translate proccess: " + text
    # Print the translated text
    return result.text