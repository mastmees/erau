import re
import sys

qnumber=100

questions=[]
for l in open("b-klass.txt").readlines():
  l=l.strip()
  if re.search("^M[1-9][0-9]*-[1-9][0-9]* ",l):
    p=l.partition(" ")
    questions.append((p[0].strip(),p[2].strip()))

def qid(qtext,module):
  global questions,qnumber
  for id,qt in questions:
    if qt.rstrip("?:")==qtext:
      return id
  id=f"{module}-{qnumber}"
  qnumber+=1
  return id
  
for l in open("d-klass.txt").readlines():
  l=l.strip()
  if l.startswith("Moodul "):
    t=l.split(" ")
    module=t[1]
    print(l)
  elif re.search("^[1-9][0-9]*\\.[1-9][0-9]*\\.",l):
    qi=0
    t=l.split(".",2)
    l=t[2]
    q=l.rstrip(".?:")
    id=qid(q,module)
    print(id,l)
  else:
    if qi>2:
      print(l)
      sys.exit(1)
    if l[0:2] not in ("A.","B.","C.","D."):
      l="ABCDEF"[qi]+". "+l
    qi+=1
    if l.endswith(";"):
      l=l[0:-1]+"."
    elif not l.endswith("."):
      l=l+"."
    print(l)

    
