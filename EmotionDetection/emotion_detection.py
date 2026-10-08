"""Emotion detection service using the Watson NLP API."""

import json
import requests

URL = (
    "https://sn-watson-emotion.labs.skills.network/"
    "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
)

HEADERS = {
    "grpc-metadata-mm-model-id":
    "emotion_aggregated-workflow_lang_en_stock"
}


def _empty_result():
    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None
    }


def emotion_detector(text_to_analyze):
    """Detect emotions using the Watson NLP EmotionPredict service."""
    if not text_to_analyze or not text_to_analyze.strip():
        return _empty_result()

    payload = {
        "raw_document": {
            "text": text_to_analyze
        }
    }

    try:
        response = requests.post(
            URL,
            headers=HEADERS,
            json=payload,
            timeout=20
        )

        if response.status_code == 400:
            return _empty_result()

        response.raise_for_status()

        result = json.loads(response.text)
        emotions = result["emotionPredictions"][0]["emotion"]
        dominant_emotion = max(emotions, key=emotions.get)

        return {
            "anger": emotions["anger"],
            "disgust": emotions["disgust"],
            "fear": emotions["fear"],
            "joy": emotions["joy"],
            "sadness": emotions["sadness"],
            "dominant_emotion": dominant_emotion
        }

    except (requests.RequestException, KeyError, IndexError, json.JSONDecodeError):
        return _empty_result()
