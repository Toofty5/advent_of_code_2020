import itertools
import textwrap

# return list of strings
def valid_strings(rule_num):
    # rules_dict contains lists of tuples
    this_rule = rules_dict[rule_num]

    if this_rule in [['a'],['b']]:
        return this_rule

    elif len(this_rule) == 1:
        return eval_rules(this_rule[0])

    else:
        return eval_rules(this_rule[0]) + eval_rules(this_rule[1])

#return list of strings, but takes tuple as input
def eval_rules(rule_tuple):

    if all([isinstance(rule_item, str) for rule_item in rule_tuple]):
        return "".join(rule_tuple)
        

    if len(rule_tuple) == 1:
        (single_rule,) = rule_tuple
        return valid_strings(single_rule)


    else:

#        rule1, rule2 = rule_tuple
#        list1 = valid_strings(rule1)
#        list2 = valid_strings(rule2)
#        return [x + y for x in list1 for y in list2]

        # product() returns list of tuples
        eval_list = [valid_strings(rule) for rule in rule_tuple]

        prod_list = list(itertools.product(*eval_list))


        return_list = ["".join(thing) for thing in prod_list]
        return return_list



input_str = open("input2", "r").read()
rules_str, messages_str = input_str.split('\n\n')

# build rules_dict

rules_dict = {}

for rule_line in rules_str.split('\n'):
    rule_num_str, rule_str = [thing.strip() for thing in rule_line.split(':')]

    rule_num = int(rule_num_str)

    rule_piped = rule_str.split('|')

    if len(rule_piped) == 1:

        if rule_str == "\"a\"":
            rules_dict[rule_num] = ['a']
            a_index = rule_num

        elif rule_str == "\"b\"":
            rules_dict[rule_num] = ['b']
            b_index = rule_num

        else:
            rules_dict[rule_num] = [tuple(map(int, rule_str.split()))]

    else:
        tupled_rules = [tuple(map(int, this_str.split())) for this_str in rule_piped]
        print(tupled_rules)
        rules = [tuple(map(int, this_str.split())) for this_str in rule_piped]

        rules_dict[rule_num] = rules

#allstrings = valid_strings(0)

corrected_list = []
fortytwos = valid_strings(42)
thirtyones = valid_strings(31)

#for i in range(1,8) :
#    for j in range(1,5):
#        if i > j:
#            print(i,j)
#            all_fortytwos = ["".join(thing) for thing in itertools.product(fortytwos, repeat=i)]
#            all_thirtyones = ["".join(thing) for thing in itertools.product(thirtyones, repeat=j)]
#            corrected = all_fortytwos + all_thirtyones
#




print("Corrected list produced")

total = 0

# now parse messages and evaluate
messages_list = messages_str.split()

for message in messages_list:

    message_split = textwrap.wrap(message, 8)

    count_a=0
    count_b=0
    valid_message = True

    for substring in message_split:
        if substring in fortytwos:
            if count_b != 0:
                print("42 in suffix", message_split)
                valid_message = False
                break
            else:
                count_a += 1
        else:
            if substring in thirtyones:
                count_b += 1
            else:
                print("invalid string", message_split)
                valid_message = False
                break

    if not count_a > count_b > 0:
        print(f"count_a: {count_a}, count_b: {count_b}", message_split)
        valid_message = False

    if valid_message:
        total += 1

print(len(messages_list))
print(total)
