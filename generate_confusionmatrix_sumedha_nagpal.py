
import sys
import os
from sklearn.metrics import confusion_matrix, f1_score

path = sys.argv[1]
confusion = numpy.array([[0, 0], [0, 0]])
f = open(path, 'r')
for i in f:
	confusion += confusion_matrix(i[0], i[1]) #confusion_matrix(test_y, predictions)
	score = f1_score(i[0], i[1], pos_label=SAD)
	score1 = f1_score(i[0], i[1], pos_label=HAPPY)
	score_sad.append(score_sad)
	score_happy.append(score_happy)


print('Total songs classified:', len(data))
print('Confusion matrix:')
print(confusion)
print('F-Score(SAD):', sum(score_sad)/len(score_sad))
print('F-Score(HAPPY)', sum(scores_happy)/len(score_happy))

