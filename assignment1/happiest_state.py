# coding: utf-8
import sys
import json

def getScores(path):
   afinnfile = open(path)
   scores = {} # initialize an empty dictionary
   for line in afinnfile:
     term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
     scores[term] = int(score)  # Convert the score to an integer.
   return scores

def getStateList():
  states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
  }  
  return states

def main():
    avg = {}
    scores = getScores(sys.argv[1])
    tweetJson = open(sys.argv[2])
    sumScore = {}
    sumTweet = {}
    stateList = getStateList()
    for line in tweetJson:
      sum = 0
      tweetData = json.loads(line)
      if not tweetData.has_key("user"):
        continue

      if not tweetData["user"].has_key("location"):
        continue
    
      state = tweetData["user"]["location"][-2:]
      
      if not stateList.has_key(state):
        continue
      
      if tweetData.has_key("text"):
        for word in tweetData["text"].split():
          if scores.has_key(word):
            sum = sum + scores[word]
        if sum == 0:
          continue

        score = sum  
 
        if not sumScore.has_key(state):
          sumScore[state] = 0 
          sumTweet[state] = 0
        sumScore[state] = sumScore[state] + score
        sumTweet[state] = sumTweet[state] + 1

    for key in sumScore:
      avg[key] = sumScore[key]/sumTweet[key]
      
    print max(avg, key=avg.get)
    return max(avg, key=avg.get)
        

if __name__ == '__main__':
    main()
