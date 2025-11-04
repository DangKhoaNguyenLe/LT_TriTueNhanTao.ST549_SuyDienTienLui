

def check_DieuKien(dieuKien, DuKien, rules):

    if isinstance(dieuKien, str):
        return suyDienLui(dieuKien, DuKien, rules)
    if isinstance(dieuKien, dict):
        if "and" in dieuKien:
            dieuKienCon = dieuKien["and"]
            return all(check_DieuKien(c, DuKien, rules) for c in dieuKienCon)
        
        if "or" in dieuKien:
            dieuKienCon = dieuKien["or"]
            return any(check_DieuKien(c, DuKien, rules) for c in dieuKienCon)

    return False


def suyDienLui(goal, DuKien, rules):
    if goal in DuKien:
        return True
    for rule in rules:
        if rule["then"] == goal:
            dieuKien = rule["if"]
            if check_DieuKien(dieuKien, DuKien, rules):
                return True
    return False