import csv
import re

DATE_RE = r"(\d{2}\/\d{2}\/\d{4})"
MONEY_RE = r"((\+|\-)\s+\$((\d+[.,]?)+\d+))"
MATCH_RE = "\d{2}\/\d{2}\/\d{4}\s+(.*)\s+[\+|\-]"

SPACING_DOUBLE = r"\s+"
EMPTY_STRING = ""
SPACINT_TRAILING = r"\s+$"
COMA_RE = r"\,"


def remove_char(reEx, string):
    return re.sub(reEx, "", string)


def extract_date(line):
    date_match = re.search(DATE_RE, line)
    if date_match:
        # print(date_match.group())
        date = date_match.group()
    else:
        print("Not found in ", line)

    return date


def extract_money_ammount(line):
    money_match = re.search(MONEY_RE, line)
    if money_match:
        # print(money_match.group())
        ammount = money_match.group()
    else:
        print("Ammount not found in ", line)

    return ammount


def extract_concept(line):

    all_match = re.findall(MATCH_RE, line)
    if all_match:
        # print(all_match)
        concept = all_match[0]
    else:
        print("weird")

    # print("{}, {}, {}".format(date, ammount, concept))
    concept = re.sub(r'\s+', ' ', concept)
    concept = re.sub(r'\s+$', "", concept)

    return concept


def read_capital_one_statement(fname):
    with open(fname) as f:
        data = f.read()
    lines = data.split("\n")

    return lines


def write_statement_to_csv(fields, fname):
    with open('test.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(fields)


def extract_capital_one_statement(lines):
    fields = []
    # Extract statement field names form lines
    fields.append(list(filter(None, lines[0].split(" "))))

    # date_p = re.compile(DATE_RE)
    # money_p = re.compile(MONEY_RE)

    # print(date_p)
    for line in lines[1:]:

        line = line.replace(",", "")
        date = extract_date(line)
        ammount = extract_money_ammount(line)
        concept = extract_concept(line)
        fields.append([date, ammount, concept])

    return fields


fileIn = "CapitalOne_Cheking_test.txt"
fileOut = "test.csv"
lines = read_capital_one_statement(fileIn)
statements = extract_capital_one_statement(lines)
write_statement_to_csv(statements, fileOut)


