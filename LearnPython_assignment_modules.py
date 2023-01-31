import re
find_members = []
for x in dir(re):
    if "find" in x:
        find_members.append(x)
for x in find_members:
    print(x)