import google.generativeai as genai

GOOGLE_API_KEY = "AIzaSyAVAAJjR0j_wnUGPFTSbfqBfWvnJsDTXyg"
genai.configure(api_key=GOOGLE_API_KEY)

print("Список доступних моделей:")
for m in genai.list_models():
    if 'generateContent' in m.supported_generation_methods:
        print(m.name)