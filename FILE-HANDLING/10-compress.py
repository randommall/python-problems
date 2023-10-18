"""
10
Implement a program that compresses a text file using a compression algorithm and saves the compressed data to another file.

"""

import gzip

input_file = "output.txt"

output_file = "compressed_output.gz"

with open(input_file, 'rb') as file_in, gzip.open(output_file, 'wb') as file_out:
    file_content = file_in.read()
    file_out.write(file_content)

print(f"File '{input_file}' has been compressed and saved as '{output_file}'.")