
message = "This is the test of counting the occurance of word. How many time each word  repeated"

message = message.split(" ")
#print message
countWord = {}
for word in message:
    countWord.setdefault(word,0)
    countWord[word] = countWord[word] + 1

print countWord


