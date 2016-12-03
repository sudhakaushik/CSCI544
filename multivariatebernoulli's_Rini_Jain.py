import os
import numpy
from pandas import DataFrame
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import BernoulliNB




def build_data_frame(path, classification):
    rows = []
    index = []
    for file_name, text in read_files(path):
        rows.append({'text': text, 'class': classification})
        index.append(file_name)

    data_frame = DataFrame(rows, index=index)
    return data_frame

NEWLINE = '\n'
SKIP_FILES = {'cmds', '_DS_Store'}


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



SAD = 'Sad'
HAPPY = 'Happy'

SOURCES = [
    (r'/Users/Rini/Documents/training_happy_sad/happy', HAPPY),
    (r'/Users/Rini/Documents/training_happy_sad/sad', SAD),
    (r'/Users/Rini/Documents/validation_happy_sad/happy',HAPPY),
    (r'/Users/Rini/Documents/validation_happy_sad/sad',SAD)
]

data = DataFrame({'text': [], 'class': []})
for path, classification in SOURCES:
    data = data.append(build_data_frame(path, classification))
data = data.reindex(numpy.random.permutation(data.index))
count_vectorizer = CountVectorizer()
counts = count_vectorizer.fit_transform(data['text'].values)


classifier = MultinomialNB()
targets = data['class'].values
classifier.fit(counts, targets)



pipeline = Pipeline([
    ('count_vectorizer',   CountVectorizer(ngram_range=(1,  2))),
    ('tfidf_transformer',  TfidfTransformer()),
    ('classifier',         MultinomialNB())
])


from sklearn.cross_validation import KFold
from sklearn.metrics import confusion_matrix, f1_score

k_fold = KFold(n=len(data), n_folds=3)
scores = []
confusion = numpy.array([[0, 0], [0, 0]])
for train_indices, test_indices in k_fold:
    train_text = data.iloc[train_indices]['text'].values
    train_y = [0,1]

    test_text = data.iloc[test_indices]['text'].values
    test_y = [0,1]

    pipeline.fit(train_text, train_y)
    predictions = pipeline.predict(test_text)

    confusion += confusion_matrix(test_y, predictions)
    score = f1_score(test_y, predictions, pos_label=SAD)
    scores.append(score)

print('Total songs classified:', len(data))
print('Score:', sum(scores)/len(scores))
print('Confusion matrix:')
print(confusion)
