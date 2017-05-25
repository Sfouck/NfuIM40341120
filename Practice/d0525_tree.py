from decision_trees import *

inputs = [
        ({'level':'Senior','lang':'Java','tweets':'no','phd':'no'},   False),
        ({'level':'Senior','lang':'Java','tweets':'no','phd':'yes'},  False),
        ({'level':'Mid','lang':'Python','tweets':'no','phd':'no'},     True),
        ({'level':'Junior','lang':'Python','tweets':'no','phd':'no'},  True),
        ({'level':'Junior','lang':'R','tweets':'yes','phd':'no'},      True),
        ({'level':'Junior','lang':'R','tweets':'yes','phd':'yes'},    False),
        ({'level':'Mid','lang':'R','tweets':'yes','phd':'yes'},        True),
        ({'level':'Senior','lang':'Python','tweets':'no','phd':'no'}, False),
        ({'level':'Senior','lang':'R','tweets':'yes','phd':'no'},      True),
        ({'level':'Junior','lang':'Python','tweets':'yes','phd':'no'}, True),
        ({'level':'Senior','lang':'Python','tweets':'yes','phd':'yes'},True),
        ({'level':'Mid','lang':'Python','tweets':'no','phd':'yes'},    True),
        ({'level':'Mid','lang':'Java','tweets':'yes','phd':'no'},      True),
        ({'level':'Junior','lang':'Python','tweets':'no','phd':'yes'},False)
    ]

for key in ['level','lang','tweets','phd']:
    print key, partition_entropy_by(inputs, key)
print

print("senior_inputs")
senior_inputs = [(input, label)
                 for input, label in inputs if input["level"] == "Senior"]

for key in ['lang', 'tweets', 'phd']:
    print key, partition_entropy_by(senior_inputs, key)
print


print("java_inputs------test")
java_inputs = [(input, label)
                 for input, label in inputs if input["lang"] == "Java"]

for key in ['lang', 'tweets', 'phd']:
    print key, partition_entropy_by(java_inputs, key)
print


print "building the tree"
tree = build_tree_id3(inputs)
print tree

print "Junior / Java / tweets / no phd", classify(tree,
    { "level" : "Junior",
      "lang" : "Java",
      "tweets" : "yes",
      "phd" : "no"} )

print "Junior / Java / tweets / phd", classify(tree,
    { "level" : "Junior",
             "lang" : "Java",
             "tweets" : "yes",
             "phd" : "yes"} )

print "Intern", classify(tree, { "level" : "Intern" } )
print "Senior", classify(tree, { "level" : "Senior" } )