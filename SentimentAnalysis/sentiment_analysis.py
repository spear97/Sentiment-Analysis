# Import necessary libraries
import requests  # Library for making HTTP requests
import json  # Library for working with JSON data

# Function to perform sentiment analysis
def sentiment_analyzer(text_to_analyze):
    # URL of the sentiment analysis service
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    
    # Data to be sent in the POST request
    myobj = { "raw_document": { "text": text_to_analyze } }
    
    # Headers for the POST request
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    
    # Send POST request to the sentiment analysis service
    response = requests.post(url, json=myobj, headers=header)
    
    # Parse the JSON response
    formatted_response = json.loads(response.text)
    
    # Check the status code of the response
    if response.status_code == 200:
        # If successful (status code 200), extract label and score
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    elif response.status_code == 500:
        # If internal server error (status code 500), set label and score to None
        label = None
        score = None
    
    # Return a dictionary with label and score
    return {'label': label, 'score': score}
