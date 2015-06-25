import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    #for w in record:
      mr.emit_intermediate(record[0], record)
      mr.emit_intermediate(record[1], record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    tmp = []
    for v in list_of_values:
      match = 0
      if v[1] == key:
        continue
      for u in list_of_values:
        if (u[0] == v[1] and u[1] == v[0]):
          match = 1
          break
      if match == 0:
         mr.emit((v[0],v[1]))
         mr.emit((v[1],v[0]))
   #     tmp.append(v)
   #     tmp.append([v[1],v[0]])    
   # print tmp
   # tmp = list(set(tmp))
   # print tmp
   # mr.emit(tmp)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
