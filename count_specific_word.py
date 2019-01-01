
message = "This is the test of counting the occurance of word. How many time each word  repeated this  time i wont allow you to this time"

word1 = "time"

message = message.split(" ")

count = {}

for word in message:
    if word == word1:
        count.setdefault(word1,0)
        count[word1] = count[word1] + 1

print count
