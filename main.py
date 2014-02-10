# -*-coding:Latin-1 -*

from NGram import NGram
from NGramJSD import NGramJSD
from NGramJSD2 import NGramJSD2
import datetime
import sys, stat, os

def moyenne(nbs):
    return float(sum(nbs) / len(nbs))

def array_substract(array, sub):
    i = 0
    for nb in array:
        array[i] = nb - sub
        i += 1
    return array

def normalized_array(array):
    mini = float(min(array))
    maxi = float(max(array))
    i = 0
    for nb in array:
        array[i] = 1.0 - float(nb - mini)/(maxi - mini)
        #array[i] = (1.0 - float(nb / maxi)) #* (1.0 - float(nb / maxi))    
        i += 1
    return array


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

def Vector():
    print "---------------- Vectors Way ------------------"

    for testFile in testFiles:
        print "\n\n--> ", testFile
        testText = open('Tests/'+testFile).read()
        testStart = datetime.datetime.now()
        testNGram = NGram(testText, n)
        scores = []
        i = 0
        for languageFile in languageFiles:
            languageText = open('Samples/'+languageFile).read()
            languageNGram = NGram(languageText, n)
            scores.append(languageNGram - testNGram)
            i += 1

        i = 0
        for score in scores:
            print " ", languageFiles[i], " : ", score
            i += 1
        bestIndex = scores.index(max(scores))
        languageFound = languageFiles[bestIndex]
        print "\n Vector based finds", languageFound, "\n With", ((scores[bestIndex] / sum(scores)))*100, "%"
        
        testEnd = datetime.datetime.now()
        print "\n  Time : ", (testEnd - testStart)

def JSD():
    print "\n\n"
    print "----------- Jenson & Shannon Way --------------"

    for testFile in testFiles:
        print "\n\n--> ", testFile
        testText = open('Tests/'+testFile).read()
        testStart = datetime.datetime.now()
        testNGram = NGramJSD(testText, n)
        scores = []
        i = 0
        for languageFile in languageFiles:
            languageText = open('Samples/'+languageFile).read()
            languageNGram = NGramJSD(languageText, n)
            scores.append(languageNGram - testNGram)
            i += 1

        i = 0
        for score in scores:
            print " ", languageFiles[i], " : ", score
            i += 1
        bestIndex = scores.index(min(scores))
        languageFound = languageFiles[bestIndex]
        print "\n JSD normal finds", languageFound, "\n With", ((scores[bestIndex] / sum(scores)))*100, "%"
        
        testEnd = datetime.datetime.now()
        print "\n  Time : ", (testEnd - testStart)

def JSD2():
    print "\n\n"
    print "------- Jenson & Shannon Way Improved ---------"

    for testFile in testFiles:
        print "\n\n--> ", testFile
        testText = open('Tests/'+testFile).read()
        testStart = datetime.datetime.now()
        testNGram = NGramJSD2(testText, n)
        scores = []
        diffs_histo = []
        i = 0
        for languageFile in languageFiles:
            languageText = open('Samples/'+languageFile).read()
            languageNGram = NGramJSD2(languageText, n)
            scores.append(languageNGram - testNGram)
            diffs_histo.append(testNGram.histo_diff(languageNGram))
            i += 1

        i = 0
        for score in scores:
            #print " ", languageFiles[i], " : ", score
            i += 1
        bestIndex = scores.index(max(scores))
        languageFound = languageFiles[bestIndex]
        #print "\n JSD normal finds", languageFound, "with", ((scores[bestIndex] / sum(scores)))*100, "%"
        
        #print "\n"

        diffs_histo = normalized_array(diffs_histo)
        
        i = 0
        for diff in diffs_histo:
            #print " ", languageFiles[i], " : ", diff
            i += 1
        print ""

        finalScores = [a*b for a,b in zip(diffs_histo,scores)] # == diffs_histo * scores element by element
        i = 0
        for score in finalScores:
            print " ", languageFiles[i], " : ", score
            i += 1

        bestIndex = finalScores.index(max(finalScores))
        languageFound = languageFiles[bestIndex]
        
        testEnd = datetime.datetime.now()
        print "\n JSD improved finds", languageFound, "\n With", ((finalScores[bestIndex] / sum(finalScores)))*100, "%"
        print "\n  Time : ", (testEnd - testStart)


Vector()
JSD()
JSD2()
