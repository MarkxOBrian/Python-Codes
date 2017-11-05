# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 18:39:44 2017

@author: MarksOBrian
"""

original = input("Enter an English Word")
if len(original)>0 and original.isalpha():
    word=original.lower()
    words=word
    latin="ay"
    converter=word[0]
    new_word=word+converter+latin
    finalword=new_word[1:]
    print(finalword)
else:
    print("Error")