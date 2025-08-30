import re
text = "The quick brown fox jumps over the lazy brown dog." 
# match =  re.search("brown",text)
# print(match)
# if match:
#     print("match found")
#     print("Start index",match.start())
#     print("end index",match.end())


# match = re.findall("the",text,re.IGNORECASE)
# print("matches :",match)

new_text = re.sub("brown","black",text)
print("new_text:",new_text)