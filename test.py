from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-6-6"
)

text = """
Artificial Intelligence is transforming industries worldwide.
It automates repetitive tasks, improves decision-making,
and helps organizations become more productive.
"""

summary = summarizer(text)

print(summary[0]["summary_text"])