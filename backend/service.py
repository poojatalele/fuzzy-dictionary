import json
from difflib import get_close_matches

# Load dictionary data
def load_dictionary(file_path='dictionary.json'):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading dictionary: {e}")
        return {}

dictionary_data = load_dictionary()

# Search Logic
def search_word(word):
    word = word.strip().lower()

    # Exact match check
    if word in dictionary_data:
        return {"type": "exact", "result": f"Exact match found: {word} - {dictionary_data[word]}"}

    # Fuzzy search using difflib
    matches = get_close_matches(word, dictionary_data.keys(), n=3, cutoff=0.6)
    if matches:
        return {"type": "suggestion", "suggestions": matches}
    
    return {"type": "no_match", "result": "No match found."}
