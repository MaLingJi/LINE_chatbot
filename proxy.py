#coding:utf-8
import json
import dialogflow_v2 as dialogflow



# ===== dialog config
project_id = 'test-wciryd'
session_id = 0
language_code = 'zh-tw'
#======


def detect_intent_texts(project_id, session_id, texts, language_code):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    for text in texts:
        text_input = dialogflow.types.TextInput(text=texts, language_code=language_code)
        query_input = dialogflow.types.QueryInput(text=text_input)
        response = session_client.detect_intent(session=session, query_input=query_input)
        print(response.query_result.query_text)
        return response.query_result.fulfillment_text

if __name__ == "__main__":
    while 1:
        texts="颱風資訊"
        #print(texts)
        Response=detect_intent_texts(project_id, session_id, str(texts), language_code)
        print(Response)
