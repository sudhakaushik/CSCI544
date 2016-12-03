import sys
import os
import random
import pickle
from collections import defaultdict

filename = sys.argv[1]
i = 0

alpha = 0
b = 0

words_weight = defaultdict(int)
words_weight['bias_value'] = b

file_list = []

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

            words = line.split()
            file_list.append(type + words)

for i in range(0, 20):
    random.shuffle(file_list)
    for file in file_list:
        alpha = 0
        each = list(file)
        if each[0] == "sad":
            y = 1
        elif each[0] == "happy":
            y = -1

        each.pop(0)

        for word in each:
            try:
                alpha += words_weight[word]
            except KeyError:
                words_weight[word] = 0

        alpha += b
        if (alpha * y) <= 0:
            for word in each:
                words_weight[word] += y
            b += y

words_weight["bias_value"] = b

#for each in words_weight:
 #   print(each+ " "+ str(words_weight[each]))
#print(words_weight)
pickle.dump(words_weight, open("per_model.txt", "wb"))

