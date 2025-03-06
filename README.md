# Text Summarization Application

This project is a simple Flask application that summarizes user-input text. It takes text input, performs summarization, and displays the result on the screen. When the page is refreshed, the summary is cleared. Users can also reset the summary by clicking the "Reset" button.

## Features

- Accepts text input from the user
- Analyzes the text and selects key sentences
- Displays the summarized text on the screen
- Allows users to clear the summary with a "Reset" button
- The summary disappears when the page is refreshed

## Requirements

To run this project, you need to have the following installed on your system:

- Python 3
- Flask
- NLTK (for Natural Language Processing)

## Installation

1. **Clone or download the repository:**
   ```bash
   git clone https://github.com/username/text-summarization-app.git
   cd text-summarization-app
   ```
2. **Install the required dependencies:**
   ```bash
   pip install flask nltk
   ```
3. **Download NLTK datasets:**
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```
4. **Run the application:**
   ```bash
   python app.py
   ```
5. **Open in browser:**
   ```
   http://127.0.0.1:5000/
   ```

## Usage

1. Enter text into the input box.
2. Click the "Summarize" button.
3. The summarized text will be displayed on the page.
4. Click the "Reset" button to clear the summary.
5. Refreshing the page will automatically remove the summary.

## Project Structure

```
text-summarization-app/
│-- app.py          # Flask application
│-- templates/
│   ├── index.html  # User interface
│-- README.md       # Project documentation
```

## Contribution

You can contribute to this project by forking the repository and submitting pull requests. If you want to add new features, follow these steps:

1. **Fork the repository** and clone it to your account.
2. **Create a new branch:**
   ```bash
   git checkout -b new-feature
   ```
3. **Make your changes and commit:**
   ```bash
   git commit -m "Added new feature"
   ```
4. **Push to GitHub:**
   ```bash
   git push origin new-feature
   ```
5. **Create a pull request.**
