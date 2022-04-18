import itertools

header = ["level", "lang", "tweets", "phd", "interviewed_well"]
table = [
        ["Senior", "Java", "no", "no", "False"],
        ["Senior", "Java", "no", "yes", "False"],
        ["Mid", "Python", "no", "no", "True"],
        ["Junior", "Python", "no", "no", "True"],
        ["Junior", "R", "yes", "no", "True"],
        ["Junior", "R", "yes", "yes", "False"],
        ["Mid", "R", "yes", "yes", "True"],
        ["Senior", "Python", "no", "no", "False"],
        ["Senior", "R", "yes", "no", "True"],
        ["Junior", "Python", "yes", "no", "True"],
        ["Senior", "Python", "yes", "yes", "True"],
        ["Mid", "Python", "no", "yes", "True"],
        ["Mid", "Java", "yes", "no", "True"],
        ["Junior", "Python", "no", "yes", "False"]
    ]

def prepend_attribute_label(table, header):
    for row in table:
        for i in range(len(row)):
            row[i] = header[i] + "=" + str(row[i])
prepend_attribute_label(table, header)
for row in table:
    print(row)
# why do this? if we represent each row as a set (unordered collection
# of unique values), as is we cannot distinguish between tweets and phd

# unsupervised learning
# there is no "special attribute" (class) we are trying to predict
# several algorithms
# looking associations, groups, trends/patterns/reduction, ...
# ARM (PA8)
# k means clustering (BONUS PA9)

# ARM notes
# recall: decision trees generate classification rules
# example: IF att1=val1 AND att2=val2 AND ... THEN class=label
# terminology
# LHS (left hand side) everything before the THEN
# RHS (right hand side) everything right the THEN
# with classifiation rules, the RHS to have only 1 "term"
# (attribute name/value pair) --> class/label pair
# ARM relaxes this constraint
# LHS has at least 1 term and the RHS at least 1 term
# an attribute can be used at most 1 time in the rule
# example: IF att1=val1 AND att2=val2 AND ... 
# THEN att10=val10 AND att11=val11 AND ...

# how to generate rules?
# brute force generate all possible combinations of attribute/values
# VERY computationally expensive
# we will use apriori algorithm... some initial notes
# 1. even the apriori tricks, still computationally expensive
# 2. apriori generates alot of rules, some of the are "weak"
# we need rule evaluation metrics
# 3. association does not imply causation

# our game plan for learning ARM/apriori
# 1. Intro to ARM lab (today): given rules interpret/evaluate them
# 2. Apriori lab (thursday): trace algorithm
# 3. PA8 starter code (next class)
# 4. finish PA8

# how to represent a rule a python?
# use dictionaries!!
# IF interviewed_well=False THEN tweets=no
rule1 = {"lhs": ["interviewed_well=False"], "rhs": ["tweets=no"]}
# task: create rule5
rule5 = {"lhs": ["phd=no", "tweets=yes"], "rhs": ["interviewed_well=True"]}

# utility function
def check_row_match(terms, row):
    # return 1 if all the terms are in the row
    # 0 otherwise
    for term in terms:
        if term not in row:
            return 0
    return 1

# lab task #2
def compute_rule_counts(rule, table):
    Nleft = Nright = Nboth = Ntotal = 0
    for row in table:
        Nleft += check_row_match(rule["lhs"], row)
        Nright += check_row_match(rule["rhs"], row)
        Nboth += check_row_match(rule["lhs"] + rule["rhs"], row)
        Ntotal += 1
    return Nleft, Nright, Nboth, Ntotal

Nleft, Nright, Nboth, Ntotal = compute_rule_counts(rule1, table)
print(Nleft, Nright, Nboth, Ntotal)

# lab task #3
def compute_rule_interestingness(rule, table):
    Nleft, Nright, Nboth, Ntotal = compute_rule_counts(rule, table)

    rule["confidence"] = Nboth / Nleft
    rule["support"] = Nboth / Ntotal
    rule["completeness"] = Nboth / Nright
    # NOTE: denominators could be 0

