from collections import Counter
import re

# Function to read and process the text file
def process_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        words = re.findall(r'\b\w+\b', text.lower())  # Tokenize the words and convert to lowercase
        return Counter(words)

# Function to write the top N words to a new text file
def write_top_words(counter, output_file_path, top_n=200):
    with open(output_file_path, 'w', encoding='utf-8') as output_file:
        for word, count in counter.most_common(top_n):
            output_file.write(f'{word}: {count}\n')

# Main script
if __name__ == "__main__":
    input_file_path = "sample.txt"
    output_file_path = "top_words.txt"

    word_counter = process_text_file(input_file_path)
    write_top_words(word_counter, output_file_path)
    
    print(f"Top 100 words written to {output_file_path}")




# count = 0
# #Opens csv file read filenames from file path may need to be changed
# with open('DataSets/labeleddata/output.csv', 'w',newline='') as csvfile:
#     reader = csv.DictReader(csvfile)

#     for row in reader:    
#       x = open_file("DataSets/"+row["id"])
#       y = open_file_allLines("DataSets/"+row["id"])
#       print(y)
#       id[count] = row["id"]
#       count = count + 1