import sqlite3

conn = sqlite3.connect('/Users/Rini/Downloads/growing_training (2).sqlite')
print ("Opened database successfully")

countsad=1
counthappy=1
cursor = conn.execute("SELECT lyrics,mood from moodtable")
for row in cursor:
    if(str(row[1])=='sad'):
        myfile = "song" + '_' + str(countsad) + '_' + str(row[1]) + ".txt"
        countsad=countsad+1
        myf = "/Users/Rini/Documents/training_happy_sad/sad/" + myfile
        f = open(myf, 'w')
        f.write(row[0])

    else:
        myfile = "song" + '_' + str(counthappy) + '_' + str(row[1]) + ".txt"
        counthappy = counthappy + 1
        myf = "/Users/Rini/Documents/training_happy_sad/happy/" + myfile
        f = open(myf, 'w')
        f.write(row[0])

# print "Operation done successfully";
conn.close()