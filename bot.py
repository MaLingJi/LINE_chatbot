import os.path
import sys
import json
try:
    import apiai
except ImportError:
    sys.path.append(
        os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)
    )
    import apiai
 
CLIENT_ACCESS_TOKEN = '15838659c7bd49d793ae9b00c9ab2c4b' # put your CLIENT_ACCESS_TOKEN here
 
def dialog_detect(say):
    ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)
 
    request = ai.text_request()
 
    request.lang = 'tw'  # optional, default value equal 'en'
 
    request.query = say
    response = request.getresponse().read().decode()
    result=json.loads(response)