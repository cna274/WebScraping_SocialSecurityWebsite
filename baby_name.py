import re
def baby_name(filename):
  f = open(filename)
  texts = f.read()
  f.close()
### Find year under consideration  
  head = re.search(r'Popularity in \d+', texts)
  head = head.group() 
  year = head[-4:]
### Find list of children name and their ranks

  words = re.findall(r'>\w+', texts)  ## find all the names and their ranks
  #words = words.group() ## put names in a list
  
  start = words.index('>1') # find first index
  end = words.index('>1000') # find last index
  req_words = words[start:end+3] #remove extra stuff from list
  val = []
  for i in req_words:
      val.append(i[1:])
      
  ## put data in dict
  dict = {}
  for i in range(0,len(val),3):
    if not val[i+1] in dict:
        dict[val[i+1]] = val[i]
    else:
        continue
  
  for i in range(0,len(val),3):
    if not val[i+2] in dict:
      dict[val[i+2]] = val[i]
    else:
      if int(dict[val[i+2]]) < int(val[i]):
        continue
      else:
        dict[val[i+2]] = val[i]
        
  #c = []
  #for i in dict:
  #  c.append((i)
  c = sorted(dict.keys())
  #c = sorted(dict.keys())
  
  values = []
  for i in c:
    values.append(dict[i])
  
  answer = []
  for i in range(len(c)):
    answer.append((c[i],values[i]))
    
  #print year
  #print '\n'
  #print answer    
  return (year,answer[:10])
    
  
  