# coding: utf-8
import sys
import json


def main():
    tweetJson = open(sys.argv[1])
    count = {}
    for line in tweetJson:
      tweetData = json.loads(line)
      if tweetData.has_key("text"):
        for newWord in tweetData["text"].split():
          if not count.has_key(newWord):
            newCount = 0 
          count[newWord] = newCount + 1

    for key in count:
      str1 = key + " " + str(count[key]) 
      print str1
        

if __name__ == '__main__':
    main()
