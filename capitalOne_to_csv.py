# import os
import csv
import re


fname = "CapitalOne_Cheking_test.txt"
with open(fname) as f:
    data = f.read()

lines = data.split("\n")
fileds_string = lines[0].split(r" ")
fields = []
# fields.append(", ".join(list(filter(None, lines[0].split(" ")))))
fields.append(list(filter(None, lines[0].split(" "))))

# print(lines)

# BANK_OPTIONS = ["Debit Card Purchase",
#                 "Overdraft charge",
#                 "Online banking",
#                 "Withdrawal"]

# OPTIONS = "|".join(BANK_OPTIONS)
# MATCH_RE = "".join(["\d{4}(\.*[", OPTIONS, "]\.*)\s+(\+|\-)"])

DATE_RE = r"(\d{2}\/\d{2}\/\d{4})"
MONEY_RE = r"((\+|\-)\s+\$((\d+[.,]?)+\d+))"
MATCH_RE = "\d{2}\/\d{2}\/\d{4}\s+(.*)\s+[\+|\-]"

date_p = re.compile(DATE_RE)
money_p = re.compile(MONEY_RE)


# print(date_p)
for line in lines[1:]:

    line = line.replace(",", "")
    date_match = re.search(DATE_RE, line)
    if date_match:
        # print(date_match.group())
        date = date_match.group()
    else:
        print("Not found in ", line)

    money_match = re.search(MONEY_RE, line)
    if money_match:
        # print(money_match.group())
        ammount = money_match.group()
    else:
        print("Ammount not found in ", line)

    all_match = re.findall(MATCH_RE, line)
    if all_match:
        # print(all_match)
        concept = all_match[0]
    else:
        print("weird")

    # print("{}, {}, {}".format(date, ammount, concept))
    concept = re.sub(r'\s+', ' ', concept)
    concept = re.sub(r'(.)\s+$', r'\1', concept)
    fields.append([date, ammount, concept])

print(fields)

with open('test.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(fields)
