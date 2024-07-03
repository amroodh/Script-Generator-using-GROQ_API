#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
import os
import pandas as pd
import streamlit as st
from groq import Groq
import random
from evaluate_script import evaluate_script, generate_pdf

# Set the API key directly in the script
os.environ["GROQ_API_KEY"] = "YOUR-GROQ-API-KEY"  # Replace with your actual API key

# Initialize Groq client
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

# Load the dataset
file_path = 'dataset.csv'  # Update with the correct path if needed
dataset = pd.read_csv(file_path)

# Define a function to generate script using Groq API
def generate_script(prompt):
    chat_completion = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": prompt
        }],
        model="llama3-8b-8192",
    )
    return chat_completion.choices[0].message.content

# Define the initial few-shot prompt with examples from the dataset
few_shot_prompt = """
### Example 1:
Date: 05/04/2024
Reference URL: https://www.instagram.com/reel/C5Gj8oMrOkd/?igshid=YmMyMTA2M2Y=
Hook: Multiple big creators stole my content and got millions of views.
Build Up: Multiple big creators stole my content and got millions of views because they have a larger audience and more reach.
Body: Multiple big creators stole my content and got millions of views, but I'm here to tell you that originality and creativity still matter.
CTA: Comment PB below if you want me to send you a free guide on how to protect your content.

### Example 2:
Date: 21/04/2024
Reference URL: https://www.instagram.com/reel/C5_wpqASpXA/?igshid=YmMyMTA2M2Y=
Hook: Can you follow MrBeast on TikTok? Comment the answer below.
Build Up: This is the secret to how the biggest creators grow their audience on TikTok.
Body: Can you follow MrBeast on TikTok? Comment the answer below and I'll share the strategies he uses to gain millions of followers.
CTA: So comment down below CTA if you want it.

### Example 3:
Date: 17/05/2024
Reference URL: https://www.instagram.com/reel/CxsrdLjuoO5/?igshid=YmMyMTA2M2Y=
Hook: "My name is Devin Jatto and as a social media strategist, I'm here to help you grow."
Build Up: "First, you need to get clear on what you're aiming for."
Body: "Within the niche of fitness you're creating 80% educational content and 20% motivational content."
CTA: "At the end of these 30 days sort your videos based on engagement and see what's working."

### Generate a new script based on the provided topic.
Date: {new_date}
Reference URL: {new_url}
Hook: {new_hook}
Build Up: {new_build_up}
Body: {new_body}
CTA: {new_cta}
"""

# Define extensive variations for each part of the script
hook_variations = [
    "Learn the secrets to {}.",
    "Discover how {} can change your life.",
    "Unlock the potential of {}.",
    "Master the art of {}.",
    "Explore the world of {} and find out what you've been missing.",
    "Dive deep into {} and uncover hidden gems.",
    "Gain insights on {} and take your skills to the next level."
]

build_up_variations = [
    "It's all about understanding {} and delivering value.",
    "The key to {} is knowing your audience.",
    "With {}, you can achieve greatness.",
    "Success in {} requires dedication and effort.",
    "Understanding {} can give you a competitive edge.",
    "Harness the power of {} to transform your approach.",
    "By focusing on {}, you can unlock new opportunities."
]

body_variations = [
    "Focus on creating content that resonates with {} and keeps them engaged.",
    "Engage your audience by delivering top-notch {} content.",
    "Make your {} content stand out by being unique and authentic.",
    "Captivate your audience with compelling {} content.",
    "Consistency is key in {}. Keep your audience hooked with regular updates.",
    "Deliver valuable {} content that addresses your audience's needs.",
    "Innovate and experiment with {} to keep your content fresh and exciting."
]

cta_variations = [
    "Comment below if you want more tips on {}.",
    "Let me know if you need more insights on {}.",
    "Reach out for more strategies on {}.",
    "Connect with me for more advice on {}.",
    "Don't hesitate to ask questions about {} in the comments.",
    "Share your thoughts on {} and let's discuss.",
    "Follow for more updates on {} and other exciting topics."
]

# Predefined true scripts for comparison (examples)
true_scripts = [
    "Learn the secrets to successful content creation. It's all about understanding your audience and delivering value. Focus on creating content that resonates with your audience and keeps them engaged. Comment below if you want more tips on content creation.",
    "Discover how social media marketing can change your life. The key to success in social media marketing is knowing your audience. Engage your audience by delivering top-notch content. Let me know if you need more insights on social media marketing.",
    "Unlock the potential of content creation. It's all about delivering value to your audience. Make your content stand out by being unique and authentic. Reach out for more strategies on content creation."
]

# Streamlit application
st.title("Script Generator")

# Input for the topic
topic = st.text_input("Enter a topic:")
if st.button("Generate Script"):
    new_date = "20/05/2024"
    new_url = "https://www.example.com/new-script"
    new_hook = random.choice(hook_variations).format(topic)
    new_build_up = random.choice(build_up_variations).format(topic)
    new_body = random.choice(body_variations).format(topic)
    new_cta = random.choice(cta_variations).format(topic)

    # Format the prompt with the new script details
    formatted_prompt = few_shot_prompt.format(
        new_date=new_date,
        new_url=new_url,
        new_hook=new_hook,
        new_build_up=new_build_up,
        new_body=new_body,
        new_cta=new_cta
    )

    # Generate the script
    generated_script = generate_script(formatted_prompt)
    st.write("### Generated Script")
    st.write(generated_script)

    # Evaluate the generated script and generate PDF
    f1, precision, recall, true_positives, false_positives = evaluate_script(true_scripts, generated_script)
    st.write(f"F1 Score: {f1}")
    st.write(f"Precision: {precision}")
    st.write(f"Recall: {recall}")
    st.write(f"True Positives: {true_positives}")
    st.write(f"False Positives: {false_positives}")

    # Generate PDF with evaluation metrics
    generate_pdf(generated_script, f1, precision, recall, true_positives, false_positives)
    st.write("Evaluation metrics have been saved to evaluation_metrics.pdf")
