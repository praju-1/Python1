import re

s = """Hello good evening dopted the nickname 'Black Hoe' from his skin color and his work on his parents' farm?"""
# print(type(s))

# result = re.match("good",s)
# print(result)
pattern = "[h]\w{2}"
print(re.findall(pattern,s, re.IGNORECASE))