import requests
import json

def emotion_detector(text_to_analyze):
    # Handle blank input
    if not text_to_analyze.strip():
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Watson NLP API setup
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "Content-Type": "application/json",
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    # Make the API request
    response = requests.post(url, headers=headers, json=payload)

    # Handle API error response
    if response.status_code == 400:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }

    # Parse the response
    response_dict = json.loads(response.text)
    emotions = response_dict['emotionPredictions'][0]['emotion']

    # Extract emotion scores
    anger = emotions['anger']
    disgust = emotions['disgust']
    fear = emotions['fear']
    joy = emotions['joy']
    sadness = emotions['sadness']

    # Determine dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)

    return {
        'anger': anger,
        'disgust': disgust,
        'fear': fear,
        'joy': joy,
        'sadness': sadness,
        'dominant_emotion': dominant_emotion
    }