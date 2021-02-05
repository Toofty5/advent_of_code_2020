import itertools as it



def valid_strings(rule_set):


    # single list, no forks
    if len(rule_set) == 1: 
        return_list = []
        single_rule = [rules[x] for x in rule_set[0]]

        for thing in single_rule:
            if isinstance(thing, str):
                return_list.append([thing])
            else:
                return_list.append(valid_strings(thing))

        # print(f"joining {return_list}")
        return_list = ["".join(thing) for thing in it.product(*return_list)]

        #print(f"return_list {return_list}")

        if len(return_list) == 1:
            return "".join(return_list[0])
        else:
            return return_list


    # multiple lists
    else:
        
        #print(f"forked input {rule_set}")
        return_list = [valid_strings([x]) for x in rule_set]
        #print(f"forked return {list(return_list)}")

        if all([isinstance(x, str) for x in return_list]):
            return return_list
        else:
            product_list = it.product(*return_list)
            return ["".join(thing) for thing in product_list]



rules_str, messages_str = [section.strip() for section in open('input',
    'r').read().split('\n\n')]

rules_lines = rules_str.split('\n')

rules = [""] * len(rules_lines)

a_index, b_index = 0,0

for line in rules_lines:
    index_str, rule_str = line.split(':')

    index = int(index_str)

    if '|' in rule_str:
        pair_a_str, pair_b_str = rule_str.split('|')
        rule1 = [int(x) for x in pair_a_str.split()]
        rule2 = [int(x) for x in pair_b_str.split()]

        rules[index] = [rule1, rule2]
    elif 'a' in rule_str:
        rules[index] = 'a'
        a_index = index
    elif 'b' in rule_str:
        rules[index] = 'b'
        b_index = index
    else:
        rules[index] = [[int(x) for x in rule_str.split()]]




#go through all the single-rule lines
for i, rule in enumerate(rules):
    if len(rule) == 1 and rule not in ['a','b']:
        single_rule = rule[0]
        if len(single_rule) == 1:
            rules[i] = rules[single_rule[0]]

#for i, rule in enumerate(rules):
#    print(i, rule)

my_list = valid_strings([[0]])

