# coding: utf-8
import sys
import json
import operator


def main():
    tweetJson = open(sys.argv[1])
    count = {}
    for line in tweetJson:
      tweetData = json.loads(line)
      if not tweetData.has_key("entities"):
        continue
      if not tweetData["entities"]["hashtags"]:
        continue
      #if not tweetData["entities"]["hashtags"].has_key("text"):
      #  continue

     # print tweetData["entities"]["hashtags"]
     # print tweetData["entities"]["hashtags”][0][“text"]
      for tag in tweetData["entities"]["hashtags"]:
          
          if not count.has_key(tag["text"]):
            count[tag["text"]] = 0 
          count[tag["text"]] = count[tag["text"]] + 1
          

    #for key in count:
    #  str1 = key, str(count[key]) 
    #  print sorted(str1, key=str1.get, reverse=True)[:10]
    #print count
    top = dict(sorted(count.iteritems(), key=operator.itemgetter(1), reverse=True)[:10])
    for key in top:
       print key, str(top[key])


      

if __name__ == '__main__':
    main()
