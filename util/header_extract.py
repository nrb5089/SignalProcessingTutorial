# import argparse

# def extract_headers(input_file, output_file):
	# with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
		# for line in infile:
			# if line.startswith("# "):
				# outfile.write(line)
			# elif line.startswith("## "):
				# outfile.write(line)
			# elif line.startswith("### "):
				# outfile.write(line)

# if __name__ == "__main__":
	# '''
	# python script_name.py path_to_input.md path_to_output.md
	# '''
	# # Set up command-line argument parsing
	# parser = argparse.ArgumentParser(description='Extract headers from markdown file.')
	# parser.add_argument('input_file', type=str, help='Path to the input markdown file.')
	# parser.add_argument('output_file', type=str, help='Path to save the extracted headers.')
	
	# args = parser.parse_args()

	# # Extract headers
	# extract_headers(args.input_file, args.output_file)
	
	
# import argparse

# def extract_headers(input_file, output_file):
	# inside_python_block = False

	# with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
		# for line in infile:
			# # Check if we're entering or exiting a Python code block
			# if line.strip().startswith("```python"):
				# inside_python_block = True
				# continue
			# elif line.strip().startswith("```"):
				# inside_python_block = False
				# continue

			# # If we're not inside a Python code block, process the headers
			# if not inside_python_block:
				# if line.startswith("# "):
					# outfile.write(line)
				# elif line.startswith("## "):
					# outfile.write(line)
				# elif line.startswith("### "):
					# outfile.write(line)

# if __name__ == "__main__":
	# parser = argparse.ArgumentParser(description='Extract headers from markdown file.')
	# parser.add_argument('input_file', type=str, help='Path to the input markdown file.')
	# parser.add_argument('output_file', type=str, help='Path to save the extracted headers.')
	
	# args = parser.parse_args()
	# extract_headers(args.input_file, args.output_file)


import argparse

def extract_headers(input_files, output_file):
	with open(output_file, 'w') as outfile:
		for input_file in input_files:
			inside_python_block = False
			
			# Write the file name to the output
			# outfile.write(f"# File: {input_file}\n")
			outfile.write(f"# {input_file[3:]}\n")

			with open(input_file, 'r') as infile:
				for line in infile:
					# Check if we're entering or exiting a Python code block
					if line.strip().startswith("```python"):
						inside_python_block = True
						continue
					elif line.strip().startswith("```"):
						inside_python_block = False
						continue

					# If we're not inside a Python code block, process the headers
					if not inside_python_block:
						if line.startswith("# "):
							outfile.write(line[2:])
						elif line.startswith("## "):
							outfile.write(line[3:])
						elif line.startswith("### "):
							outfile.write(line[4:])

			# Add a newline between files for better separation
			outfile.write("\n")

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Extract headers from markdown files.')
	parser.add_argument('input_files', type=str, nargs='+', help='Path(s) to the input markdown files.')
	parser.add_argument('output_file', type=str, help='Path to save the extracted headers.')
	
	args = parser.parse_args()
	extract_headers(args.input_files, args.output_file)
