import PyPDF2
import spacy

nlp = spacy.load("en_core_web_sm")

def process_document(file):

    text = ""

    if file.filename.endswith(".pdf"):

        reader = PyPDF2.PdfReader(file)

        for page in reader.pages:
            text += page.extract_text()

    else:
        text = file.read().decode("utf-8", errors="ignore")

    doc = nlp(text)

    summary = " ".join([sent.text for sent in list(doc.sents)[:3]])

    keywords = list(set(
        token.text for token in doc
        if token.pos_ in ["NOUN","PROPN"] and not token.is_stop
    ))[:10]

    return summary, keywords