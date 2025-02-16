from unittest import result
from zipfile import ZipFile
import statistics
from scipy.stats import kurtosis
from scipy.stats import skew
import csv
from sentence_transformers import SentenceTransformer, InputExample, losses
import pandas as pd
from sentence_transformers import SentenceTransformer, InputExample
from torch.utils.data import DataLoader
from sentence_transformers import SentenceTransformer, util
from torch import tensor
from promcse import PromCSE

#Opens dataset reads data all data into array
def open_file_allLines(file_name):
	f = open(file_name, "r")
	y = f.readlines()     #Y will have the whole transcript as an array
	for i in range(0,len(y)):
		i = i +1
	f.close
	return y

#Rwturns Semantic Similarity Scentence Comparisons
def semantic(x):
	#Model A:
	#model = SentenceTransformer("Sakil/sentence_similarity_semantic_search")

	#Model B:
	#model = PromCSE("YuxinJiang/unsup-promcse-bert-base-uncased", "cls_before_pooler", 16)

	#Model C
	model = SentenceTransformer('all-MiniLM-L6-v2')
    
	sentences = x

	#Number of scentences
	n = len(sentences)

	#Encode all sentences
	embeddings = model.encode(sentences)

	#Compute cosine similarity between all pairs
	cos_sim = util.cos_sim(embeddings, embeddings)

	#Add all pairs to a list with their cosine similarity score
	all_sentence_combinations = []

	for i in range(len(cos_sim)-1):

		for j in range(i+1, len(cos_sim)):
		
			all_sentence_combinations.append([cos_sim[i][j], i, j])

	#Create an array of all unique sentence combinations
	unique_comparisons = []
	for i in range(0,(n)):
		for j in range(i+1, n):
			unique_comparisons.append(cos_sim[i][j].item())

	#Compute Statisticle Measurments: All Scentences		
	Average_All = statistics.mean(unique_comparisons)
	SD_All = statistics.stdev(unique_comparisons)
	Skew_All = skew(unique_comparisons, axis = 0, bias = True)
	Kurt_All = kurtosis(unique_comparisons, axis = 0, fisher = True, bias = True)

	#Create an array of all adjacent sentence combinations
	adj_comparisons =[]
	for i in range(0,n-1):
		#uncomment to check which scentences are being compared
		#print("{} \t {} \t {:.4f}".format(sentences[i], sentences[i+1], cos_sim[i][i+1]))
		adj_comparisons.append(cos_sim[i][i+1].item())

	#Compute Statisticle Measurments: Adjacent Scentences
	Average_Adj = statistics.mean(adj_comparisons)
	SD_Adj = statistics.stdev(adj_comparisons)
	Skew_Adj = skew(adj_comparisons, axis = 0, bias = True)
	Kurt_Adj = kurtosis(adj_comparisons, axis = 0, fisher = True, bias = True)


	all_semantics =[Average_All, SD_All, Skew_All, Kurt_All, Average_Adj, SD_Adj, Skew_Adj, Kurt_Adj]
	return all_semantics


#Main

file_name = "content/DataSets.zip"

with ZipFile(file_name, 'r') as zip:
  zip.extractall()
  print('Done')

#Creation of empty arrays
id 				= [0] * 258
label 			= [0] * 258
Sem_All_Avg 	= [0] * 258
Sem_All_SD 		= [0] * 258
Sem_All_Skew 	= [0] * 258
Sem_All_Kurt 	= [0] * 258
Sem_Adj_Avg 	= [0] * 258
Sem_Adj_SD 		= [0] * 258
Sem_Adj_Skew 	= [0] * 258
Sem_Adj_Kurt 	= [0] * 258

count = 0
#Opens csv file read filenames from file path may need to be changed
with open('C:/Users/User/Documents/Capstone/content/DataSets/labeleddata/testlabels.csv', newline='') as csvfile:
	reader = csv.DictReader(csvfile)
	for row in reader:
		if(row["id"] == 'high_022' or row["id"] == 'low_023'):
			continue
		x = open_file_allLines("C:/Users/User/Documents/Capstone/content/DataSets/"+row["id"])
		id[count] = row["id"]
		label[count] = row["label"]
		#get semantic information for file x
		Sem_results = semantic(x)
		#store semantic feature information
		Sem_All_Avg[count] 	= Sem_results[0]
		Sem_All_SD[count] 	= Sem_results[1]
		Sem_All_Skew[count] = Sem_results[2]
		Sem_All_Kurt[count] = Sem_results[3]

		Sem_Adj_Avg[count] 	= Sem_results[4]
		Sem_Adj_SD[count] 	= Sem_results[5]
		Sem_Adj_Skew[count] = Sem_results[6]
		Sem_Adj_Kurt[count] = Sem_results[7]
		
		count = count + 1

count = 0
#Opens empty csv and writes labeled data
with open('labeled.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'label', 
				  'Sem_All_Avg', 'Sem_All_SD', 'Sem_All_Skew', 'Sem_All_Kurt', 
				  'Sem_Adj_Avg', 'Sem_Adj_SD', 'Sem_Adj_Skew', 'Sem_Adj_Kurt']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    count = 0
    writer.writeheader()
    for at in range(len(id)):
      writer.writerow({'id': id[count], 'label': label[count],
                        'Sem_All_Avg' 	: Sem_All_Avg[count],
						'Sem_All_SD' 	: Sem_All_SD[count],
						'Sem_All_Skew' 	: Sem_All_Skew[count],
						'Sem_All_Kurt' 	: Sem_All_Kurt[count],
						'Sem_Adj_Avg' 	: Sem_Adj_Avg[count],
						'Sem_Adj_SD' 	: Sem_Adj_SD[count],
						'Sem_Adj_Skew' 	: Sem_Adj_Skew[count],
						'Sem_Adj_Kurt' 	: Sem_Adj_Kurt[count]
                        })
      count = count + 1

print("Success")
