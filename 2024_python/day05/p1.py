
def check_after(value: int, rules: list[tuple[int, int]], after: list[int]):
    if after == []:
        return True
    for rule in rules:
        for check_value in after:
            if value == rule[1] and check_value == rule[0]:
                return False
    return True


def check_before(value: int, rules: list[tuple[int, int]], before: list[int]):
    if before == []:
        return True
    for rule in rules:
        for check_value in before:
            if value == rule[0] and check_value == rule[1]:
                return False
    return True


def find_middle(updates: list):
    middle = len(updates) // 2
    return updates[middle]


def apply_rules(rules: list[tuple[int, int]], updates: list[list[int]]) -> int:
    score: int = 0
    for update_list in updates:
        valid = True
        for i, update in enumerate(update_list):
            after = update_list[i + 1:]
            before = update_list[:i]
            if not (check_after(update, rules, after) and check_before(update, rules, before)):
                valid = False
                break
        if valid:
            score += find_middle(update_list)
    return score


def read_rules(rules: str) -> list[tuple]:
    rules_list = rules.splitlines()
    parsed_rules = []
    for rule in rules_list:
        front, back = rule.split("|")
        parsed_rules.append((int(front), int(back)))
    return parsed_rules


def main(data):
    rules, updates = data.split("\n\n")
    updates = updates.splitlines()
    updates = [list(map(int, x.split(","))) for x in updates]
    parsed_rules = read_rules(rules)
    score = apply_rules(parsed_rules, updates)
    return score
