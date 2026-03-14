import json
import random
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

with open("data/intents.json") as f:
    intents = json.load(f)

patterns = []
responses = []

for intent in intents["intents"]:
    for p in intent["patterns"]:
        patterns.append(p)
        responses.append(intent["responses"])

pattern_embeddings = model.encode(patterns)


def get_bot_response(user_input, document_text=""):

    user_embedding = model.encode(user_input)

    scores = util.cos_sim(user_embedding, pattern_embeddings)[0]

    best_index = scores.argmax()

    if scores[best_index] > 0.5:
        return random.choice(responses[best_index])

    if document_text:
        return "Based on uploaded document: " + document_text[:200]

    return "I am not sure about that. Please contact the department."