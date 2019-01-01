
message = "it is the test for count the character occurence in this string"

count = {}
print message
for character in message:
    count.setdefault(character,0)
    count[character] = count[character] + 1
print count

message = "it is the test for count the character occurence in this string"

count = {}
print message
for character in message.upper():
        count.setdefault(character,0)
        count[character] = count[character] + 1

print count

