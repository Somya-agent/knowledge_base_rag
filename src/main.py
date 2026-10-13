import argparse
from urllib import response

import requests
from openai import OpenAI

from flow import fetch_url


def main() -> None:
    #Run ollama serve in terminal first
    #ollama pull gpt-oss:120b-cloud
    response = requests.get("http://localhost:11434", timeout=5)
    response.raise_for_status()
    print(response.text)

    Ollama_base_url = "http://localhost:11434/v1"

    ollama = OpenAI(base_url=Ollama_base_url, api_key="ollama")

    response = ollama.chat.completions.create(
        model="gpt-oss:120b-cloud",
        messages=[
            {"role": "user", 
             "content": "What is the capital of France?"}
        ]
    )
    print(response.choices[0].message.content)

    response = ollama.chat.completions.create(
        model="gpt-oss:120b-cloud",
        messages=[
            {"role": "user", 
             "content": "Tell me a joke about programming."}
        ]
    )
    print(response.choices[0].message.content)

    

if __name__ == "__main__":
    main()