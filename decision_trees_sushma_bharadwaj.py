import os
import nltk
import scipy
import sklearn
from sklearn import tree
import random


file_path = "D:\\data\\train"
#Count to keep track of number of spam files

#Set to maintain the vocabulary of words so that unique existence is present
vocabulary_set=set([])
#Dictionary to keep count of words
happy_word_dict = {}
sad_word_dict = {}
#Variables used later in evaluation
correctly_classified_as_happy = 0
classified_as_happy = 0
correctly_classified_as_sad = 0
classified_as_sad = 0

token_remover = ['a', 'about', 'above', 'after', 'again', 'against', 'all', 'am', 'an', 'and', 'any', 'are', "aren't", 'as', 'at', 'be', 'because', 'been', 'before', 'being', 'below', 'between', 'both', 'but', 'by', "can't", 'cannot', 'could', "couldn't", 'did', "didn't", 'do', 'does', "doesn't", 'doing', "don't", 'down', 'during', 'each', 'few', 'for', 'from', 'further', 'had', "hadn't", 'has', "hasn't", 'have', "haven't", 'having', 'he', "he'd", "he'll", "he's", 'her', 'here', "here's", 'hers', 'herself', 'him', 'himself', 'his', 'how', "how's", 'i', "i'd", "i'll", "i'm", "i've", 'if', 'in', 'into', 'is', "isn't", 'it', "it's", 'its', 'itself', "let's", 'me', 'more', 'most', "mustn't", 'my', 'myself', 'no', 'nor', 'not', 'of', 'off', 'on', 'once', 'only', 'or', 'other', 'ought', 'our', 'ours\tourselves', 'out', 'over', 'own', 'same', "shan't", 'she', "she'd", "she'll", "she's", 'should', "shouldn't", 'so', 'some', 'such', 'than', 'that', "that's", 'the', 'their', 'theirs', 'them', 'themselves', 'then', 'there', "there's", 'these', 'they', "they'd", "they'll", "they're", "they've", 'this', 'those', 'through', 'to', 'too', 'under', 'until', 'up', 'very', 'was', "wasn't", 'we', "we'd", "we'll", "we're", "we've", 'were', "weren't", 'what', "what's", 'when', "when's", 'where', "where's", 'which', 'while', 'who', "who's", 'whom', 'why', "why's", 'with', "won't", 'would', "wouldn't", 'you', "you'd", "you'll", "you're", "you've", 'your', 'yours', 'yourself', 'yourselve']

for directories, subdirectories, files in os.walk(file_path):
    for each_file in files:
        if "happy" in each_file:

            fopen = open(os.path.join(directories,each_file), "r").read()
            word= fopen.split()


            for i in word:
                if i in token_remover:
                    continue
                vocabulary_set.add(i)
                if i not in happy_word_dict:
                    happy_word_dict[i] = 1
                else:
                    happy_word_dict[i] += 1
        elif "sad" in each_file:

            fopen = open(os.path.join(directories,each_file), "r").read()
            word=fopen.split()
            for i in word:
                if i in token_remover:
                    continue
                vocabulary_set.add(i)
                if i not in sad_word_dict:
                    sad_word_dict[i] = 1
                else:
                    sad_word_dict[i] += 1


##############################################################################

#Convert vocab_set to a list
vocab_list=[]

for each in vocabulary_set:
    vocab_list.append(each)
X=[]
Y=[]
for directories, subdirectories, files in os.walk(file_path):
    for each_file in files:
        if "happy" in each_file:
            temp_dict = {}
            inter_list=[]
            fopen = open(os.path.join(directories,each_file), "r").read()
            words= fopen.split()

            for each_word in words:
                if each_word in vocab_list:
                    temp_dict[vocab_list.index(each_word)]=1
            for count in range(0,len(vocab_list)):
                if count in temp_dict.keys():
                    inter_list.append(1)
                else:
                    inter_list.append(0)
            X.append(inter_list)
            Y.append("happy")
        elif "sad" in each_file:
            temp_dict = {}
            inter_list=[]
            fopen = open(os.path.join(directories,each_file), "r").read()
            words= fopen.split()

            for each_word in words:
                if each_word in vocab_list:
                    temp_dict[vocab_list.index(each_word)]=1
            for count in range(0,len(vocab_list)):
                if count in temp_dict.keys():
                    inter_list.append(1)
                else:
                    inter_list.append(0)
            X.append(inter_list)
            Y.append("sad")
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X, Y)
#################################################################################

#############################################################################
#Classifier part

dev_file_path = "D:\\data\\dev"
#Count to keep track of number of spam files
total_happy_files = 0
total_sad_files=0
test_happy=[]
test_sad=[]
for directories, subdirectories, files in os.walk(dev_file_path):
    for each_file in files:
        if "happy" in each_file:
            temp_dict = {}
            inter_list=[]
            fopen = open(os.path.join(directories,each_file), "r").read()
            words= fopen.split()

            for each_word in words:
                if each_word in vocab_list:
                    temp_dict[vocab_list.index(each_word)]=1
            for count in range(0,len(vocab_list)):
                if count in temp_dict.keys():
                    inter_list.append(1)
                else:
                    inter_list.append(0)
            test_happy.append(inter_list)
        elif "sad" in each_file:
            temp_dict = {}
            inter_list=[]
            fopen = open(os.path.join(directories,each_file), "r").read()
            words= fopen.split()

            for each_word in words:
                if each_word in vocab_list:
                    temp_dict[vocab_list.index(each_word)]=1
            for count in range(0,len(vocab_list)):
                if count in temp_dict.keys():
                    inter_list.append(1)
                else:
                    inter_list.append(0)
            test_sad.append(inter_list)
str1= clf.predict(test_happy)
str2=clf.predict(test_sad)

for each in str1:
    total_happy_files += 1
    if each=="happy":
        correctly_classified_as_happy+=1
        classified_as_happy+=1
    else:
        classified_as_happy+=1


for each in str2:
    total_sad_files+=1
    if each == "sad":
        correctly_classified_as_sad += 1
        classified_as_sad += 1
    else:
        classified_as_sad += 1


# print (correctly_classified_as_happy)
# print (correctly_classified_as_sad)
# print (classified_as_happy)
# print (classified_as_sad)
# print (total_happy_files)
# print (total_sad_files)
######################################################################3
#Evaluation of precision, recall and f1
precision_of_happy = float(correctly_classified_as_happy)/float(classified_as_happy)
precision_of_sad = float(correctly_classified_as_sad)/float(classified_as_sad)
recall_of_happy = float(correctly_classified_as_happy)/ float(total_happy_files)
recall_of_sad = float(correctly_classified_as_sad)/ float(total_sad_files)
f_score_of_happy = float(2*precision_of_happy*recall_of_happy)/float(precision_of_happy+recall_of_happy)
f_score_of_sad = float(2*precision_of_sad*recall_of_sad)/float(precision_of_sad+recall_of_sad)
print ("Precision of happy: ",precision_of_happy)
print ("Precision of sad: ",precision_of_sad)
print ("Recall of happy: ",recall_of_happy)
print ("Recall of sad: ",recall_of_sad)
print ("F score of happy: ",f_score_of_happy)
print ("F score of sad: ",f_score_of_sad)






