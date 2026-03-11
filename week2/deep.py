import sys
question=input('What is the Answer to the Great Question of Life, the Universe, and Everything?')
answer=question.strip().lower().replace('-','')
if answer in {"42",'forty two'}:
    print('yes')
else:
    print('no')