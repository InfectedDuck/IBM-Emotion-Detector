"""
Emotion Detector!!
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def sent_detector():
    """
    Analyzes the user-provided text for emotions and returns the result.

    Query Parameters:
    - textToAnalyze: The text to analyze for emotions.

    Returns:
    - A string summarizing the detected emotions and the dominant emotion.
    """
    text_to_detect = request.args.get('textToAnalyze')

    if not text_to_detect:
        return "Invalid text! Please try again."

    response = emotion_detector(text_to_detect)

    if not response or response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    return (
        f"For the given statement, the system response is 'anger': {formated_response['anger']} "
        f"'disgust': {formated_response['disgust']}, 'fear': {formated_response['fear']}, "
        f"'joy': {formated_response['joy']} and 'sadness': {formated_response['sadness']}. "
        f"The dominant emotion is {formated_response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Renders the main application page.

    Returns:
    - The HTML content of the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
