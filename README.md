Alterbrain
==========

This project is a simple chatbot built using Flask, OpenAI API, and AWS Comprehend. The chatbot generates responses to user input based on a pre-set context and sentiment analysis using AWS Comprehend.

Prerequisites
-------------

Before running this project, you need to install the following:

-   Python 3.6 or higher
-   Flask
-   OpenAI API
-   AWS SDK for Python (Boto3)
-   Dotenv

Installation
------------

To install the required packages, run the following command:

Copy code

`pip install -r requirements.txt`

Setup
-----

Before running the code, you need to set up the following environment variables:

-   `OPENAI_API_KEY`: Your OpenAI API key.
-   `AWS_ACCESS_KEY_ID`: Your AWS access key ID.
-   `AWS_SECRET_ACCESS_KEY`: Your AWS secret access key.
-   `REGION_NAME`: The AWS region name where you want to use Comprehend.

You can set these variables in a `.env` file at the root of the project.

Usage
-----

To start the server, run the following command:

Copy code

`python app.py`

This will start a Flask server at `http://localhost:5000`.

To interact with the chatbot, send a POST request to `http://localhost:5000/alterbrain` with a JSON payload containing a `message` field that represents the user input. The server will return a JSON response containing a `response` field that represents the chatbot's response to the input.

License
-------

This project is licensed under the MIT License. See the LICENSE file for details.
