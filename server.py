''' Module designed for handling and running the app's server.
    This only contains two routes:
    - The root/index page
    - The API route that gets called whenever the "Run Sentiment Analysis" button
      is clicked on the page. This will take the text inputted by the user and
      send it over to the Emotion Prediction Analysis API and score based on the
      emotions detected.
'''

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

# The root/index page
@app.route("/")
def index():
    ''' Load the index.html template '''
    return render_template("index.html")

# POST API route for hanlding emotion detection analysis
@app.route("/emotionDetector")
def emotion_detect():
    ''' This route gets called whenever the user clicks the "Run Sentiment Analysis"
        button on the webpage. This will take the text inputted by the user and
        sends it over to the Emotion Prediction Analysis API, before returning back the
        scores based on the range of emotions detected in the text.
    '''

    # Retrieve the text from the request arguments for analysis
    text_to_analyze = request.args.get("textToAnalyze")

    # Pass the text over to the emotion detector function and return the response
    response = emotion_detector(text_to_analyze)

    # Return an error message back to the user if invalid text
    # was provided (e.g. no text given for analysis)
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

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
