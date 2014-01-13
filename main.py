# -*-coding:Latin-1 -*

from NGram import NGram
import datetime

englishSample = open('Samples/english.txt')
frenchSample = open('Samples/french.txt')
germanSample = open('Samples/german.txt')
spanishSample = open('Samples/spanish.txt')
russianSample = open('Samples/russian.txt')

n = 3

english = NGram(englishSample.read(), n)
french = NGram(frenchSample.read(), n)
german = NGram(germanSample.read(), n)
spanish = NGram(spanishSample.read(), n)
russian = NGram(russianSample.read(), n)

textSample = "La langue française est un attribut de souveraineté en France, depuis 1992 « la langue de la République est le français » (article 2 de la Constitution de la Cinquième République française). Elle est également le principal véhicule de la pensée et de la culture française dans le monde. La langue française fait l’objet d’un dispositif public d’enrichissement de la langue, avec le décret du 3 juillet 1996 relatif à l'enrichissement de la langue française."

text = NGram(textSample, n)

start = datetime.datetime.now()

print "French : ", 1 - (french - text)
print "English : ", 1 - (english - text)
print "German : ", 1 - (german - text)
print "Spanish : ", 1 - (spanish - text)
print "Russian : ", 1 - (russian - text)

end = datetime.datetime.now()

print (end - start)