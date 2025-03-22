import json
from rapidfuzz import process

def load_dictionary(file_path='dictionary.json'):
    with open(file_path, 'r') as file:
        return json.load(file)

def fuzzy_search(word, dictionary):
    words = list(dictionary.keys())
    # Perform fuzzy matching
    matches = process.extract(word, words, limit=3)
    best_match = max(matches, key=lambda x: x[1])

    if best_match[1] == 100:
        return {"match": best_match[0], "meaning": dictionary[best_match[0]]}
    else:
        suggestions = [match[0] for match in matches]
        return {"suggestions": suggestions}
