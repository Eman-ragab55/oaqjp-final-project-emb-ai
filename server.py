from flask import Flask, request, jsonify
from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_analyzer():

    text_to_analyze = request.args.get('textToAnalyze')

    # لو المستخدم مبعتش نص
    if not text_to_analyze:
        return "Invalid text! Please try again!"

    response = emotion_detector(text_to_analyze)

    # لو الرجوع فاضي أو فيه None
    if not response or response.get("dominant_emotion") is None:
        return "Could not analyze emotion. Please try again!"

    return (
        f"For the given statement, "
        f"the system response is "
        f"'anger': {response.get('anger')}, "
        f"'disgust': {response.get('disgust')}, "
        f"'fear': {response.get('fear')}, "
        f"'joy': {response.get('joy')}, "
        f"'sadness': {response.get('sadness')}. "
        f"The dominant emotion is {response.get('dominant_emotion')}."
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)