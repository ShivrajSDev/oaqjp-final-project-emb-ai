import requests, json

def emotion_detector(text_to_analyze):
    # Define the URL for the emotion prediction analysis
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Set the headers required for the API request, including the model ID
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Define the JSON data to be sent via POST API, including the text for analysis
    my_obj = { "raw_document": { "text": text_to_analyze } }

    # Make the POST API request
    response = requests.post(url = url, headers = headers, json = my_obj)

    # Retrieve the JSON data from the API response and extract the set of emotions
    response_json = json.loads(response.text)
    emotions = response_json["emotionPredictions"][0]["emotion"]

    # Initialise data, then search through all emotions to determine the dominant
    # emotion based on their score
    dominant_emotion = 'none'
    dominant_score = 0

    for key in emotions.keys():
        emotion_score = emotions[key]
        if emotion_score >= dominant_score:
            dominant_score = emotion_score
            dominant_emotion = key

    # Make a copy for the emotions set and include the dominant emotion
    result = emotions.copy()
    result["dominant_emotion"] = dominant_emotion

    # Return the emotion data
    return result
