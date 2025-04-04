import re
import json
from pprint import pprint as pp

def read_questions(filename):
  questions={}
  module=None
  qm=None
  qn=None
  line=1
  qc=0
  for l in open(filename,"rt").readlines():
    if l.startswith("Moodul"):
      module=int(l.split(" ")[1][1:-1])
    elif re.search("^M[1-9][0-9]*-",l):
      q=l.split(" ")[0].split("-")
      qm=int(q[0][1:])
      qn=int(q[1])
      if qm not in questions:
        questions[qm]={}
      questions[qm][qn]={"?":l.partition(" ")[2].strip()}
      qc+=1
    elif l[0] in "ABCDE" and l[1]=='.':
      questions[qm][qn][l[0]]=l.partition(" ")[2].strip()
    else:
      print(filename,line,l)
    line+=1
  print(qc,"questions from",filename)
  return questions
  
aq=read_questions("a-klass.txt")
bq=read_questions("b-klass.txt")
dq=read_questions("d-klass.txt")
ij=json.load(open("es2ice.json"))
#pp(aq)
#pp(bq)
#pp(dq)
qc=0
for m in ij["modules"]:
  #print(m["id"],m["title"])
  for q in m["questions"]:
    #print(q["id"],q["text"])
    i=q["id"].split("-")
    module=int(i[0][1:-1])
    qn=int(i[1])
    if module in bq and qn in bq[module]:
      if q["text"]!=bq[module][qn]["?"]:
        print(f"question M{module}-{qn} mismatch:")
        print(" json:",q["text"])
        for a in q["answers"]:
          print(" ",a["text"])
        print(" b.kat:",bq[module][qn]["?"])
        for a in bq[module][qn]:
          if a!='?':
            print(" ",bq[module][qn][a])
      else:
        for a in q["answers"]:
          if a["correct"]:
            ca=a["text"]
            cao=a.get("oldtext",None)
            for aa in bq[module][qn]:
              if aa!="?":
                if bq[module][qn][aa] in (ca,cao):
                  break
            else:
              print(f"cannot identify correct answer to {module}-{qn} {q['text']}")
              print(" should be :",ca)
              print(" options are :")
              for aa in bq[module][qn]:
                if aa!="?":
                  print("    ",bq[module][qn][aa])
    else:
      print(f"no question {module}-{qn} {q['text']}")
    qc+=1

print(qc,"questions from es2ice.json")

#{'id': 'M5B-1', 'text': 'Mis tüüpi sisendsignaali kasutatakse SSB saatja lineaarsuse kontrollimiseks?', 
# 'answers': [{'text': 'Tavalist kõnet.', 'correct': False, 'isChanged': False}, 
#             {'text': 'Helisageduslikku siinuslainet.', 'correct': False, 'isChanged': False}, 
#             {'text': 'Kaht helisageduslikku siinuslainet', 'correct': True}], 'hasProblem': False, 'tags': 'lineaarsus', 'info': '', 'isChanged': False}
