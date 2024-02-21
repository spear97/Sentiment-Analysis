'''
Executing this function initiates the application of sentiment
analysis to be executed over the Flask channel and deployed on
localhost:5000.
'''
# Import necessary modules
from flask import Flask, make_response, request, render_template
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer  # Import sentiment_analyzer function

# Create Flask app instance
app = Flask("Sentiment Analyzer")

# Route for sentiment analysis
@app.route("/sentimentAnalyzer")
def sent_analyzer():
    # Get the text to analyze from the query parameters
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Call the sentiment_analyzer function from the SentimentAnalysis module
    response = sentiment_analyzer(text_to_analyze)
    
    # Extract label and score from the response
    label = response['label']
    score = response['score']
    
    # Check if label is None (invalid input) and return appropriate message
    if label is None:
        return "Invalid input! Try again."
    else:
        # Return the result with the identified label and score
        return "The given text has been identified as {} with a score of {}.".format(label.split('_')[1], score)

# Route for the main page
@app.route("/")
def render_index_page():
    return render_template('index.html')  # Render the HTML template for the main page

# Run the app if this script is executed
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Run the app on host 0.0.0.0 (accessible from outside) and port 5000
