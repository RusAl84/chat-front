from pymystem3 import Mystem

def getwords(mas):
    tstr=""
    skob=0;
    words=[];
    last_i=len(mas)+1;
    for i in range(0, len(mas)):
        if mas[i] == '(':
            skob+=1
        if mas[i] == ')':
            skob -= 1
        if (mas[i]==',' or mas[i]==';') and skob==0:
            #print(tstr.strip())
            tstr=tstr.lower()
            words.append(tstr.strip())
            tstr=""
            last_i=i
            continue
        tstr = tstr + mas[i]
    if tstr==mas:
        words=mas
        return words
    if last_i<len(mas):
        tstr = ""
        for i in range(last_i+1, len(mas)):
            tstr = tstr + mas[i]
        tstr = tstr.lower()
        words.append(tstr.strip())
    return words

# def print(self):
#     print(self.mas)
#     for x in self.words:
#         print(x)
#     return "%s " % self.mas

# def compare(self, words1, words2):
#     gscore=[]
#     for w1 in words1:
#         score=[];
#         for w2 in words2:
#             score.append(Levenshtein.distance(w1, w2))
#             #print( Levenshtein.distance(w1, w2) )
#         if len(score)>1:
#             gscore.append(min(score))
#         else:
#             gscore=100000
#             return gscore
#     #print(sum(gscore))
#     return sum(gscore)

def compare_words(words1, words2):
    kol_sovp=0
    for i in range(len(words1)):
        item1=words1[i]
        if  len(str(item1))>2:
            for j  in range(len(words2)):
                item2 = words2[j]
                if len(str(item2))>2:
                    if item1 == item2:
                        kol_sovp += 1

    return kol_sovp

def d2lemmatize(mas):
    сrazdelitel = " cr "
    razdelitel = " br "
    rwords=""
    row_num=1;
    # for item in mas:
    #     # print(row_num)
    #     row_num+=1
    #     cwords = ""
    #     for word in item:
    #         if len(str(word)) > 3:
    #             cwords = cwords + str(word) + razdelitel
    #     if len(cwords)>1:
    #         rwords = rwords + cwords + сrazdelitel
    for item1 in mas:
        cwords = ""
        if type(item1) in (tuple, list):
            for item2 in item1:
                cwords = cwords + str(item2) + razdelitel
        else:
            item1=item1.split()
            for item2 in item1:
                cwords = cwords + str(item2) + razdelitel
        #print(cwords)
        rwords = rwords + cwords + сrazdelitel
    m = Mystem()
    # print(rwords)
    lmas = m.lemmatize(rwords)
    gmas = []
    tmpword = []
    stroka=[]
    for word in lmas:
        if word==str.strip(razdelitel):
            stroka.append(tmpword)
            tmpword=[]
        elif len(word)>3:
            tmpword.append(word)
        elif word==str.strip(сrazdelitel):
            gmas.append(stroka)
            stroka=[]
    # print(gmas)
    return gmas

def d1lemmatize(mas):
    gmas=[]
    razdelitel=" br "
    m = Mystem()
    lwords = ""
    for word in mas:
        if len(str(word))>3:
            lwords=lwords+word+razdelitel
    # print(lwords)
    # print(mas)
    lmas = m.lemmatize(lwords)
    # print(lmas)
    tmpword=[]
    for word in lmas:
        if word==str.strip(razdelitel):
            gmas.append(tmpword)
            tmpword=[]
        elif len(word)>3:
            tmpword.append(word)
    # print(gmas)
    return gmas
