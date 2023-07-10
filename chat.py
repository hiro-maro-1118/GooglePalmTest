# Copyright 2023 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START aiplatform_sdk_chat]
from vertexai.preview.language_models import ChatModel, InputOutputTextPair
from flask import Flask,render_template,request,jsonify

app = Flask(__name__)

def science_tutoring(user_message,temperature: float = 0.2) -> None:
    chat_model = ChatModel.from_pretrained("chat-bison@001")

    # TODO developer - override these parameters as needed:
    parameters = {
        "temperature": temperature,  # Temperature controls the degree of randomness in token selection.
        "max_output_tokens": 256,  # Token limit determines the maximum amount of text output.
        "top_p": 0.95,  # Tokens are selected from most probable to least until the sum of their probabilities equals the top_p value.
        "top_k": 40,  # A top_k of 1 means the selected token is the most probable among all tokens.
    }

    # chat = chat_model.start_chat(
    #     context="My name is Miles. You are an astronomer, knowledgeable about the solar system.",
    #     examples=[
    #         InputOutputTextPair(
    #             input_text="How many moons does Mars have?",
    #             output_text="The planet Mars has two moons, Phobos and Deimos.",
    #         ),
    #     ],
    # )

    chat = chat_model.start_chat(
        context="My name is Miles. You are an individual with abundant business ideas and a strong knowledge of business.",
        examples=[
            InputOutputTextPair(
                input_text = "Please tell me how to develop future business ideas based on the latest technology trends and market demand.",
                output_text = "It is important to thoroughly research the latest technology trends and market demand, and develop new products or services based on them. Additionally, by gathering customer feedback and analyzing competitors, you can generate sustainable and differentiated business ideas. Furthermore, it is crucial to articulate the ideas into concrete business plans and adopt strategic marketing approaches that consider market needs and competitive landscape.",
            ),
            InputOutputTextPair(
                input_text = "Please advise on effective strategies for entering new markets.",
                output_text = "When entering a new market, start by conducting market research and analyzing target customers and competitors. Then, clarify your company's strengths and unique selling points, and provide products or services that meet customer needs. Additionally, consider competitive pricing and deploy effective marketing campaigns to facilitate market entry. Also, explore strategic initiatives suitable for the market environment, such as partnerships and establishing distribution channels.",
            ),
        ],
    )

    response = chat.send_message(
        # "How many planets are there in the solar system?", **parameters
        user_message, **parameters
    )

    print(f"Response from Model: {response.text}")
    # [END aiplatform_sdk_chat]

    return response.text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_message', methods=['POST'])
def process_message():
    user_message = request.json.get('message')

    # Call the science_tutoring function with the user message
    bot_response = science_tutoring(user_message)

    # Return the bot response as a JSON object
    return jsonify({'response': bot_response})

if __name__ == "__main__":
    app.run()