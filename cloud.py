import os
import socket
import string
from collections import Counter

# Setting path variables
base_dir = '/home/data'
output_dir = '/home/output'

# Accessing all text files in the given directory
files = os.listdir("/home/data")

# Locating target files
if_file_path = os.path.join(base_dir, 'IF.txt')
limerick_file_path = os.path.join(base_dir, 'Limerick-1.txt')
res_file_path = os.path.join(output_dir, 'result.txt')

# Function to count words in a file
def count_words(file_path):
    word_count = 0
    with open(file_path) as file:
        for row in file:
            word_count += len(row.split())
    return word_count

# Counting words in target files
wc_if = count_words(if_file_path)
wc_lim = count_words(limerick_file_path)

# Computing top 3 frequent words in IF.txt
words = Counter()
with open(if_file_path) as file_if:
    for line in file_if:
        words.update([word.strip(string.punctuation).capitalize() for word in line.split()])

# Getting the top 3 words
sort_words = words.most_common(3)

# Getting the host machine's IP address
hostname = socket.gethostname()
IP_address = socket.gethostbyname(hostname)

# Writing output to result.txt
with open(res_file_path, 'w') as res_file:
    res_file.write("List of all the text files in the directory:\n")
    res_file.write('\n'.join(files) + '\n')
    res_file.write(f"No of words in Limerick-1.txt: {wc_lim}\n")
    res_file.write(f"No of words in IF.txt: {wc_if}\n")
    res_file.write(f"Total of words: {wc_if + wc_lim}\n")
    res_file.write("Top 3 words with their counts in IF.txt:\n")
    for word, count in sort_words:
        res_file.write(f"{word} -> count: {count}\n")
    res_file.write(f"IP address of the machine: {IP_address}\n")

# Displaying output from result.txt file
with open(res_file_path) as res_file:
    for line in res_file:
        print(line.strip())
