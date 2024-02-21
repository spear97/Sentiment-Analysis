# Import the sentiment_analyzer function from SentimentAnalysis.sentiment_analysis module
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest  # Import the unittest module

# Create a test class that inherits from unittest.TestCase
class TestSentimentAnalyzer(unittest.TestCase):
    
    # Define a test method for the sentiment_analyzer function
    def test_sentiment_analyzer(self):
        # Test positive sentiment
        result_1 = sentiment_analyzer('I love working with Python')
        self.assertEqual(result_1['label'], 'SENT_POSITIVE')  # Check if the label is 'SENT_POSITIVE'
        
        # Test negative sentiment
        result_2 = sentiment_analyzer('I hate working with Python')
        self.assertEqual(result_2['label'], 'SENT_NEGATIVE')  # Check if the label is 'SENT_NEGATIVE'
        
        # Test neutral sentiment
        result_3 = sentiment_analyzer('I am neutral on Python')
        self.assertEqual(result_3['label'], 'SENT_NEUTRAL')  # Check if the label is 'SENT_NEUTRAL'

# Run the tests if this script is executed directly
if __name__ == '__main__':
    unittest.main()
