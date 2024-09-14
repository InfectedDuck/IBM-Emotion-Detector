# Emotion Detection System

## Overview
The **Emotion Detection System** is an NLP-powered web application built using Flask that analyzes and detects emotions in user-provided text. By leveraging Watson's advanced NLP capabilities, the system identifies emotions like anger, joy, fear, sadness, and disgust, presenting a dominant emotion as part of the analysis.

## Key Features
* **Emotion Analysis**: Utilizes IBM Watson's NLP API to predict emotions in a given text.
* **Real-Time Web Interface**: Built with Flask and Bootstrap for a responsive and user-friendly UI.
* **Comprehensive Emotion Breakdown**: Provides insights into five emotions: anger, disgust, fear, joy, and sadness, with a dominant emotion for clarity.
* **Unit Testing**: Ensures accurate emotion detection using well-structured test cases in Python's `unittest`.
* **Modular Design**: The project structure supports easy integration of future features and upgrades.

## Technologies Used
* **Flask**: Backend framework to handle requests and render the web pages.
* **IBM Watson API**: Provides the core NLP and emotion detection capabilities.
* **Bootstrap 4**: Used for the front-end design and layout.
* **unittest**: For automated testing to validate the emotion detection logic.

## How It Works
1. **Input**: Users enter text they wish to analyze on the web interface.
2. **Backend Processing**: The text is sent to the Watson API, where NLP algorithms process the input and predict emotional content.
3. **Output**: The system returns the analysis with the emotion breakdown, showing values for anger, disgust, fear, joy, sadness, and the dominant emotion.

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/InfectedDuck/emotion-detection-system.git
    cd emotion-detection-system
    ```

2. **Install Dependencies**:
    Ensure you have `Python 3.7+` and `pip` installed.
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the Flask App**:
    ```bash
    python app.py
    ```

4. **Run Unit Tests**:
    ```bash
    python -m unittest discover -s tests
    ```

## Usage
Once the app is running, open your browser and visit `http://localhost:5000`. Enter a text to analyze, and the system will return an emotion breakdown along with the dominant emotion.

## Example
**Input**: *"I am really happy today!"*

**Output**: *For the given statement, the system response is 'anger': 0, 'disgust': 0, 'fear': 0, 'joy': 0.95, and 'sadness': 0. The dominant emotion is 'joy'.*
## Testing
The project comes with a suite of unit tests to ensure reliability:
* **Emotion-based Unit Tests**: Verifies if the correct dominant emotion is returned for various inputs.
    * Glad, Mad, Disgusted, Sad, and Afraid statements are tested.

To run the tests:
```bash
python -m unittest discover
```

## License
This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for details. <br>
This project is made as a part of IBM Course.
