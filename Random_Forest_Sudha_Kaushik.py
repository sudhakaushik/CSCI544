from sklearn.ensemble import RandomForestClassifier
import sys
import os
import numpy

filename = sys.argv[1]
file_test = sys.argv[2]
opfile = sys.argv[3]
Ylist = []
Xlist = []
all_words = set()
word_dict = dict()

stop_words = {"a","able","about","above","abst","accordance","according","accordingly","across","act","actually","added","adj","affected","affecting","affects","after","afterwards","again","against","ah","all","almost","alone","along","already","also","although","always","am","among","amongst","an","and","announce","another","any","anybody","anyhow","anymore","anyone","anything","anyway","anyways","anywhere","apparently","approximately","are","aren","arent","arise","around","as","aside","ask","asking","at","auth","available","away","awfully","b","back","be","became","because","become","becomes","becoming","been","before","beforehand","begin","beginning","beginnings","begins","behind","being","believe","below","beside","besides","between","beyond","biol","both","brief","briefly","but","by","c","ca","came","can","cannot","can't","cause","causes","certain","certainly","co","com","come","comes","contain","containing","contains","could","couldnt","d","date","did","didn't","different","do","does","doesn't","doing","done","don't","down","downwards","due","during","e","each","ed","edu","effect","eg","eight","eighty","either","else","elsewhere","end","ending","enough","especially","et","et-al","etc","even","ever","every","everybody","everyone","everything","everywhere","ex","except","f","far","few","ff","fifth","first","five","fix","followed","following","follows","for","former","formerly","forth","found","four","from","further","furthermore","g","gave","get","gets","getting","give","given","gives","giving","go","goes","gone","got","gotten","h","had","happens","hardly","has","hasn't","have","haven't","having","he","hed","hence","her","here","hereafter","hereby","herein","heres","hereupon","hers","herself","hes","hi","hid","him","himself","his","hither","home","how","howbeit","however","hundred","i","id","ie","if","i'll","im","immediate","immediately","importance","important","in","inc","indeed","index","information","instead","into","invention","inward","is","isn't","it","itd","it'll","its","itself","i've","j","just","k","keep	keeps","kept","kg","km","know","known","knows","l","largely","last","lately","later","latter","latterly","least","less","lest","let","lets","like","liked","likely","line","little","'ll","look","looking","looks","ltd","m","made","mainly","make","makes","many","may","maybe","me","mean","means","meantime","meanwhile","merely","mg","might","million","miss","ml","more","moreover","most","mostly","mr","mrs","much","mug","must","my","myself","n","na","name","namely","nay","nd","near","nearly","necessarily","necessary","need","needs","neither","never","nevertheless","new","next","nine","ninety","no","nobody","non","none","nonetheless","noone","nor","normally","nos","not","noted","nothing","now","nowhere","o","obtain","obtained","obviously","of","off","often","oh","ok","okay","old","omitted","on","once","one","ones","only","onto","or","ord","other","others","otherwise","ought","our","ours","ourselves","out","outside","over","overall","owing","own","p","page","pages","part","particular","particularly","past","per","perhaps","placed","please","plus","poorly","possible","possibly","potentially","pp","predominantly","present","previously","primarily","probably","promptly","proud","provides","put","q","que","quickly","quite","qv","r","ran","rather","rd","re","readily","really","recent","recently","ref","refs","regarding","regardless","regards","related","relatively","research","respectively","resulted","resulting","results","right","run","s","said","same","saw","say","saying","says","sec","section","see","seeing","seem","seemed","seeming","seems","seen","self","selves","sent","seven","several","shall","she","shed","she'll","shes","should","shouldn't","show","showed","shown","showns","shows","significant","significantly","similar","similarly","since","six","slightly","so","some","somebody","somehow","someone","somethan","something","sometime","sometimes","somewhat","somewhere","soon","sorry","specifically","specified","specify","specifying","still","stop","strongly","sub","substantially","successfully","such","sufficiently","suggest","sup","sure","take","taken","taking","tell","tends","th","than","thank","thanks","thanx","that","that'll","thats","that've","the","their","theirs","them","themselves","then","thence","there","thereafter","thereby","thered","therefore","therein","there'll","thereof","therere","theres","thereto","thereupon","there've","these","they","theyd","they'll","theyre","they've","think","this","those","thou","though","thoughh","thousand","throug","through","throughout","thru","thus","til","tip","to","together","too","took","toward","towards","tried","tries","truly","try","trying","ts","twice","two","u","un","under","unfortunately","unless","unlike","unlikely","until","unto","up","upon","ups","us","use","used","useful","usefully","usefulness","uses","using","usually","v","value","various","'ve","very","via","viz","vol","vols","vs","w","want","wants","was","wasnt","way","we","wed","welcome","we'll","went","were","werent","we've","what","whatever","what'll","whats","when","whence","whenever","where","whereafter","whereas","whereby","wherein","wheres","whereupon","wherever","whether","which","while","whim","whither","who","whod","whoever","whole","who'll","whom","whomever","whos","whose","why","widely","willing","wish","with","within","without","wont","words","world","would","wouldnt","www","x","y","yes","yet","you","youd","you'll","your","youre","yours","yourself","yourselves","you've","z","zero"}

a = open(opfile,"w")

for subdir, dirs, files in os.walk(filename):
    for file in files:
        if file[len(file)-3:len(file)] == "txt":
            if os.path.basename(subdir) == 'happy':
                with open(os.path.join(subdir, file), 'r', encoding='latin1') as f:
                    line = f.read()
                    type = ["happy"]

            elif os.path.basename(subdir) == 'sad':
                with open(os.path.join(subdir, file), 'r', encoding='latin1') as f:
                    line = f.read()
                    type = ["sad"]

            words_list = line.split()
            words = set(words_list)
            for each in words:
                each = each.lower().strip()
            for each in words:
                if each.isalpha():
                    if each not in stop_words:
                        all_words.add(each)
            words = list(words)
            word_dict[file] = type+words


#Ylist.append(type)
#Xlist.append(words)

for each in word_dict:
    present = []
    new_list = word_dict[each]
    type = new_list[0]
    new_list.remove(type)
    for e in all_words:
        if new_list.count(e)>0:
            present.append(1)
        else:
            present.append(0)

    Ylist.append(type)
    Xlist.append(numpy.array(present))


clf = RandomForestClassifier(n_estimators=7)

clf = clf.fit(Xlist, Ylist)


for subdir, dirs, files in os.walk(file_test):
    for file in files:
        if file[len(file)-3:len(file)] == "txt":
            with open(os.path.join(subdir, file), 'r', encoding='latin1') as f:
                line = f.read()

            words_list = line.split()
            words = set(words_list)
            for each in words:
                each = each.lower().strip()
            present = []
            words = list(words)
            for e in all_words:
                if words.count(e) > 0:
                    present.append(1)
                else:
                    present.append(0)

            output = clf.predict(numpy.array(present).reshape(1,-1))
            a.write((" ".join(str(s).upper() for s in output))+' '+ os.path.join(subdir, file) + '\n')
