import sys,getopt
import re
from collections import deque

class ITGTableElement:
    def __init__(self):
        self.name = ""
        self.value = ""
        self.weight = 0

def main(argv):
    germanF = ''
    englishF = ''
    dictionaryF = ''
    try:
        opts, args = getopt.getopt(argv,"d:g:e:")
    except getopt.GetoptError:
        print "Error: Unknown argument provided, use -d, -g or -e"
        sys.exit(2)

    for opt,arg in opts:
        if opt == "-d":
            dictionaryF  = arg
        if opt == "-e":
            englishF = arg
        if opt == "-g":
            germanF = arg

    grammar = []

    dictFile = open(dictionaryF,'r')

    wordSwapCount = 0
    totalCount = 0
    enList = (open(englishF,'r')).readlines()
    geList = (open(germanF,'r')).readlines()

    for eachLine in dictFile:
        tokens = (eachLine.strip()).split()
        element = ITGTableElement()
        element.name = tokens[0].strip()
        element.value = tokens[1].strip()
        element.weight = float(tokens[2].strip())
        grammar.append(element)


    for sentenceNumber in range(len(enList)):
        print "\n\n*****************SentenceNumber : ",sentenceNumber,"*******************"
        englishS = (enList[sentenceNumber]).strip()
        germanS =  (geList[sentenceNumber]).strip()
        engTokens = englishS.split()
        geTokens = germanS.split()

        print "English Sentence :", englishS
        print "German Sentence  :", germanS
        index = 1
        germanwords = []
        while(len(engTokens)>0):
            engWords = deque(engTokens)
            word = engWords.popleft()
            engTokens.remove(word)
            flag = 0
            for element in grammar:
                if element.name == word:
                    for gerWords in geTokens:
                        if element.value == gerWords:
                            flag = 1
                            germanwords.append(gerWords)
                            print "English to German           : ", word, " -> ", element.value
                            word = ""
                            geIndex = geTokens.index(element.value)
                            print  "EngWordPos to GermanWordPos : ", index, " -> ", geIndex + 1
                            totalCount = totalCount + 1
                            if index != geIndex + 1:
                                wordSwapCount = wordSwapCount + 1
                            # geTokens.remove(gerWords)

            if flag == 0:
                print "English to German           :", word, " -> ", " "
                print "EngWordPos to GermanWordPos : ", index, " -> ", index
                totalCount = totalCount + 1

            index = index +1
        for item in geTokens:
            if item not in germanwords:
                geIndex = geTokens.index(item)
                print "English to German           :  "," -> ", item
                print "EngWordPos to germanWordPos : ", geIndex + 1, " -> ", geIndex + 1
                totalCount = totalCount + 1
        print "total alignments done =" + str(totalCount)
        print "total word swaps done =" + str(wordSwapCount)



if __name__=="__main__":
    main(sys.argv[1:])
