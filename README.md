# Sentiment Analysis

This project demonstrates a simple web application built with Flask for performing sentiment analysis using a BERT-based model. The application allows users to input text, analyze its sentiment, and view the result.

## Sentiment Analysis Function

The `sentiment_analyzer` function performs sentiment analysis using a BERT-based model hosted on a remote service. It sends a POST request to the sentiment analysis service, retrieves the result, and returns the sentiment label and score.

## Flask Application

### Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Application
To run the Flask application, execute the following command:
  ```bash
  python app.py
  ```
The server will start on `http://localhost:5000/`.

### Endpoints
- `/sentimentAnalyzer`:
  - Method: GET
  - Parameters:
    - `textToAnalyze`: Text to be analyzed for sentiment.
  - Example Usage: http://localhost:5000/sentimentAnalyzer?textToAnalyze=YourTextHere
- `/`: Main page of the application.
  -  Method: GET
  -  Provides a simple interface to enter text for sentiment analysis.
 
### Directory Structure
- `app.py`: Contains the Flask application code with defined routes.
- `SentimentAnalysis/sentiment_analysis.py`: Module with the sentiment_analyzer function for sentiment analysis.
- `templates/index.html`: HTML template for the main page with input fields and buttons.
- `static/`: Directory for static files such as JavaScript (`mywebscript.js`).

### Dependencies
- `Flask`: A lightweight WSGI web application framework.
- `requests`: Library for making HTTP requests.
- `json`: Library for working with JSON data.

### Usage
1. Access the main page at `http://localhost:5000/`.
2. Enter the text you want to analyze in the provided input field.
3. Click the "Run Sentiment Analysis" button to view the sentiment analysis result.

### NOTE
- The sentiment analysis model used in this application is hosted on a remote service. Ensure a stable internet connection for accurate results.
- If the input text is invalid or the model encounters an error, an appropriate message will be displayed.
