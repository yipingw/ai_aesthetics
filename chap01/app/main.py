from fastapi import FastAPI
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
import json

app = FastAPI()

# notice: replace <PUT_YOUR_OPENAI_API_KEY_HERE> to your API Key
os.environ["OPENAI_API_KEY"] = '<PUT_YOUR_OPENAI_API_KEY_HERE>'


COMPLETION_MODEL = "text-davinci-003"

prompt = """
Consideration product : LEGO Star Wars 2023 Advent Calendar 75366 Christmas Holiday Countdown Gift Idea with 9 Star Wars Characters and 15 Mini Building Toys,
Discover New Experiences and Daily Collectible Surprises
1. Refine the product title, keeping the text within 15 words..
2. Provide 8 selling points for this product in Amazon.
3. Describe this product's information in Amazon..
Output the result in json format with three properties: title, selling_points and information.
"""


def get_response(prompt):
    completions = client.completions.create(engine=COMPLETION_MODEL,
    prompt=prompt,
    max_tokens=512,
    n=1,
    stop=None,
    temperature=0.0)
    message = completions.choices[0].text
    return message


@app.get("/")
def read_root():
    return {"message": json.loads(get_response(prompt))}
