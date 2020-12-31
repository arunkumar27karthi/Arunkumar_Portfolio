import random

words = open('words.txt')
score = 0
total_quess = 0
chance = 0
def quess(word1,num,letter):
    if word1[num]==letter:
        return 'yes'
    else:
        return 'false'
    
for word in words:
    total_quess += 1
    word=word.rstrip()
    lenth = len(word)
    list1=[]
    for i in range(lenth):
        list1.append(word[i])
    
    n = random.randint(0,lenth-1)
    org_letter = list1[n]
    find = list1
    #print(find)
    find[n]='_'
    #print(find)
    find = ''.join(find)
    #print(find)
    
    print('word: ',find)
    
    quess_letter = input('letter: ')
    result = quess(word,n,quess_letter)
    if result=='yes':
        
        score+=1
    elif result=='false':
        print(result,' retry...')
        quess_letter = input('letter: ')
        result = quess(word,n,quess_letter)
        
    print(result)
    
print('you got {0} points out of {1}'.format(score,total_quess))
