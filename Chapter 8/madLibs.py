##! python 3
#madLibs.py - Create a madLibs program that reads in text files and lets the user add their own text anywher the word ADJJECTIVE, NOUN, ADVERB, or VERB appears in the test files
import os, re, sys, shelve

def madLibs(file):
    madLibRegex = re.compile(r'\b(verb|adjective|adverb|noun)\b*') 
    textFile = open(file, 'r')
    madLibText = textFile.read()
    madLibList = madLibText.split(" ")

    for word in madLibList:
        index = madLibList.index(word)
        wordMatch = madLibRegex.search(word.lower()) 
        if wordMatch:
            newWord = input(f'Please enter a {word.lower()}: ')
            madLibList[index] = newWord

    newText = " ".join(madLibList)
    print(newText)
    newTextFile = open(f"{file}"+"_complete", 'w')
    newTextFile.write(newText)

    textFile.close()
    newTextFile.close()

madLibs('chapter 8\\test.txt')
