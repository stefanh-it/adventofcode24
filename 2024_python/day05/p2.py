
def main(data):
    rules, updates = data.split("\n\n")
    updates = updates.splitlines()
    updates = [list(map(int, x.split(","))) for x in updates]
    parsed_rules = read_rules(rules)
    score = apply_rules(parsed_rules, updates)
    return score

