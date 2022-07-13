def countoccurence(str,word):
    wordlist = list(str.split())
    return wordlist.count(word)

str = " I am Aubaid Nabi LONE.I am from Kashmir. "    
word1 = "am"
print(countoccurence(str,word1))