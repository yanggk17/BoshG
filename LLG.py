# -*- coding: UTF-8 -*-

import os, re
import random, readJSON

data = readJSON.read_json("dataEN.json")
before = data["before"]
after = data["after"]
bosh = data["bosh"]
famous = data["famous"]

xx = "情书"

repeat_degree = 2

def shuffle_card(liebiao):
    global repeat_degree
    pool = list(liebiao)*repeat_degree
    while True:
        random.shuffle(pool)
        for element in pool:
            yield element

next_bosh = shuffle_card(bosh)
next_famous = shuffle_card(famous)

def give_sth_famous():
    global next_famous
    xx = next(next_famous)
    xx = xx.replace("1",random.choice(before))
    xx = xx.replace("2",random.choice(after))
    return xx

def another_section():
    xx = "."
    xx += "\r\n"
    xx += "    "
    return xx

if __name__ == "__main__":
    xx = input("plz enter theme:")
    for x in xx:
        tmp = str()
        while (len(tmp) < 6000 ):
            branch = random.randint(0,100)
            if branch <5:
                tmp += another_section()
            elif branch < 20:
                tmp += give_sth_famous()
            else:
                tmp += next(next_bosh)
        tmp = tmp.replace("x",xx)
        print(tmp)
