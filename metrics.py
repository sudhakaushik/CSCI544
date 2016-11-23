import sys
import os

filename = sys.argv[1]
op_file = sys.argv[2]
ham = 0
ham_count = 0
spam = 0
spam_count = 0
actual_ham = 0
actual_spam = 0

f = open(op_file, 'r', encoding='latin1')
for line in f:
    words = line.split()
    if words[0] == 'HAPPY':
        ham = ham+1
        if words[1].__contains__('happy'):
            ham_count = ham_count+1
    elif words[0] == 'SAD':
        spam = spam+1
        if words[1].__contains__('sad'):
            spam_count = spam_count+1

for subdir, dirs, files in os.walk(filename):
    for file in files:
        if file.__contains__('.txt'):
            if os.path.basename(subdir) == 'happy':
                actual_ham = actual_ham +1
            elif os.path.basename(subdir) == 'sad':
                actual_spam = actual_spam +1

#print(spam)
#print(ham)
#print(spam_count)
#print(ham_count)
#print(actual_ham)
#print(actual_spam)

spam_precision = round((spam_count/spam),2)
ham_precision =  round((ham_count/ham),2)

spam_recall =  round((spam_count/actual_spam),2)
ham_recall =  round((ham_count/actual_ham),2)

spam_f1 =  round(((2*spam_precision*spam_recall)/(spam_precision+spam_recall)),2)
ham_f1 =  round(((2*ham_precision*ham_recall)/(ham_precision+ham_recall)),2)

print('sad precision: ' + str(spam_precision))
print('sad recall: ' + str(spam_recall))
print('sad F1 score: ' + str(spam_f1))

print('happy precision: '+ str(ham_precision))
print('happy recall: ' + str(ham_recall))
print('happy F1 score: ' + str(ham_f1))