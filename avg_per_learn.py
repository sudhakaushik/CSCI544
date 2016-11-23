import sys
import os
import random
import pickle
from collections import defaultdict

filename = sys.argv[1]
i = 0

alpha = 0
b = 0
beta = 0
c = 1

words_weight = defaultdict(int)
avg_words_weight = defaultdict(int)

avg_words_weight['bias_value'] = beta

file_list = []

for subdir, dirs, files in os.walk(filename):
    for file in files:
        if file[len(file)-3:len(file)] == "txt":
            if os.path.basename(subdir) == 'happy':
                with open(os.path.join(subdir, file), 'r', encoding='latin1') as f:
                    file_list.append("happy" + " " + f.read())
            elif os.path.basename(subdir) == 'sad':
                with open(os.path.join(subdir, file), 'r', encoding='latin1') as f:
                    file_list.append("sad" + " " + f.read())



for i in range(0, 30):
    random.shuffle(file_list)
    for file in file_list:
        alpha = 0
        words = file.split()
        if words[0] == "sad":
            y = 1
        elif words[0] == "happy":
            y = -1
        words.pop(0)
        for word in words:
            try:
                alpha += words_weight[word]
            except KeyError:
                words_weight[word] = 0
                avg_words_weight[word] = 0
        alpha += b

        if (alpha * y) <= 0:
            for word in words:
                words_weight[word] += y
                avg_words_weight[word] += (y * c)
            b += y
            beta += (y * c)
        c += 1


for word in words_weight:
    avg_words_weight[word] = words_weight[word] - ((1/c) * avg_words_weight[word])

beta = b - ((1/c) * beta)
avg_words_weight["bias_value"] = beta
pickle.dump(avg_words_weight, open("per_model.txt", "wb"))
