init python:
    import os
    import random
    import requests
    import ollama
    import httpx

    class TextModel:


        def getLLM(self, prompt):
            seed = random.random() if persistent.seed == "random" else persistent.seed 

            options = ollama.Options(temperature=float(f".{persistent.temp}"), stop=["[INST", "[/INST", "[END]"],
            num_ctx=int(persistent.context_window), seed=seed, num_predict=200)

            try:
                response = ollama.chat(model=persistent.chatModel, messages=prompt, options=options)
                result = response['message']['content']

                renpy.log(f"RAW RESPONSE: {result}")

                if "[END]" not in result:
                    return result.strip() + " [END]"
                return result.strip()

            except httpx.ConnectError:
                return False, "<|Error|> You don't have ollama running."
            except ollama.ResponseError as e:
                if e.status_code == 404:
                    return False, f"<|Error|> You dont have the model \"{persistent.chatModel}\" installed! Go to settings and install this model (if it exists)."
                return False, f"<|Error|> {e.error}"





        def getGroq(self, prompt):
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {persistent.chatToken}"
            }
            payload = {
                "model": persistent.chatModel, # llama3-70b-8192, llama-3.1-70b-versatile
                "max_tokens": 200,
                "temperature": float(f".{persistent.temp}"),
                "stop": "[END]",
                "messages": prompt
            }

            response = requests.post(
                url="https://api.groq.com/openai/v1/chat/completions",
                headers=headers,
                json=payload
                )

            try:
                response.raise_for_status()
                data = response.json()
                result = data["choices"][0]["message"]["content"]

                renpy.log(f"RAW RESPONSE: {result}")

                if "[END]" not in result:
                    return result.strip() + " [END]"
                return  result.strip()

            except requests.exceptions.RequestException as e:
                return False, f"<|Error|> {e}"

        """
        def getGroq(self, prompt):
            import groq
            from groq import Groq
            
            client = Groq(api_key=persistent.chatToken)
            try:        
                response = client.chat.completions.create(
                    messages=prompt,
                    model=persistent.chatModel,
                    temperature=persistent.temp,
                    max_tokens=200,
                    stop="[END]",
                    stream=False,
                )
                result = response.choices[0].message.content
                if "[END]" not in result:
                    return result.strip() + " [END]"
                return result.strip()
            except groq.APIConnectionError as e:
                return False, "<|Error|> Your wifi isn't on"
            except groq.RateLimitError as e:
                return False, "<|Error|> You're being ratelimited, come back another time."
            except groq.APIStatusError as e:
                return False, f"<|Error|> The model \"{persistent.chatModel}\" is not recognized OR something else is wrong."

        """
