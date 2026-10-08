"""Flask web server for the Emotion Detection application."""

from flask import Flask, jsonify, render_template, request

from EmotionDetection.emotion_detection import emotion_detector


app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the Emotion Detector home page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Analyze the text supplied by the user."""
    text_to_analyze = request.args.get("textToAnalyze", "")

    if not text_to_analyze.strip():
        return "Invalid text! Please try again!."

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!."

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
