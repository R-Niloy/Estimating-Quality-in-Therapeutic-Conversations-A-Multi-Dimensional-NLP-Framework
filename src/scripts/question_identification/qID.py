from nltk.tokenize import word_tokenize
from nltk.tokenize import TweetTokenizer
from nltk import bigrams
from zipfile import ZipFile
import os
import csv
import pandas as pd

#lib https://github.com/kartikn27/nlp-question-detection FOR CORPUS

#QUESTION word set and Auxillary verb word set combined
Set_A = ["what", "why", "when", "where", "who", "whom", "whose", "were",
                "which", "was", "does", "did", "can", "could", "will", "would", "should", "has",
                "have", "had", "may", "might", "shall", "should", "must", "be", "do", "have", "best", 
                "need", "shall", "better", "may", "should", "can", "might", "will",
                "could", "must", "would", "dare", "ought", "are", "to", "in", "of", "is", "i", "it", "?"]

def is_question(sentence):
    # Tokenize the input sentence
    tokens = word_tokenize(sentence.lower())

    # Check if any question words are present in the tokens
    if any(word in tokens for word in Set_A):
        return True
    else:
        return False

#Opens dataset reads data all data into array
def open_file_allLines(file_name):
  f = open(file_name, "r")
  y = f.readlines()     #Y will have the whole transcript as an array
  f.close
  return y


#print(open_file_allLines("DataSets/"+"high_001"))

id = [0] * 258

cnt = 0

#populates file ID list
for filename in os.listdir("DataSets"): 
    id[cnt] = filename
    cnt+=1

inClient = False

for x in id:
    transcript = open_file_allLines("DataSets/"+x) # this is a list containing all lines of trascript.
    c_cnt = 0
    t_cnt = 0
    for line in transcript: #transcript is tokenized here
        length = len(transcript)

        tknzr = TweetTokenizer()
        tokens= tknzr.tokenize(line)

        # Create word pairs (bigrams)
        word_pairs = list(bigrams(tokens))

        print("Original sentence:")
        print(line)

        #to check speaker
        if len(word_pairs) >= 2:
            if(word_pairs[0][0] == 'C'):
                inClient = True
            elif(word_pairs[0][0] == 'T'):
                inClient = False

        print(x)
        print(inClient)
        print("\nWord pairs:")
        print(word_pairs)
        #now we look for words in the bigrams in or word pools
        for pair in word_pairs:
            if((pair[0] in Set_A) and (pair[1] in Set_A) or (pair[1] == "?")):
                if(inClient == True):
                    c_cnt+=1
                elif(inClient == False):
                    t_cnt+=1
                if(pair[1] == "?"):#avoid incrementing multiple times if we hit a question mark in middle, some transcripts have them.
                    break
        #we have the total question in the transcript. now we calculate and add to a new spreadsheet
    c_qperlines = c_cnt/length
    t_qperlines = t_cnt/length

    if t_cnt != 0 and c_cnt != 0:
        c_t_question_ratio = c_cnt/t_cnt
    else:
        c_t_question_ratio = None

    #now store in spreadsheet
    filename = 'questionFeature.csv'
    data = [[x, c_qperlines, t_qperlines, c_t_question_ratio],]
    with open(filename, 'a', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data)

    print(f'Data has been written to {filename}')





