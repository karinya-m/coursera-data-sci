# coding: utf-8
import sys
import json


def main():
    scores = getScores(sys.argv[1])
    tweetJson = open(sys.argv[2])
    newSent = {}
    for line in tweetJson:
      sum = 0
      numOfWord = 0
      temp = []
      tweetData = json.loads(line)
      if tweetData.has_key("text"):
        for word in tweetData["text"].split():
          if scores.has_key(word):
            sum = sum + scores[word]
            numOfWord = numOfWord + 1
          else:
            temp.append(word)        
     #if (numOfWord == 0):
     #  continue
      newScore = sum #/numOfWord
      for newWord in temp:
        if newSent.has_key(newWord):
          newScore = (newScore + newSent[newWord])/2 
        newSent[newWord] = newScore
    for key in newSent:
      str1 = key + "\t" + str(newSent[key]) 
      print str1
        

if __name__ == '__main__':
    main()
