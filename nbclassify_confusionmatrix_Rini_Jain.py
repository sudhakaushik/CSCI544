import sys
import os
countphappy=0
countpsad=0
happy_prior = 0
sad_prior = 0
count_of_happy=0
count_of_sad=0
happy_dict = {}
sad_dict = {}
count_of_happy_prec=0
count_of_sad_prec=0
input_arr=[]
prob_arr=[]
with open('nbmodel.txt') as file:
    lines = file.readlines()

    happy_prior = float(lines[0].strip())
    sad_prior = float(lines[1].strip())

    for line in lines[2:]:
        lineContent = line.split('::')

        word = lineContent[0]
        NBclass = lineContent[1]
        prob = float(lineContent[2])

        if NBclass == 'happy':
            happy_dict[word] = prob
        else:
            sad_dict[word] = prob

def classifymail(fileLocation):
    global count_of_happy, count_of_sad, count_of_happy_prec,count_of_sad_prec
    global happy_dict, sad_dict, happy_prior, sad_prior
    global countphappy,countpsad
    happy_prob = happy_prior
    sad_prob = sad_prior

    with open(fileLocation,"r", encoding="latin1") as testData:
        mail = testData.read().split()
        if 'happy' in fileLocation:
            count_of_happy = count_of_happy + 1
        else:
            count_of_sad = count_of_sad + 1
        for word in mail:
            if word in happy_dict:
                happy_prob += happy_dict[word]
                sad_prob += sad_dict[word]
        if happy_prob>sad_prob and 'happy' in fileLocation:
            count_of_happy_prec=count_of_sad_prec+1
        elif sad_prob>happy_prob and 'sad' in fileLocation:
            count_of_sad_prec=count_of_sad_prec+1

        if happy_prob > sad_prob:
            countphappy=countphappy+1
            return 'happy ' + fileLocation
        else:
            countpsad=countpsad+1
            return 'sad ' + fileLocation


def getAllwords(rootFolder):

    mails = []
    for root, dirs, files in os.walk(rootFolder, topdown=False):
        for name in files:
            if name.endswith(".txt"):
                mails.append(os.path.join(root, name))
    return mails
if len(sys.argv) != 2:
    print("Missing the location of the test data")
else:
    rootFolder = sys.argv[1]
    mails = getAllwords(rootFolder)

    output = open('nboutput.txt', 'w')
    for mail in mails:
        output.write(classifymail(mail) + '\n')

precisionhappy=round(countphappy/count_of_happy_prec,2)
precisionsad=round(countpsad/count_of_sad_prec,2)



recallhappy=round(countphappy/count_of_happy,2)
recallsad=round(countpsad/count_of_sad,2)

f1happy=round((2*precisionhappy*recallhappy)/(precisionhappy+recallhappy),2)
f1sad=round((2*precisionsad*recallsad)/(precisionsad+recallsad),2)
if(f1happy):
    prob_arr[0]=f1happy
    input_arr[0]='Happy'
else:
    prob_arr[1]=f1sad
    input_arr[1]='Sad'


    def conf_mat(prob_arr, input_arr):
        # confusion matrix
        conf_arr = [[0, 0], [0, 0]]

        for i in range(len(prob_arr)):
            if int(input_arr[i]) == 1:
                if float(prob_arr[i]) < 0.5:
                    conf_arr[0][1] = conf_arr[0][1] + 1
                else:
                    conf_arr[0][0] = conf_arr[0][0] + 1
            elif int(input_arr[i]) == 2:
                if float(prob_arr[i]) >= 0.5:
                    conf_arr[1][0] = conf_arr[1][0] + 1
                else:
                    conf_arr[1][1] = conf_arr[1][1] + 1

        accuracy = float(conf_arr[0][0] + conf_arr[1][1]) / (len(input_arr))

