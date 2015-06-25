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
    mat = record[0]
    i = record[1]
    j = record[2]
    value = record[3]
    if mat == 'a':
      ansI = record[1]
      for index in range(5):
        mr.emit_intermediate((ansI,index),(record[2],record[3]))
    else:
      ansJ = record[2]
      for index in range(5):
        mr.emit_intermediate((index,ansJ),(record[1],record[3])) 

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
   # total = 0
   # for v in list_of_values:
   #   total += v
    print key, list_of_values
    total = 0
    for i,v in enumerate(list_of_values):
       for j,u in enumerate(list_of_values):
         if v[0] == u[0] :
           total += (v[1]*u[1])/4
           print i, j
    mr.emit((key[0],key[1],total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
