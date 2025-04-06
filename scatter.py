import re
import json
from pprint import pprint as pp
import os

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
    elif l[0] in "ABCDE" and l[1] in ".*"  and l[2] in ". ":
      p=l.partition(" ")
      questions[qm][qn][p[0].strip(".")]=p[2].strip()
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
problems=0
for m in ij["modules"]:
  #print(m["id"],m["title"])
  for q in m["questions"]:
    #print(q["id"],q["text"])
    i=q["id"].split("-")
    module=int(i[0][1:-1])
    qn=int(i[1])
    if module in bq and qn in bq[module]:
      if q["text"]!=bq[module][qn]["?"]:
        problems+=1
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
              problems+=1
              print(f"cannot identify correct answer to {module}-{qn} {q['text']}")
              print(" should be :",ca)
              print(" options are :")
              for aa in bq[module][qn]:
                if aa!="?":
                  print("    ",bq[module][qn][aa])
    else:
      problems+=1
      print(f"no question {module}-{qn} {q['text']}")
    qc+=1

print(qc,"questions from es2ice.json")
print(problems,"problems")

"""
  "modules": [
    {
      "id": "M1B",
      "title": "M1B Raadio- ja elektrotehnika teooria",
      "maxQuestions": 5,
      "questions": [
        {
          "id": "M1B-1",
          "text": "Mida tähendab termin impedants?",
          "answers": [
            {
              "text": "Kondensaatoris salvestatavat elektrilaengut.",
              "correct": false,
              "isChanged": false
            },
            {
              "text": "Vooluringi poolt vahelduvvoolule osutatavat takistust.",
              "correct": true,
              "isChanged": false
            },
            {
              "text": "Mahtuvust sisaldava vooluringi poolt vahelduvvoolule osutatavat takistust.",
              "correct": false,
              "isChanged": false
            }
          ],
          "hasProblem": false,
          "tags": "impedants",
"""          
def correct_answer(question,answer):
  for module in ij["modules"]:
    if module["id"]==f"M{int(chapter)}B":
      for q in module["questions"]:
        if q["text"]==question:
          for a in q["answers"]:
            if a["text"]==answer and a["correct"]:
              return True
  return False

def chapter_name(chapter):
  for module in ij["modules"]:
    if module["id"]==f"M{int(chapter)}B":
      t=module["title"].split()
      return " ".join(t[1:])
  return ""

if not problems:
  for chapter in sorted(bq.keys()):
    for qn in sorted(bq[chapter].keys()):
      print(chapter,qn)
      question=bq[chapter][qn]
      dn=f"C{chapter:02d}"
      if not os.path.exists(dn):
        os.mkdir(dn)
      with open(os.path.join(dn,"meta.et"),"wt") as f:
        f.write(f"T {chapter_name(chapter)}\n")
      with open(os.path.join(dn,f"q{qn:03d}.et"),"wt") as f:
        for a in sorted(question.keys()):
          if a=="?":
            s=""
          elif a.endswith('*') or correct_answer(question["?"],question[a]):
            s="*."
          else:
            s="." 
          f.write(f"{a[0]}{s} {question[a]}\n")
        f.write(". AB\n")

  for chapter in sorted(dq.keys()):
    for qn in sorted(dq[chapter].keys()):
      print(chapter,qn)
      question=dq[chapter][qn]
      dn=f"C{chapter:02d}"
      if not os.path.exists(dn):
        os.mkdir(dn)
      with open(os.path.join(dn,"meta.et"),"wt") as f:
        f.write(f"T {chapter_name(chapter)}\n")
      with open(os.path.join(dn,f"q{qn:03d}.et"),"wt") as f:
        for a in sorted(question.keys()):
          if a=="?":
            s=""
          elif a.endswith('*') or correct_answer(question["?"],question[a]):
            s="*."
          else:
            s="." 
          f.write(f"{a[0]}{s} {question[a]}\n")
        f.write(". D\n")

#21: {'?': 'Amatöörraadiojaama alaline (kohtpaikne) kasutamine väljaspool selle registreeritud asukohta ilma tööloa muutmiseta on lubatud:', 'A': 'Kolm kuud.', 'B': 'Viis kuud.', 'C': 'Kuus kuud.', 'D': 'Üks aasta.'}}
        

#{'id': 'M5B-1', 'text': 'Mis tüüpi sisendsignaali kasutatakse SSB saatja lineaarsuse kontrollimiseks?', 
# 'answers': [{'text': 'Tavalist kõnet.', 'correct': False, 'isChanged': False}, 
#             {'text': 'Helisageduslikku siinuslainet.', 'correct': False, 'isChanged': False}, 
#             {'text': 'Kaht helisageduslikku siinuslainet', 'correct': True}], 'hasProblem': False, 'tags': 'lineaarsus', 'info': '', 'isChanged': False}
