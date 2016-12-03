sad_positive=0
sad_negative=0
happy_positive=0
happy_negative=0

model_file = open("nboutput.txt", 'r', encoding='latin1')
file_data = model_file.read()
lines = file_data.splitlines()
for file in lines:
    words = file.split()
    if words[0] == "SAD":
        if "SAD" in words[1]:
            sad_positive += 1
        else:
            sad_negative += 1
    if words[0] == "HAPPY":
        if "HAPPY" in words[1]:
            happy_positive += 1
        else:
            happy_negative += 1


total = sad_negative+sad_positive+happy_negative+happy_positive
print("sad_negative:",sad_negative)
print("sad_positive:",sad_positive)
print("happy_negative:",happy_negative)
print("happy_positive:",happy_positive)

print("Accuracy:" + (sad_positive+happy_positive)/total)
