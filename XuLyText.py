import re

def chuyenDoi(text):
    text = text.strip().replace("?", "").replace(".", "")
    danghoi = [" có phải đó ", " có phải "]
    fact_part = text
    goal_part = ""
    

    for sep in danghoi:
        if sep in text:
            parts = text.split(sep, 1) 
            fact_part = parts[0].strip()
            goal_part = parts[1].strip()
                

            if goal_part.endswith(" không"):
                goal_part = goal_part[:-6].strip()
            elif goal_part.endswith(" ko"):
                goal_part = goal_part[:-3].strip()
            break 
    
    facts = re.split(r"\s+và\s+|\s+của\s+|\s+hoặc\s+|,", fact_part)
    facts = [f.strip() for f in facts if f.strip()]
    return facts, goal_part