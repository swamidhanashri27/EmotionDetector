from unittest.mock import patch
from EmotionDetection.emotion_detection import emotion_detector

@patch("EmotionDetection.emotion_detection.requests.post")
def test_package(mock_post):
    mock_post.return_value.status_code = 200
    mock_post.return_value.text = '{"emotionPredictions":[{"emotion":{"anger":0.01,"disgust":0.02,"fear":0.03,"joy":0.90,"sadness":0.04}}]}'
    mock_post.return_value.raise_for_status = lambda: None

    result = emotion_detector("I love this new technology")
    print(result)

test_package()
