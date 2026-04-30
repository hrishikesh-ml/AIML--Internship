count=0
vowel='aeiou'
name=input('enter the name')
for i in name:
    if i in vowel:
        count=count+1
print(count)