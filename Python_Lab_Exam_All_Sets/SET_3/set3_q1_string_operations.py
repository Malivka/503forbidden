
quote = "In the middle of difficulty lies opportunity"

# word count
print("Word count:", len(quote.split()))

# remove vowels
vowels = "aeiouAEIOU"
new = ""
for ch in quote:
    if ch not in vowels:
        new += ch
print("Without vowels:", new)

# replace word
print("Replaced:", quote.replace("difficulty", "challenge"))

# sort words by length
words = quote.split()
words.sort(key=len)
print("Sorted by length:", words)
