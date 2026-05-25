import requests

def emotion_detector(text_to_analyse):

    URL = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"

    HEADERS = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    default_output = {
        "anger": 0,
        "disgust": 0,
        "fear": 0,
        "joy": 0,
        "sadness": 0,
        "dominant_emotion": "joy"
    }

    try:
        response = requests.post(URL, json=input_json, headers=HEADERS, timeout=10)
        response.raise_for_status()

        formatted_response = response.json()

        emotions_list = formatted_response.get("emotionPredictions", [])

        if not emotions_list:
            return default_output

        emotions = emotions_list[0].get("emotion", {})

        for key in default_output:
            if key != "dominant_emotion":
                emotions.setdefault(key, 0)

        dominant_emotion = max(emotions, key=emotions.get)

        emotions["dominant_emotion"] = dominant_emotion

        return emotions

    except:
        return default_output