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
    key = record[0]
    order_id = record[1]
   # if record[0] == "line_item": 
    mr.emit_intermediate(order_id, record)

   # if record[0] == "order": 
   #   mr.emit_intermediate(order_id, record[0:9])



def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = []
    
      
    for v in list_of_values:
      if v[0] == "order":
        for p in list_of_values:
          if p[0] == "line_item":
            total = []
            for a in v:
              total.append(a)
            for b in p:
              total.append(b)
  
            mr.emit((total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
