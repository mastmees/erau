import sys
import os
import re

klass="A"
lang="et"

if len(sys.argv)>1:
  klass=sys.argv[1][0].upper()

def meta(dir):
  m={}
  if os.path.exists(os.path.join(dir,"meta."+lang)):
    for l in open(os.path.join(dir,"meta."+lang),"rt").readlines():
      l=l.strip()
      e=l.split(" ",1)
      m[e[0].strip()]=e[1].strip()
  return m
  
def get_title(dir):
  return meta(dir).get("T","")

def get_author(dir):
  return meta(dir).get("A","")
    
def get_content(dir):
  if os.path.exists(os.path.join(dir,"content."+lang)):
    return open(os.path.join(dir,"content."+lang),"rt").read()
  return ""
  
def get_questions(dir,klass):
  result=[]
  for fn in sorted(filter(lambda x: re.search("^q[0-9]*."+lang,x),os.listdir(dir) ) ):
    q={}
    for l in open(os.path.join(dir,fn),"rt").readlines():
      e=l.split(" ",1)
      q[e[0][0]]=e[1].strip()
    if "." in q and klass in q["."]:
      result.append(q)
  return result
  
chapters=list(filter(lambda x: re.search("^C[0-9][0-9]",x),os.listdir(".")))
if chapters:
  print("# "+get_title("."))
  print("# "+klass+"-kategooria")
  print(get_author("."))
  print(get_content("."))
for chapter in sorted(chapters):
  sections=list(filter(lambda x: re.search("^S[0-9][0-9]",x),os.listdir(os.path.join(".",chapter))))
  allquestions={}
  chapterquestions=get_questions(os.path.join(".",chapter),klass)
  for section in sorted(sections):
    s=os.path.join(".",chapter,section)
    q=get_questions(s,klass)
    if q:
      allquestions[section]=q
  if allquestions or chapterquestions:
    print("# "+chapter+" "+get_title(chapter))
    print(get_content(chapter))
    if chapterquestions:
      print("---")
      print("***Kordamisküsimused***")
      for question in chapterquestsions:
        print("* "+question["?"])
      
    for section in sorted(allquestions.keys()):
      s=os.path.join(".",chapter,section)
      print("## "+section+" "+get_title(s))
      print(get_content(s))
      print("---")
      print("***Kordamisküsimused***")
      for question in allquestions[section]:
        print("* "+question["?"])
    print("")
     
