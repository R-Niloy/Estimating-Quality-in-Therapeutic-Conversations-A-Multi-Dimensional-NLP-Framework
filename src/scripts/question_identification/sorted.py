import csv

# Specify the input and output file names
input_file_name = 'questionFeature.csv'
output_file_name = 'questionFeature_sorted.csv'

# Specify the column to sort by
sort_column_index = 0  # Assuming "Name" is the first column (0-based index)

# Read the CSV file into a list of rows
with open(input_file_name, 'r') as infile:
    reader = csv.reader(infile)
    data = list(reader)

# Sort the data by the specified column
sorted_data = sorted(data, key=lambda x: x[sort_column_index])

# Write the sorted data to a new CSV file
with open(output_file_name, 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerows(sorted_data)

print(f'Data has been sorted and written to {output_file_name}')