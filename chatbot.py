import gradio as gr

disclaimer = """
📌 **AmbujBot - Professional Resume Chatbot**

🔹 This is a demo chatbot representing **Ambuj Tripathi**.
🔹 Please wait 25–30 seconds after opening — the bot is warming up.
🔹 This session is temporary — refreshing will reset the chat.
🔹 For interview or hiring inquiries, please contact Ambuj on Naukri or LinkedIn.
"""

def ambuj_response(message, history):
    msg = message.lower().strip()

    # Resume / Interview related
    if "experience" in msg:
        return "I have over 4 years of experience in telecom and recently transitioned into the AI domain."
    elif "tools" in msg or "software" in msg:
        return "I’ve worked with Amanda Tool, Piper Tool, Jupyter Lab, and Optical Fiber Communication systems."
    elif "certification" in msg or "course" in msg:
        return "I hold certifications from Google Cloud and Microsoft in Prompt Engineering, Gemini APIs, and Vertex AI."
    elif "projects" in msg:
        return "I’ve built AI avatar videos, explainer bots, and chatbot apps deployed for social platforms and portfolios."
    elif "resume" in msg:
        return "This bot is built to give a walkthrough of my resume. Please ask anything specific you'd like to know!"
    elif "contact" in msg or "hire" in msg or "interview" in msg:
        return "Thanks for showing interest! You can contact Ambuj Tripathi directly via LinkedIn or Naukri profile."

    # Casual normal conversation
    elif "hello" in msg or "hi" in msg:
        return "Hello! I’m AmbujBot — your virtual assistant. Ask me anything about Ambuj’s experience or certifications."
    elif "how are you" in msg:
        return "I'm doing well! Always ready to support with resume or interview questions. How can I assist you today?"

    # Handling offensive / irrelevant inputs
    elif any(word in msg for word in ["fuck", "abuse", "nonsense", "idiot", "chutiya", "mad"]):
        return "I'm here to assist professionally. Please keep your queries interview or resume-related."
    elif len(msg) < 3:
        return "Please enter a valid question related to resume or interview."
    else:
        return "I'm not trained for that yet. Please ask about Ambuj’s resume, skills, certifications or experience."

# Interface setup
gr.ChatInterface(
    ambuj_response,
    title="🤖 Chat with AmbujBot - Resume AI",
    description=disclaimer,
    theme="soft",
    examples=[
        ["Tell me about your experience."],
        ["Which tools have you used?"],
        ["What certifications do you have?"],
        ["Can I contact you for an interview?"],
        ["Hi!"],
        ["How are you?"]
    ],
    clear_on_submit=True
).launch()