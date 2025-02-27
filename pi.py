text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO
#list(map(len,["a","bc","def"]))
cleantext = text.replace(",","")
cleantext = cleantext.replace(".","")
words = cleantext.split()
wordscountlist=list(map(len,list(words)))
result=''.join(map(str,wordscountlist))
print(result)



