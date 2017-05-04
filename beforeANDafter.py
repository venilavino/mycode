s=raw_input()
word=s.split()
i=0
for i in range(len(word)):
    if(word[i]=='and'):
        temp=word[i-1]
        word[i-1]=word[i+1]
        word[i+1]=temp
i=0
for i in range(len(word)):
    print word[i],
