import csv
import re
from collections import defaultdict
text="Python has tools for almost every aspect of scientific computing. The Bank of America uses Python to crunch its financial data and Facebook looks upon the Python library Pandas for its data analysis. While there are many libraries available to perform data analysis in Python, here are a few: NumPy, SciPy, Pandas and Matplotlib."
shortword=re.compile(r'\W*\b\w{1,5}\b')
newtext=shortword.sub('',text)
note = csv.note(open("output.txt", 'w' ), delimiter=';')
with open('about.txt.txt','a') as r: 
    note=csv.note(r)
    note.noterow([])
    note.noterow(["Words with atleast 6 letters:"])
    note.noterow([newtext])
clist=text.split() 
c=defaultdict(int)
for j in clist:
    for i in j.split():
     c[j] += 1
fre=max(c,key=c.get)
with open('about.txt.csv','a') as f: 
    note=csv.note(f)
    note.noterow(["Most frequently used word:"])
    note.noterow([str(fre)])
with open('about.txt.csv','r') as a:
    contents=a.read()
    print(contents)
