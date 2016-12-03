import sys
import os

file_path = "D:\\data\\dev"
output_file_path = 'avg_perceptron_output_sushma_bharadwaj.txt'

final_weight_dict={}
ptr_to_learn = open('avg_per_model_sushma_bharadwaj.txt','r')
for every_line in ptr_to_learn:
    all_data=every_line.strip().split(' ')
    final_weight_dict[all_data[0]]= all_data[1]
#print (final_weight_dict)
beta_or_bias_val = float(final_weight_dict["beta_or_bias_value"])
######Variables used for calculation of accuracy
correctly_classified_as_happy = 0
classified_as_happy = 0
correctly_classified_as_sad = 0
classified_as_sad = 0
total_happy_files = 0
total_sad_files = 0

for dirs,subdir,files in os.walk(file_path):
    for file in files:
        if 'sad' in file:
            total_sad_files+=1
        elif 'happy' in file:
            total_happy_files+=1


f=open(output_file_path,'w')

for directories, subdirectories, files in os.walk(file_path):
    for each_file in files:
        if ".txt" in each_file:
            abs_path = os.path.join(directories,each_file)
            file = open(abs_path, "r").read()
            tokens = file.split()
            summation=0
            for every_token in tokens:
                if every_token in final_weight_dict.keys():
                    next_u_w = float(final_weight_dict[every_token])
                else:
                    next_u_w=0
                summation = summation+next_u_w
            alpha = summation+beta_or_bias_val
            if alpha > 0:
                line = "happy"+" "+abs_path
                f.write(line)
                f.write('\n')
                classified_as_happy+=1
                if "happy" in each_file:
                    correctly_classified_as_happy+=1
            else:
                line = "sad"+" "+abs_path
                f.write(line)
                f.write('\n')
                classified_as_sad+=1
                if "sad" in each_file:
                    correctly_classified_as_sad+=1

f.close()

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
