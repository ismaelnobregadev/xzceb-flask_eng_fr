import json
from ibm_watson import LanguageTranslatorV3

from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['API_KEY']
url = os.environ['API_URL']

authenticator = IAMAuthenticator(apikey)

language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

def englishToFrench(englishText):
    
    """
    translate english text to french
    """
    if englishText is None:
        return None
    response = language_translator.translate(text=englishText,model_id="en-fr").get_result()

    frenchText = response['translations'][0]['translation']

    return frenchText

def frenchToEnglish(frenchText):
    
    """
    translate french to english
    """
    if frenchText is None:
        return None
    response = language_translator.translate(text=frenchText,model_id="fr-en").get_result()
    englishText = response['translations'][0]['translation']
    
    return englishText

