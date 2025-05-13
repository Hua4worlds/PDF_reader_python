from pypdf import PdfReader
import pyttsx3


def pdf_to_speech(pdf_path):
    # Initialize text-to-speech engine
    engine = pyttsx3.init()

    # Load PDF
    reader = PdfReader(pdf_path)
    text = ""

    # Extract text from each page
    for page_num, page in enumerate(reader.pages):
        page_text = page.extract_text()
        if page_text:
            text += page_text + "\n"
        else:
            print(f"Warning: No text found on page {page_num + 1}")

    if not text.strip():
        print("No readable text found in the PDF.")
        return

    # Read aloud
    engine.say(text)
    engine.runAndWait()


# Replace with your PDF file path (relative)
pdf_path = r"..\..\User\Downloads\example.pdf"
pdf_to_speech(pdf_path)