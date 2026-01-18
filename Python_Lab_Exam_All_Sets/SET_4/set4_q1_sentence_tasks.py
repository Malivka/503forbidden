
sentence="The quick brown fox jumps over the lazy dog"

# remove duplicates
res=""
for ch in sentence:
    if ch not in res:
        res+=ch
print("No duplicates:",res)

# frequency
freq={}
for ch in sentence.lower():
    if ch!=" ":
        freq[ch]=freq.get(ch,0)+1
print(freq)

# longest word and vowel count
words=sentence.split()
long=words[0]
for w in words:
    if len(w)>len(long):
        long=w
count=0
for ch in long:
    if ch in "aeiouAEIOU":
        count+=1
print("Longest:",long,"Vowels:",count)

# reverse word order
rev=" ".join(sentence.split()[::-1])
print("Reversed words:",rev)
