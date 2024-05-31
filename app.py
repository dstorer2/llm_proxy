import logging
from flask import Flask, request, jsonify
from litellm import completion
import os

app = Flask(__name__)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
CLARIFAI_API_KEY = os.getenv("ANTHROPIC_API_KEY")

logging.basicConfig(level=logging.INFO)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.json
    prompt = data.get('prompt', '')
    model = data.get('model', '')
    if not prompt:
        app.logger.error('No prompt provided')
        return jsonify({'error': 'No prompt provided'}), 400
    
    if model == 'openai':
        try:
            response = completion(
                model="gpt-3.5-turbo",
                messages=[{"content":prompt, "role": "user"}]
            )
            app.logger.info(f'OpenAI API response: {response}')
            generated_text = response['choices'][0]['message']['content']
            app.logger.info(f'Generated response: {generated_text}')
            return jsonify({'response': generated_text})
        except Exception as e:
            app.logger.error(f'Error generating response: {str(e)}')
            return jsonify({'error': str(e)}), 500
    elif model == 'claude':
        try:
            response = completion(
                model="clarifai/anthropic.completion.claude-v1",
                messages=[{"content": prompt, "role": "user"}],
                api_key=CLARIFAI_API_KEY
            )
            app.logger.info(f'Claude API response: {response}')
            generated_text = response['choices'][0]['message']['content']
            app.logger.info(f'Generated response: {generated_text}')
            return jsonify({'response': generated_text})
        except Exception as e:
            app.logger.error(f'Error generating response: {str(e)}')
            return jsonify({'error': str(e)}), 500
    else:
        app.logger.error('Invalid model specified')
        return jsonify({'error': 'Invalid model specified'}), 400

if __name__ == '__main__':
    app.run(debug=True)