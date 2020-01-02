"""Parsing a request"""

# Authors: Thierry Moudiki
#
# License: BSD 3


import re
import numpy as np

# req = "(time == 'Dinner') & (day == 'Sun') & (tip>1.5)"
# req = "(tip>1.5)"
# req = "(tip > 5) & (size > 3)"
# req = "(tip > 5) & (size > 3) & (sex = 'Male')"
# req = "(tip > 5) & (size > 3) & (sex == 'Male')"
def parse_request(x):

    # parse the request
    y = re.compile(r"(\bAND\b|\bOR\b|&|!=|==|<=|>=|<|>|\(|\)|\.\*)")
    y = y.split(x.replace(" ", ""))
    y = list(filter(("").__ne__, y))

    # one filtering condition
    if len(y) <= 5:
        try:
            return "(df['" + y[1] + "']" + " " + y[2] + " " + y[3] + ")"
        except:
            return "(df['" + y[0] + "']" + " " + y[1] + " " + y[2] + ")"

    # more filtering conditions

    assert "(" in y, "parentheses must be provided for multiple conditions"

    step_size = 6
    idx = 0
    left_exps = []
    ops_conds = []
    right_exps = []
    ops_between_conds = []

    while idx < 3:
        try:
            left_exps.append(y[idx * step_size + 1])
        except:
            pass
        try:
            ops_conds.append(y[idx * step_size + 2])
        except:
            pass
        try:
            right_exps.append(y[idx * step_size + 3])
        except:
            pass
        try:
            ops_between_conds.append(y[idx * step_size + 5])
        except:
            pass
        idx += 1

    n_conds = len(left_exps)
    str_conds = (
        "(df['"
        + left_exps[0]
        + "'] "
        + ops_conds[0]
        + " "
        + right_exps[0]
        + ")"
    )
    idx_cond = 1

    while idx_cond < n_conds:
        try:
            op = ops_between_conds[idx_cond - 1]
            str_conds += (
                " "
                + op
                + " (df['"
                + left_exps[idx_cond]
                + "']"
                + " "
                + ops_conds[idx_cond]
                + " "
                + right_exps[idx_cond]
                + ")"
            )
            idx_cond += 1
        except:
            raise ValueError(
                "invalid request: check column names, column contents, operators and parentheses"
            )
            return

    return str_conds


# parse_update_request('tip = 2*tip')
# parse_update_request("toto = 3*tip")
# parse_update_request('tip = tip*2')
# parse_update_request("toto = tip*3")
# parse_update_request('tip = np.mean(tip)')
# parse_update_request('toto = np.mean(tip)')
def parse_update_request(x):

    if x[0] == "(":
        raise ValueError("invalid request: do not use parentheses")

    # parse the request
    try:
        y = x.replace(" ", "").split("=")
    except:
        raise ValueError("invalid request: must be colname = f(colname)")

    key1 = y[0]
    exp_block2 = y[1]
    z = exp_block2.replace(key1, "df['" + key1 + "']")
    idx_par_begin = y[1].find("(")  # e.g np.mean(tip)

    # parentheses found?
    if (idx_par_begin > 0) & (z.find("(") > 0):  # e.g np.mean(tip)

        try:
            idx_par_end = z.find(")")
        except:
            raise ValueError("invalid request: closing parenthese not found")

        t = z[(idx_par_begin + 1) : idx_par_end]

        key2 = t.replace("df['", "").replace("']", "")

        if key1 == key2:
            return "df['" + key1 + "']" + " = " + z
        else:
            return (
                "df['"
                + key1
                + "']"
                + " = "
                + z.replace(key2, "df['" + key2 + "']")
            )

    # no parenthese found
    reg = re.compile(r"(\+|\*|\-|/)")
    key2 = reg.split(exp_block2)[-1]

    if key1.isalpha() & key2.isalpha():

        if key1 == key2:
            return "df['" + key1 + "']" + " = " + z
        else:
            return (
                "df['"
                + key1
                + "']"
                + " = "
                + z.replace(key2, "df['" + key2 + "']")
            )

    else:

        key2 = reg.split(z)[0]

        if key2.find("df[") >= 0:
            return "df['" + key1 + "']" + " = " + z

        if key2.isalpha() == False:
            temp = reg.split(z)
            key3 = temp[-1]
            op = temp[1]
            return (
                "df['" + key1 + "']" + " = " + key2 + op + "df['" + key3 + "']"
            )

        return (
            "df['" + key1 + "']" + " = " + z.replace(key2, "df['" + key2 + "']")
        )


# parse_cols_request("SELECT tip, smoker, day FROM df WHERE tip > 25")
# parse_cols_request("SELECT SUM(tip), smoker FROM df WHERE tip > 20 GROUP BY smoker")
# parse_cols_request("SELECT AVG(tip), size, smoker FROM df WHERE tip > 20 GROUP BY size")
# parse_cols_request("SELECT AVG(tip) as avg_tip, size, smoker FROM df WHERE tip > 20 GROUP BY size")
# parse_cols_request("SELECT AVG(tip) as avg_tip, AVG(size) as   avg_size, smoker FROM df WHERE tip > 20 GROUP BY size, tip")
def parse_cols_request(x):

    idx_from = x.lower().find("from")
    cols_text = x[7:idx_from]

    cols_text_split = cols_text.split(",")

    if cols_text.find("as") < 0:
        for idx, elt in enumerate(cols_text_split):
            idx_as = elt.find("(")
            if idx_as > 0:
                cols_text_split[idx] = (
                    elt.replace(" ", "")
                    .replace("(", "_")
                    .replace(")", "")
                    .replace("*", "all")
                    .lower()
                )

        return [
            cols_text_split[idx].replace(" ", "")
            for idx in range(len(cols_text_split))
        ]

    # if cols_text.find('as') > 0 # (as is found):
    for idx, elt in enumerate(cols_text_split):
        idx_as = elt.find("as")
        if idx_as > 0:
            cols_text_split[idx] = elt[(idx_as + 2) : len(elt)].replace(" ", "")

    return [
        cols_text_split[idx].replace(" ", "")
        for idx in range(len(cols_text_split))
    ]
