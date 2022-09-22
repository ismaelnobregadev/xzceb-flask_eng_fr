# import json

from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def english2french(english_text):
    """
    translate english text to french
    """
    if english_text is None:
        return None
    response = language_translator.translate(text=english_text,model_id="en-fr").get_result()
    french_text = response['translations'][0]['translation']
    return french_text

def french2english(french_text):
    """
    translate french to english
    """
    if french_text is None:
        return None
    response = language_translator.translate(text=french_text,model_id="fr-en").get_result()
    english_text = response['translations'][0]['translation']
    return english_text
    