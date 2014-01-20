# -*-coding:Latin-1 -*

from NGram import NGram
import datetime
import sys, stat, os


n = 3 # NGram size

#simple command line processing to get files (if, list)
languageFiles=os.listdir("./Samples")
#ignore files starting with '.' using list comprehension
languageFiles=[filename for filename in languageFiles if filename[0] != '.']

#simple command line processing to get files (if, list)
testFiles=os.listdir("./Tests")
#ignore files starting with '.' using list comprehension
testFiles=[filename for filename in testFiles if filename[0] != '.']
    
print "Language samples : ", languageFiles
print "Files to test : ", testFiles

resultMatrix = []

for testFile in testFiles:
    print "\n\n--> ", testFile
    testText = open('Tests/'+testFile).read()
    testStart = datetime.datetime.now()
    testNGram = NGram(testText, n)
    for languageFile in languageFiles:
        languageText = open('Samples/'+languageFile).read()
        languageNGram = NGram(languageText, n)
        print " ", languageFile, " : ", 1 - (languageNGram - testNGram)
    
    testEnd = datetime.datetime.now()
    print "\n  Time : ", (testEnd - testStart)
