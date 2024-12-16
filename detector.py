# pip install langdetect

from langdetect import detect, detect_langs

def detect_language_free(text):
    try:
        language_code = detect(text)
        probable_languages = detect_langs(text)
        
        print(f"Detected language code: {language_code}")
        print("Probable languages with confidence:")
        for lang in probable_languages:
            print(f"  {lang.lang}: {lang.prob:.2f}")
        return language_code
    except Exception as e:
        print(f"Error detecting language: {e}")
        return None

if __name__ == "__main__":
    # Example text for detection
    text_to_detect = "Bonjour tout le monde"
    
    # Call the function
    detected_language = detect_language_free(text_to_detect)
    
    if detected_language:
        print(f"The detected language is: {detected_language}")
