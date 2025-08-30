import os
from openai import OpenAI

key = "sk-proj-Z2LyRRO9edCw3Ha8yKUVpNI6rYrbAaepbwbYfPEsClPvOW1ebNKluZwSHWDakTQaObfUugT3BlbkFJZ4h0-JQaqXMMH4ixTUA9kDf1LQlfzWHbV76AtG2-c7nLKDuBHzeZdSe0p-Sdn4m00xwM2s4-AA"

messages = []

client = OpenAI(api_key=key)

def completion(message):
    global messages
    messages.append({
        "role": "user",
        "content": message
    })
    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-4o"
    )
    response = {
        "role": "assistant",
        "content": chat_completion.choices[0].message.content
    }
    messages.append(response)
    print(f"Jarvis: {response['content']}")

if __name__ == "__main__":
    user_question = input("Jarvis :Hi I am Jarvis, How may I help you\n")
    completion(user_question)
