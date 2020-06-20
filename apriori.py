from efficient_apriori import apriori
import re
class Apriori :
    def __init__(self, known_transactions):
        self.known_transactions = known_transactions

    def get_rules(self):
        itemsets, rules = apriori(self.known_transactions, min_support=0.1, min_confidence=1)
        antecedents = []
        consequents = []
        for i in range(0, len(rules)):
            rule = rules[i]
            antecedent = re.search('{(.+?)}', str(rule))
            consequent = re.search('-> {(.+?)}', str(rule))
            antecedents.append(antecedent.group(1).split(", "))
            consequents.append(consequent.group(1).split(", "))
        return antecedents, consequents