for rule in [rule1, rule5]:
    compute_rule_interestingness(rule, table)
    print(rule)

# set theory basics and implementation in Python
# set: an unordered collection with no duplicates
# there is a built in set type in python
transaction = ["apples", "apples", "coffee", "batteries"]
transaction_set = set(transaction)
print("set:", transaction_set)
# note there are no duplicates and order is lost
transaction = sorted(list(transaction_set))
print("list:", transaction)

# A union B: the set of all items in A or B or both
# A instersect B: the set of all items in both A and B
# there are both union() and intersection() from set type
# transaction_set.

# suppose we an LHS and an RHS (lists or sets)
# LHS intersect RHS should be empty set (0)
# LHS union RHS
# sorted(LHS + RHS) OR LHS.union(RHS)
# apriori needs union

# A is a subset of B if all the items in A are 
# also in B
# check_row_match(A, B) returns 1 if A is a subset of B

# powerset of A is the set of all subsets of A
# (including 0 and A itself)
# task: on paper, calculate the powerset of transaction
powerset = []
for i in range(0, len(transaction) + 1):
    # i is the size of the subsets
    powerset.extend(itertools.combinations(transaction, i))
print(powerset)

# intro to market basket analysis (MBA)
# associations between produces customers
# buy together
# IF {"milk=true", "sugar=true"} THEN {"eggs=true"}
# we are only interested in products purchased 
# (e.g. =true), not products not purchased (e.g. =false)
# shorthand, drop =true
# IF {"milk", "sugar"} THEN {"eggs"}
# {"milk", "sugar"} -> {"eggs"}
# terminology: 
# a row in our dataset is a "transaction"
# transactions are "itemsets"

# apriori lab

# PA8 starter code
transactions = [
 ["b", "c", "m"],
 ["b", "c", "e", "m", "s"],
 ["b"],
 ["c", "e", "s"],
 ["c"],
 ["b", "c", "s"],
 ["c", "e", "s"],
 ["c", "e"]
]

# NOTE: apriori lab task #1: find the set I
def compute_unique_values(table):
    unique = set()
    for row in table:
        for value in row: 
            unique.add(value)
    return sorted(list(unique))

transactions_I = compute_unique_values(transactions)
print(transactions_I)
interview_I = compute_unique_values(table)
print(interview_I)

# NOTE: apriori algorithm step 4 prune step: exame all susbets of c with k - 1 elements
def compute_k_minus_1_subsets(itemset):
    # or use itertools.combinations()
    subsets = []
    for i in range(len(itemset)):
        subsets.append(itemset[:i] + itemset[i + 1:])
    return subsets

k2_subsets = compute_k_minus_1_subsets(["c", "e", "s"])
print(k2_subsets) # [[c, e], [c, s], [e, s]]

# NOTE: apriori lab task #4/5: generate confidenet rules using supported itemsets
def generate_apriori_rules(supported_itemsets, table, minconf):
    rules = []
    # for each itemset S in supported_itemsets
    # generate the 1 term RHSs and the corresponding LHSs
    # check confidence >= minconf => append to rules
    # move on to the 2 term RHS... len(S)-1 term RHS...
    return rules 

# NOTE: apriori lab task #3: find supported itemsets
def apriori(table, minsup, minconf):
    # goal is to generate and return supported and confident rules
    supported_itemsets = []
    # TODO: finish apriori...
    # step 1. generate L1 supported itemsets of cardinality 1
    # to do this, use I
    I = compute_unique_values(table)
    # TODO: check support of singletons in L1!!
    # step 2. k = 2
    k = 2
    # TODO: step 3. while loop... while(Lkminus1 is not empty)
    # TODO: steps 4., 5., 6., ...

    rules = generate_apriori_rules(supported_itemsets, table, minconf)
    return rules 

rules = apriori(transactions, 0.25, 0.8)
print(rules) # check against your hand trace from apriori lab tasks #4/5