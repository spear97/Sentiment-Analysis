// Function to run sentiment analysis
let RunSentimentAnalysis = () => {
    // Get the value of the input field with id "textToAnalyze"
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    // Create a new XMLHttpRequest object
    let xhttp = new XMLHttpRequest();

    // Define a function to handle the response
    xhttp.onreadystatechange = function() {
        // Check if the request is complete and successful
        if (this.readyState == 4 && this.status == 200) {
            // Update the content of the element with id "system_response"
            document.getElementById("system_response").innerHTML = xhttp.responseText;
        }
    };

    // Construct the URL for the GET request
    let url = "sentimentAnalyzer?textToAnalyze=" + encodeURIComponent(textToAnalyze);

    // Open a new GET request
    xhttp.open("GET", url, true);

    // Send the request
    xhttp.send();
};
