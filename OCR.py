import SnippingTool
import pytesseract
pytesseract.pytesseract.tesseract_cmd = 'Tesseract-OCR/tesseract.exe'

def ocr(language = str):
    image = SnippingTool.getImage()

    if image == None:
        return None

    match language:
        case "English":
            language = "eng"
        case "Japanese":
            language = "jpn"
        case "Chinese - Simplified":
            language = "chi_sim"
        case "Chinese - Traditional":
            language = "chi_tra"
        case _:
            language = "eng"    

    # Use pytesseract to extract text
    try:
        extracted_text = pytesseract.image_to_string(image, lang=language)
    except: 
        return "There was an error, during the Optical character recognition proceess."

    image.save("temp.png", "PNG")
    return extracted_text