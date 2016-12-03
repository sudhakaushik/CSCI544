import os
import pickle
from math import log10
import sys
import json
import random

file_path = "D:\\data\\train"

#Dictionary to keep words
dict_of_all_words={}
#Dictionary to keep initial weights
weight_dict={}
#Dictionary to keep initial values of 'u' (Average weights)
u_dict={}
#Counter to keep track of number of files
count_of_file = 1
counter = 1 # Variable c used in algorithm
#Traverse through the directories
for directories, subdirectories, files in os.walk(file_path):
    for each_file in files:
         if "happy" in each_file:
            fopen = open(os.path.join(directories, each_file), "r").read()
            word = fopen.split()
            if count_of_file not in dict_of_all_words.keys():
                dict_of_all_words[count_of_file]={}
                dict_of_all_words[count_of_file]["happy"] = word
            else:
                dict_of_all_words[count_of_file]["happy"] = word
            count_of_file += 1
            for each_word in word:
                if each_word not in weight_dict.keys():
                    weight_dict[each_word]=0
                if each_word not in u_dict.keys():
                    u_dict[each_word]=0


         elif "sad" in each_file:
            fopen = open(os.path.join(directories, each_file), "r").read()
            word = fopen.split()
            if count_of_file not in dict_of_all_words.keys():
                dict_of_all_words[count_of_file]={}
                dict_of_all_words[count_of_file]["sad"] = word
            else:
                dict_of_all_words[count_of_file]["sad"] = word
            count_of_file += 1
            for each_word in word:
                if each_word not in weight_dict.keys():
                    weight_dict[each_word] = 0
                if each_word not in u_dict.keys():
                    u_dict[each_word]=0

#Randomise the input given to the perceptron algorithm
list_of_indices=[]
for each_index in dict_of_all_words.keys():
    list_of_indices.append(each_index)
random.shuffle(list_of_indices)

#Perceptron Algorithm implementation
bias = 0
beta = 0
for iteration_value in range(0,30):
    for index_value in list_of_indices:
        sum_of_weights = 0
        check_if_spam_or_ham = dict_of_all_words[index_value]
        for keys in check_if_spam_or_ham:
            if keys == "happy":
                for each_word_weight in dict_of_all_words[index_value][keys]:
                    sum_of_weights = sum_of_weights + weight_dict[each_word_weight]
                alpha = sum_of_weights + bias
                if 1 * alpha <= 0:
                    for each_word_weight in dict_of_all_words[index_value][keys]:
                            weight_dict[each_word_weight] = weight_dict[each_word_weight] + 1
                            u_dict[each_word_weight] = u_dict[each_word_weight] + (1*counter)
                    bias = bias + 1
                    beta = beta + (1*counter)
            elif keys == "sad":
                for each_word_weight in dict_of_all_words[index_value][keys]:
                    sum_of_weights = sum_of_weights + weight_dict[each_word_weight]
                alpha = sum_of_weights + bias
                if -(1 * alpha) <= 0:
                    for each_word_weight in dict_of_all_words[index_value][keys]:
                        weight_dict[each_word_weight] = weight_dict[each_word_weight] - 1
                        u_dict[each_word_weight] = u_dict[each_word_weight] + ((-1)*counter)
                    bias = bias - 1
                    beta = beta + ((-1) * counter)
            counter = counter+1
#print (bias)
#Final update of u_dict and beta
beta = bias-((1/counter)*beta)
for every_word in u_dict:
    u_dict[every_word] = weight_dict[every_word]-((1/counter)*u_dict[every_word])

f=open('avg_per_model_sushma_bharadwaj.txt','w')
line = "beta_or_bias_value"+" "+str(beta)
f.write(line)
f.write('\n')
for weight in u_dict:
    line = weight+" "+str(u_dict[weight])
    f.write(line)
    f.write('\n')
f.close()
