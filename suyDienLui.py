def check_DieuKien(goal, facts, rules, ruleCheck):
    if isinstance(goal, str):
        return suyDienLui(goal, facts, rules, ruleCheck)
    if isinstance(goal, dict):
        if "and" in goal:
            return all(check_DieuKien(c, facts, rules, ruleCheck) for c in goal["and"])
        if "or" in goal:
            return any(check_DieuKien(c, facts, rules, ruleCheck) for c in goal["or"])
    return False


def suyDienLui(goal, facts, rules, ruleCheck=None):
    if ruleCheck is None:
        ruleCheck = set()
    if goal in facts:
        return True
    if goal in ruleCheck:
        return False
    ruleCheck.add(goal)

    for rule in rules:
        if rule["then"] == goal:
            tmp = rule["if"]
            if check_DieuKien(tmp, facts, rules, ruleCheck):
                return True
    return False