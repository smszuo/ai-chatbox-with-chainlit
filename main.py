import re

import chainlit as cl
from openai import OpenAI

client = OpenAI()

@cl.on_message
async def main(message: cl.Message):
    response_id = cl.user_session.get("response_id")
    response = client.responses.create(
        model = "gpt-4o",
        input = message.content,
        previous_response_id = response_id
    )
    cl.user_session.set("response_id", response.id)
    await cl.Message(
        content=f"Assistant: {response.output_text}",
    ).send()