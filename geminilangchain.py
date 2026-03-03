from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model

model = init_chat_model("gemini-2.5-flash", model_provider="google_genai")

result = model.invoke("what is hugging face in AI?  explain in few words")
print(result.content)