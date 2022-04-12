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
rule5 = {"lhs": ["phd=no", "tweets=yes"], "rhs": ["interviwed_well=True"]}