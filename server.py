"""
server.py — Flask web server for emotion detection.

This module sets up routes for receiving text input and returning emotion analysis
using the EmotionDetection module.
"""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector", methods=["GET", "POST"])
def detect_emotion():
    """
    Handles emotion detection requests via GET or POST.

    Returns:
        str: A formatted string with emotion scores and dominant emotion,
             or an error message if input is invalid.
    """
    if request.method == "POST":
        text_to_analyze = request.form['text']
    else:
        text_to_analyze = request.args.get('textToAnalyze')

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return response

@app.route("/")
def index():
    """
    Renders the homepage.

    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, port=5001)
