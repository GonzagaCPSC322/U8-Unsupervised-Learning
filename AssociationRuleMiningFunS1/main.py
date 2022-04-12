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

# lab task #2: compute_rule_counts()

# lab task #3: compute_rule_interestingness()