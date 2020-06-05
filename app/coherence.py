from flask import Blueprint, render_template
from difflib import SequenceMatcher
import nltk
import docx2txt
import pandas as pd
import docx
from docx import Document
import nltk as nl
import pandas as pd
import numpy as np
import operator
import glob
import re
# coherence=Blueprint("coherence",__name__,static_folder="static",template_folder="templates")
# keywo = ["java", "python", "c"]
# @coherence.route("/coherence")
# def coherence_c():


def coherence_cv(keywo):
    print(keywo)
    keywords = keywo[0]
    d = dict()
    for filename in glob.glob("./uploads/*.docx"):
        resume=filename
    my_text = docx2txt.process(resume)
    print(my_text)
    print(type(my_text))
    with open("./repository.csv") as f:
        lst = f.read()
    lst = lst.replace('\n', ' ')
    # lst=lst.splitlines()
    lst = lst.lower()
    # print(lst)
    wordz = lst.split(" ")
    wordz.pop()
    # print(wordz)
    # print("addddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddds")

    my_text = my_text.strip()
    line = my_text.lower()
    line =re.sub('[\n]+','',line)
    # print(line)
    words = line.split(" ")
    # print(words)
    for word in words:
        # print(word)
        if word in wordz:
            if word in d:
                d[word] = d[word] + 1
            else:
                d[word] = 1


    for key in list(d.keys()):
        print(key, ":", d[key])
    sorted_d = dict(
        sorted(d.items(), key=operator.itemgetter(1), reverse=True))
    print(sorted_d)
    # result = sorted_d.pop(" ", None)
    a1 = [50, 42, 35, 28, 21, 14, 7, 0]
    a2 = [30, 30, 25, 20, 15, 10, 5, 0]
    a3 = [20, 20, 20, 15, 11, 7, 3, 0]
    i = -1
    for w in sorted_d:
        i = i+1
        if (w == keywords[0]):
            break
        if(i+1 == len(d)):
            i = 7
    j = -1
    for w in sorted_d:
        j = j+1
        if (w == keywords[1]):
            break
        if(j+1 == len(d)):
            j = 7

    k = -1
    for w in sorted_d:
        k = k+1
        if (w == keywords[2]):
            break
        if(k+1 == len(d)):
            k = 7

    ans = a1[i]+a2[j]+a3[k]
    print("idharrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
    print(sorted_d)
    print(ans)
    return ans,sorted_d


def coherence_ans(keywo):
    keywords = keywo[0]
    d = dict()
    my_text = open("./uploads/audio_text.txt", "r")
    with open("./repository.csv") as f:
        lst = f.read()
    lst = lst.replace('\n', ' ')
    # lst=lst.splitlines()
    lst = lst.lower()
    print(lst)
    wordz = lst.split(" ")
    wordz.pop()
    print(wordz)
    for line in my_text:
        line = line.strip()
        line = line.lower()
        words = line.split(" ")
        for word in words:
            if word in wordz:
                if word in d:
                    d[word] = d[word] + 1
                else:
                    d[word] = 1
    for key in list(d.keys()):
        print(key, ":", d[key])
    sorted_d = dict(
        sorted(d.items(), key=operator.itemgetter(1), reverse=True))
    print(sorted_d)
    # result = sorted_d.pop(" ", None)
    a1 = [50, 42, 35, 28, 21, 14, 7, 0]
    a2 = [30, 30, 25, 20, 15, 10, 5, 0]
    a3 = [20, 20, 20, 15, 11, 7, 3, 0]
    i = -1
    for w in sorted_d:
        i = i+1
        if (w == keywords[0]):
            break
        if(i+1 == len(d)):
            i = 7
    j = -1
    for w in sorted_d:
        j = j+1
        if (w == keywords[1]):
            break
        if(j+1 == len(d)):
            j = 7

    k = -1
    for w in sorted_d:
        k = k+1
        if (w == keywords[2]):
            break
        if(k+1 == len(d)):
            k = 7

    ans = a1[i]+a2[j]+a3[k]
    # print("YEAHAHAHAHAHAHAHAHAHAHAHAHAHHAHAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    print(sorted_d)
    print(ans)
    return ans,sorted_d

# ans1=coherence_cv(keywo)
# ans2=coherence_ans(keywo)

# print(ans1)
# print(ans2)
