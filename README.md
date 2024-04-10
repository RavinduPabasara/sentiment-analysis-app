# sentiment-analysis-app
This is a simple Flask web application that performs sentiment analysis on user-provided text. It utilizes the NLTK library and Vader lexicon to determine the sentiment (positive, negative, or neutral) of the input text.
Features:

Takes text input from a user via a web form.
Analyzes the sentiment of the text using NLTK and Vader lexicon.
Displays the sentiment result on the same webpage.
How to Use

Prerequisites:

Python 3.x
Flask
NLTK
Installation:

Clone this repository:
git clone https://github.com/your-username/sentiment-analysis-app.git
Navigate to the project directory:
cd sentiment-analysis-app
Create a virtual environment (recommended) and activate it.
Install the required libraries:
pip install flask nltk
Download the Vader lexicon (NLTK will handle this automatically during the first run).
Run the App:

python main.py
This will start the Flask development server, usually accessible at http://127.0.0.1:5000/.

Usage:

Open the app in your web browser.
Enter text in the "Enter your text:" field.
Click the "Analyze" button.
The sentiment of the text will be displayed below the form.
Contributing

Feel free to fork this repository and make improvements! We welcome pull requests with bug fixes, new features, or enhancements.

License

This project is licensed under the MIT License. See the LICENSE file for details.
