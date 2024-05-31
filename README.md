# LLM Proxy App

This project provides a simple Flask web application that serves as a proxy to generate text completions using different language models, including OpenAI's GPT-3.5-turbo and Anthropic's Claude.

## Project Structure
    .
    ├── app.py
    ├── test_proxy.py
    ├── .env
    ├── requirements.txt
    └── README.md

## Requirements
    Python 3.6+
    pip (Python package installer)

## Setup

### 1. Clone the repository:
        git clone <repository-url>
        cd <repository-directory>

### 2. Create a virtual environment:
        python -m venv llm_proxy_env

### 3. Activate the virtual environment:
        On Windows:
            llm_proxy_env\Scripts\activate

        On macOS and Linux:
            source llm_proxy_env/bin/activate

### 4. Install dependencies:
        pip install -r requirements.txt

### 5. Create a .env file in the root directory and add your API keys:
        OPENAI_API_KEY=your_openai_api_key_here
        ANTHROPIC_API_KEY=your_anthropic_api_key_here

## Running the Application
### 1. Start the Flask app:
        In the virtual environmnet, run the app script:
        py app.py

### 2. Test the proxy:
        Open a new terminal window, activate the virtual environment, and run the test script:
        py test_proxy.py

## Files
    app.py
    This file contains the Flask application which defines an endpoint to generate text completions using OpenAI and Claude models.

    test_proxy.py
    This file contains a test script to send a request to the Flask app and print the generated response.

## Dependencies
    Listed in the requirements.txt file
    Install them with: pip install -r requirements.txt
