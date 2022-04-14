import itertools

from numpy import power

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

# warmup task
def prepend_attribute_label(table, header):
    for row in table:
        for i in range(len(row)):
            row[i] = header[i] + "=" + str(row[i])

prepend_attribute_label(table, header)
for row in table:
    print(row)
# why do this? if we store each row as a set (unordered collection 
# of unique values), then as is we could not distinguish
# between tweets and phd

# unsupervised learning
# there is no "special attribute" (AKA class) that we are interested
# in predicting
# instead we are looking for associations, groups,
# patterns, trends, reduction, etc...
# PA8: association rule mining
# BONUS PA9: k means clustering

# intro to ARM
# recall: decision trees give us classification rules
# example: IF att1=val1 AND att2=val2 AND .... THEN class=label
# terminology:
# everything to the left of the THEN is the "LHS" (left hand side)
# everything to the right of the THEN is the "RHS" (right hand side)
# with classification rules, there is only one "term" 
# (attribute name/value pair) in the RHS (class/label pair)
# ARM relaxes this constraint
# at least one term in LHS and at least one term in RHS
# example: IF att1=val1 AND att2=val2 AND .... THEN att10=val10
# AND att11=val1 AND ...
# attribute can be used at most once in the rule

# how to generate rules?
# brute force generate rules using possible attribute/value combinations
# VERY computationally expensive
# we will use apriori... some initial notes
# 1. even with apriori tricks, still computationally expensive
# 2. apriori generates ALOT of rules... some are very "weak"
# we need rule evaluation metrics
# 3. association does not imply causality

# our game plan for learning ARM/apriori
# 1. Intro to ARM lab (today): given rules, interpret/evaluate them
# 2. Apriori lab (thursday): tracing the algorithm
# 3. PA8 starter code (next week)
# 4. Finish PA8 (last one!!)

# how to represent rules in Python?
# use dictionaries!
# example: IF interviewed_well=False THEN tweets=no
rule1 = {"lhs": ["interviewed_well=False"], "rhs": ["tweets=no"]}
# task define rule5
rule5 ={"lhs": ["phd=no", "tweets=yes"], "rhs": ["interviewed_well=True"]}

# utility function
def check_row_match(terms, row):
    # return 1 if all the terms in terms are in row
    # 0 otherwise
    for term in terms:
        if term not in row:
            return 0
    return 1

# lab task #2: compute_rule_counts()
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

# lab task #3: compute_rule_interestingness()
def compute_rule_interestingness(rule, table):
    Nleft, Nright, Nboth, Ntotal = compute_rule_counts(rule, table)
    rule["confidence"] = Nboth / Nleft
    rule["support"] = Nboth / Ntotal
    rule["completeness"] = Nboth / Nright
    # NOTE: the denominators could be 0

for rule in [rule1, rule5]:
    compute_rule_interestingness(rule, table)
    print(rule)

# set theory basics and implementation in Python
# set: an unordered collection with no duplicates
# python has a built in set type
transaction = ["eggs", "eggs", "peanutbutter", "chaitea"]
transaction_set = set(transaction)
print("set:", transaction_set)
# note there are no duplicates and order is lost
transaction = sorted(list(transaction_set))
print("list:", transaction)

# A union B: the set of all items in A or B or both
# A intersect B: the set of all items in both A and B
# there are union() and intersection() methods
# with the set type
# transaction_set.
# for apriori, we do need union()

# A is subset of B if all the items in A are also in B
# check_row_match(A, B) returns 1 if A is a subset of
# B, 0 otherwise

# suppose we have an LHS (list or set) and 
# an RHS (list or set)
# LHS intersection RHS should be 0 (empty set)
# LHS union RHS (lhs.union(rhs) or sorted(lhs + rhs))

# powerset of A is the set of all subsets of A
# (including the empty set and A itself)
# task: on paper, calculate the powerset of
# transaction
powerset = []
for i in range(0, len(transaction) + 1):
    # i is the size of subsets
    powerset.extend(itertools.combinations(transaction, i))
print(powerset)

# intro to market basket analysis (MBA)
# associations between products customers
# buy together
# IF {"milk=true", "sugar=true"} THEN {"eggs=true"}
# we are only interested in products bought (e.g. =true)
# and not products not bought (e.g. =false)
# shorthand, dropping the =true
# IF {"milk", "sugar"} THEN {"eggs"}
# {"milk", "sugar"} -> {"eggs"}
# terminology
# a row in our dataset is "transaction"
# a transaction is an "itemset"

# apriori lab