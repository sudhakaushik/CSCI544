


from pandas import DataFrame
import numpy
from sklearn.svm import SVC
def build_data_frame(path, classification):
    rows = []
    index = []
    for file_name, text in read_files(path):
        rows.append({'text': text, 'class': classification})
        index.append(file_name)

    data_frame = DataFrame(rows, index=index)
    return data_frame
import os

NEWLINE = '\n'
SKIP_FILES = {'cmds'}


def read_files(path):
    for root, dir_names, file_names in os.walk(path):
        for path in dir_names:
            read_files(os.path.join(root, path))
        for file_name in file_names:
            if file_name not in SKIP_FILES:
                file_path = os.path.join(root, file_name)
                if os.path.isfile(file_path):
                    past_header, lines = False, []
                    f = open(file_path, encoding="latin-1")
                    for line in f:
                        if past_header:
                            lines.append(line)
                        elif line == NEWLINE:
                            past_header = True
                    f.close()
                    content = NEWLINE.join(lines)
                    yield file_path, content


SAD = 'sad'
HAPPY = 'happy'

SOURCES = [
    (r'C:\Users\sue_12\Documents\sad\training_happy_sad\happy', HAPPY),
    (r'C:\Users\sue_12\Documents\sad\training_happy_sad\sad', SAD),
    (r'C:\Users\sue_12\Documents\sad\validation_happy_sad\happy',HAPPY),
    (r'C:\Users\sue_12\Documents\sad\validation_happy_sad\sad',SAD)
]

data = DataFrame({'text': [], 'class': []})
for path, classification in SOURCES:
    data = data.append(build_data_frame(path, classification))

data = data.reindex(numpy.random.permutation(data.index))
import numpy
from sklearn.feature_extraction.text import CountVectorizer

count_vectorizer = CountVectorizer()
counts = count_vectorizer.fit_transform(data['text'].values)
#print(counts)

#examples = ['Free Viagra call today!', "I'm going to attend the Linux users group tomorrow."]
#example_counts = count_vectorizer.transform(examples)

#predictions = classifier.predict(example_counts)
#predictions # [1, 0]

#from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
#from sklearn.naive_bayes import GaussianNB
from sklearn.feature_extraction.text import TfidfTransformer
#from sklearn.naive_bayes import BernoulliNB
pipeline = Pipeline([
    ('count_vectorizer',   CountVectorizer()),
    ('tfidf_transformer',  TfidfTransformer()),
    ('classifier',         SVC(gamma = 'auto', C=3))
])


#pipeline.fit(data['text'].values, data['class'].values
#pipeline.predict(examples)
from sklearn.cross_validation import KFold
from sklearn.metrics import confusion_matrix, f1_score

k_fold = KFold(n=len(data), n_folds=6)
scores = []
scores1 = []
confusion = numpy.array([[0, 0], [0, 0]])
for train_indices, test_indices in k_fold:
    train_text = data.iloc[train_indices]['text'].values
    train_y = data.iloc[train_indices]['class'].values

    test_text = data.iloc[test_indices]['text'].values
    test_y = data.iloc[test_indices]['class'].values
    #train_text = train_text.todense()
    pipeline.fit(train_text, train_y)
    predictions = pipeline.predict(test_text)

    confusion += confusion_matrix(test_y, predictions)
    score = f1_score(test_y, predictions, pos_label=SAD)
    score1 = f1_score(test_y, predictions, pos_label=HAPPY)
    scores.append(score)
    scores1.append(score1)


print('Total songs classified:', len(data))
print('F-Score(SAD):', sum(scores)/len(scores))
print('F-Score(HAPPY)', sum(scores1)/len(scores1))
print('Confusion matrix:')
print(confusion)




