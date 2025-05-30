text="python is easy and python is powerful"

"""
{'python':2,'is':2,'easy':1, 'and':1,'powerful':1}
"""

word_count={}
for word in text.split(" "):
    word_count[word] = word_count.get(word,0)+1

print(word_count)
#{'python':2, 'is':2, 'easy':1, 'and':1,'powerful':1}
