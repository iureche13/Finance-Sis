def calculate_score(scores):
    score = 0
    score += scores['urgency'] * 2.5
    score += scores['guarantee'] * 1.5
    score += scores['payment'] * 2.0
    for category in scores:
        if category not in ['urgency', 'guarantee', 'payment']:
            score += scores[category] # other hits
    return min(100, (score * 10))

def keyword_score(search_words, text):
    flags = []
    text = text.lower()
    scores = {}
    categories = list(search_words.keys())
    matched_phrases = {}
    for category in categories:
        matches = [k for k in search_words[category] if k in text]
        scores[category] = len(matches)
        matched_phrases[category] = matches
        matches = list({k for k in search_words[category] if k in text})
        for match in matches:
            flags.append(match)
    max_category = max(scores, key=scores.get)
    return calculate_score(scores), max_category, flags