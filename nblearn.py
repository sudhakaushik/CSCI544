import sys
import os
import math

happy_file_count = 0
sad_file_count = 0
stoplist = []
happy_dict = {}
sad_dict = {}
unique_words = set()


stoplist = []

file2 = open('stop.txt', 'r')
for line in file2:
    w = line.split()
    for word in w:
        stoplist.append(word)
def getClass(fileLocation):
    if 'happy' in fileLocation.split('/')[-2]:
        return 'happy'
    elif 'sad' in fileLocation.split('/')[-2]:
        return 'sad'

def wordCount(dict):
    total_count = 0
    for word, count in dict.items():
        total_count += count

    return total_count

def getAllwords(rootFolder):
    mails = []
    for root, dirs, files in os.walk(rootFolder, topdown=False):
        for name in files:
            if name.endswith(".txt"):
                mails.append(os.path.join(root, name))
    return mails

def learn(fileLocation):
    global happy_file_count, sad_file_count

    fileObj = open(fileLocation,"r", encoding="latin1")

    NBclass = getClass(fileLocation)

    if NBclass == 'happy':
        happy_file_count += 1
    else:
        sad_file_count += 1

    mail = fileObj.read().split()
    for mailWord in mail:
        if word in stoplist: continue
        else:

            unique_words.add(mailWord)
            if NBclass == 'happy':
                if mailWord in happy_dict:
                    happy_dict[mailWord] += 1
                else:
                    happy_dict[mailWord] = 1
            else:
                if mailWord in sad_dict:
                    sad_dict[mailWord] += 1
                else:
                    sad_dict[mailWord] = 1

if len(sys.argv) != 2:
    print("Missing the location of the training data")
else:
    rootFolder = sys.argv[1]
    mails = getAllwords(rootFolder)
    for mail in mails:
        learn(mail)




for word in unique_words:
    if word not in happy_dict:
        happy_dict[word] = 0
    if word not in sad_dict:
        sad_dict[word] = 0

for word, count in happy_dict.items():
    happy_dict[word] += 1

for word, count in sad_dict.items():
    sad_dict[word] += 1

happy_count = wordCount(happy_dict)
sad_count = wordCount(sad_dict)

output = open('nbmodel.txt', "w")

happy_prior = happy_file_count / (happy_file_count + sad_file_count)
sad_prior = sad_file_count / (happy_file_count + sad_file_count)
output.write(str(happy_prior) + '\n')
output.write(str(sad_prior) + '\n')

for word, count in happy_dict.items():
    output.write(word + '::' + 'happy' + '::' + str(math.log(count/happy_count)) + '\n')

for word, count in sad_dict.items():
    output.write(word + '::' + 'sad' + '::' + str(math.log(count / sad_count)) + '\n')


file2.close()