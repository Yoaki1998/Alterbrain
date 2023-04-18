import openai
from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
import boto3

# Load environment variables
load_dotenv()

# Set OpenAI credentials
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
context = "From now on I will address you as if your name is Nemuri and please answer as such."
emotion = ""

# Set AWS credentials
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key = os.getenv("AWS_SECRET_ACCESS_KEY")
region_name = os.getenv("REGION_NAME")

# Call AWS Comprehend to generate sentiment for a input text 
def get_sentiment(text):
    comprehend = boto3.client(
        service_name='comprehend',
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        region_name=region_name
    )
    response = comprehend.detect_sentiment(Text=text, LanguageCode='en')
    print(response['Sentiment'])
    return response['Sentiment']

# Call OpenAI API to generate response
def generate_response(message):

    # Use the global context variable
    global context 
    global emotion

    match get_sentiment(message):
        case "POSITIVE" :
            emotion = "very kind"
        case "NEGATIVE":
            emotion = "sassy"
        case "NEUTRAL":
            emotion = "emotionally neutral"
        case "MIXED":
            emotion = "confused"



    # Construct messages with context and user input
    messages= [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "assistant", "content": context},
    {"role": "user", "content": f"Be {emotion} in your response. {message}" }
    ]

    # Call OpenAI API to generate response
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages= messages,
        temperature=0.7,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    
    print(messages[2])

    # Update context with new conversation history
    context += "\n"+ message + "\n" + response.choices[0].message.content
    print(context)

    return response.choices[0].message



@app.route("/alterbrain", methods=["POST"])
def alterbrain():
    message = request.json["message"]
    response = generate_response(message).content
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)

