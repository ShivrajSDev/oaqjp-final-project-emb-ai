from EmotionDetection.emotion_detection import emotion_detector
from flask import Flask, request, render_template, json

app = Flask("Emotion Detection")

@app.route("/")
def index():
    return render_template("index.html")

''' This route gets called whenever the user clicks the "Run Sentiment Analysis"
    button on the webpage. This will take the text inputted by the user and
    sends it over to the Emotion Prediction Analysis API,before returning back the
    scores based on the range of emotions detected in the text.
'''
@app.route("/emotionDetector")
def emotion_detect():
    # Retrieve the text from the request arguments for analysis
    text_to_analyze = request.args.get("textToAnalyze")

    # Pass the text over to the emotion detector function and return the response
    response = emotion_detector(text_to_analyze)

    # Define the message to be displayed to the user
    message = "For the given statement, the system response is "
    message += f"'anger': {response['anger']}, "
    message += f"'disgust': {response['disgust']}, "
    message += f"'fear': {response['fear']}, "
    message += f"'joy': {response['joy']} "
    message += f"and 'sadness': {response['sadness']}. "
    message += f"The dominant emotion is {response['dominant_emotion']}."

    # Return the formatted message
    return message

app.run(host="0.0.0.0", port="5000")
