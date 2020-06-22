import re
from random import randint
from efficient_apriori import apriori


class Apriori :
    def __init__(self, known_transactions):
        self.known_transactions = known_transactions
        self.antecedents = []
        self.consequents = []

    def get_rules(self):
        itemsets, rules = apriori(self.known_transactions, min_support=0.1, min_confidence=1)
        for i in range(0, len(rules)):
            rule = rules[i]
            antecedent = re.search('{(.+?)}', str(rule))
            consequent = re.search('-> {(.+?)}', str(rule))
            self.antecedents.append(antecedent.group(1).split(", "))
            self.consequents.append(consequent.group(1).split(", "))
        return self.antecedents, self.consequents

    # returns the number of common elements between two arrays
    def __count(self, tab1, tab2):
        count = 0
        for i in range(0, len(tab1)):
            for j in range(0, len(tab2)):
                if tab1[i] == tab2[j] :
                    count+=1
        return count

    # returns the index of the array which contains the most common elements
    def __search_index(self, tab1, tab2):
        index = randint(0, len(tab1)-1)
        nbr_common_elements = 0
        for i in range(0, len(tab1)):
            nbr = self.__count(tab1[i], tab2)
            if(nbr > nbr_common_elements) :
                nbr_common_elements = nbr
                index = i
        return index

    # returns the choice of the apriori algorithm
    def choice_apriori(self, known_objects, choices):
        index = self.__search_index(self.antecedents, known_objects)
        choice = self.__search_index(choices, self.consequents[index])
        return choice
