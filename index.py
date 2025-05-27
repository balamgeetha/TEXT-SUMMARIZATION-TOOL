from transformers import pipeline


def summarize_text(text, max_length=130, min_length=30, do_sample=False):
    # Load the summarization pipeline
    summarizer = pipeline("summarization")

    # Generate summary
    summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=do_sample)

    # Return the summarized text
    return summary[0]['summary_text']


if __name__ == "__main__":
    print("🔹 Welcome to the Text Summarization Tool 🔹\n")

    # Input: Paste a long article or text
    input_text = input("📥 Enter the long article or paragraph:\n\n")

    # Summarize and display the result
    print("\n⏳ Summarizing...\n")
    summary_result = summarize_text(input_text)

    print("✅ Summary:\n")
    print(summary_result)

