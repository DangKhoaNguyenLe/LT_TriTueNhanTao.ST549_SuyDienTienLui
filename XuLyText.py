import re

def chuyenDoi(text):
    text = text.lower().strip().replace("?", "").replace(".", "")
    fact_part = ""
    goal_part = ""

    match = re.search(r"^(.*)\b(có bị|có phải)\b(.*)\b(không)$", text)
    
    if match:
        fact_part = match.group(1).strip()
        goal_part = match.group(3).strip()
    else:
        parts = re.split(r"\b(muốn|để|thì|nhằm|mong|hi vọng|nên|cần)\b", text)
        if len(parts) < 3:
            fact_part = text
        else:
            fact_part = parts[0].strip() 
            goal_part = (parts[-2] + parts[-1]).strip()
    fact_stop_words = r"\b(tôi|bị|bi|là|có|đang)\b"
    fact_part = re.sub(fact_stop_words, "", fact_part).strip()
    raw_facts = re.split(r"\s+và\s+|\s+hoặc\s+|\s*,\s*", fact_part)
    facts = []
    for f in raw_facts:
        f_clean = f.strip()
        if f_clean:
            facts.append(re.sub(r"\s+", " ", f_clean))
    goal = ""
    if goal_part:
        goal_stop_words = r"\b(tôi|muốn|được|hãy|thì|sẽ|phải|ko|không|bị|phải|nên|cần)\b" 
        goal = re.sub(goal_stop_words, "", goal_part).strip()
        goal = re.sub(r"\s+", " ", goal).strip().strip(' ')

    return facts, goal
