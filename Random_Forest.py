from sklearn.ensemble import RandomForestClassifier
import sys
import os
import numpy

filename = sys.argv[1]
file_test = sys.argv[2]
opfile = sys.argv[3]
Ylist = []
Xlist = []
all_words = set()
word_dict = dict()

a = open(opfile,"w")

for subdir, dirs, files in os.walk(filename):
    for file in files:
        if file[len(file)-3:len(file)] == "txt":
            if os.path.basename(subdir) == 'happy':
                with open(os.path.join(subdir, file), 'r', encoding='latin1') as f:
                    line = f.read()
                    type = ["happy"]

            elif os.path.basename(subdir) == 'sad':
                with open(os.path.join(subdir, file), 'r', encoding='latin1') as f:
                    line = f.read()
                    type = ["sad"]

            words_list = line.split()
            words = set(words_list)
            for each in words:
                each = each.lower().strip()
            for each in words:
                if each.isalpha():
                    all_words.add(each)
            words = list(words)
            word_dict[file] = type+words


#Ylist.append(type)
#Xlist.append(words)

for each in word_dict:
    present = []
    new_list = word_dict[each]
    type = new_list[0]
    new_list.remove(type)
    for e in all_words:
        if new_list.count(e)>0:
            present.append(1)
        else:
            present.append(0)

    Ylist.append(type)
    Xlist.append(numpy.array(present))


clf = RandomForestClassifier(n_estimators=10)

clf = clf.fit(Xlist, Ylist)


for subdir, dirs, files in os.walk(file_test):
    for file in files:
        if file[len(file)-3:len(file)] == "txt":
            with open(os.path.join(subdir, file), 'r', encoding='latin1') as f:
                line = f.read()

            words_list = line.split()
            words = set(words_list)
            for each in words:
                each = each.lower().strip()
            present = []
            words = list(words)
            for e in all_words:
                if words.count(e) > 0:
                    present.append(1)
                else:
                    present.append(0)

            output = clf.predict(numpy.array(present).reshape(1,-1))
            a.write((" ".join(str(s).upper() for s in output))+' '+ os.path.join(subdir, file) + '\n')