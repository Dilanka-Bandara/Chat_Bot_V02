import google.generativeai as genai

# ✅ Add your actual key here
genai.configure(api_key="AIzaSyAaBsxnsbJkVqpbpMpBAtpMAvHP6BO2G1Y")

# ✅ Use correct model name
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")
chat = model.start_chat()

print("Welcome to Gemini Chatbot!")
print("Ask anything. Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    try:
        response = chat.send_message(user_input)
        print("Gemini:", response.text)
    except Exception as e:
        print("⚠️ Error:", e)
