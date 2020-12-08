import re


bag_dict = {}

# return number of shiny gold bags inside this dict
def shiny_gold(bag):
    total = 0;
    if bag == {}:
        return 0;
    else:
        if 'shiny gold' in bag.keys():
            total += bag['shiny gold']

        for (bag_name,qty) in bag.items() :
            if bag_name != 'shiny gold':
                total += qty * shiny_gold(bag_dict[bag_name])

        return total


def main():
    lines = [line.strip() for line in open("input", "r").readlines()]


    for line in lines:

        re_line = re.search('([a-z]+ [a-z]+) bags contain ((\d+) ([a-z]+ [a-z]+) bag[s,. ]+)+', line)
        bag_name = re.search('[a-z]+ [a-z]+', line).group(0)

        bag_contents = re.search('(?<=contain ).+', line).group(0).rsplit(',')

        this_bag = {}

        for words in [item.split() for item in bag_contents]:
            
            if words[0] == "no":
                pass
            else: 
                qty = int(words[0])
                this_bag_name = ' '.join(words[1:3])
                
                this_bag[this_bag_name] = qty


        bag_dict[bag_name] = this_bag

    for item in bag_dict.items():
        print(item)


    total_shiny  = 0
    for (bag_name, contents) in bag_dict.items():
        shiny = shiny_gold(bag_dict[bag_name])
        if shiny > 0 :
            total_shiny += 1
            print(f'{bag_name} contains {shiny} ')
    print(total_shiny)


if __name__ == '__main__':
    main()
