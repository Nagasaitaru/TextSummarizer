from transformers import pipeline

summarizer = pipeline(
    "summarization",
    model="sshleifer/distilbart-cnn-6-6"
)

def generate_summary(text):
    words = text.split()

    # Split large text into chunks
    chunk_size = 800
    chunks = []

    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i + chunk_size]))

    summaries = []

    for chunk in chunks:
        result = summarizer(
            chunk,
            max_length=700,   # Increase for longer summaries
            min_length=500,   # Forces more detailed output
            do_sample=False
        )

        summaries.append(result[0]["summary_text"])

    return "\n\n".join(summaries)