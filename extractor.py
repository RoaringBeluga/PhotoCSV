import getopt
import os
import sys
from pathlib import Path

import parsers.pdfparser as pdf_parser
import parsers.reportparser as r_parser
from utilities.misc import get_file_list

DEBUG = True

short_options = 'hi:o:f:'
long_options = ['help', 'input=', 'output=', 'file=']

input_dir = ''
output_dir = ''
output_file = 'out.csv'


def get_options():
	global output_dir, input_dir, output_file

	full_cmd_arguments = sys.argv
	# Keep all but the first
	argument_list = full_cmd_arguments[1:]
	print(argument_list)
	try:
		arguments, values = getopt.getopt(argument_list, short_options, long_options)
	except getopt.error as err:
		# Output error, and return with an error code
		print(str(err))
		sys.exit(2)
	print(arguments, values)
	for option, value in arguments:
		if option in ('-h', '--help'):
			print(f'Usage: {full_cmd_arguments[0]} [-i <input_dir>] [-o <output_dir>] [-f <output_file>]\n\tOR')
			print(f'Usage: {full_cmd_arguments[0]} [--input=<input_dir>] [--output-<output_dir>] [--file=<output_file>]')
			exit(0)
		elif option in ('-i', '--input'):
			input_dir = value
		elif option in ('-o', '--output'):
			output_dir = value
		elif option in ('-f', '--file'):
			output_file = value
	print(f'Input directory: {input_dir}')
	print(f'Output directory: {output_dir}')
	print(f'Output file: {output_file}')


def do_processing(p_input_dir, p_output_dir, p_output_file):
	global output_dir, input_dir, output_file

	print('Processing started...')
	# Check for input directory...
	p = Path(os.path.expanduser(p_input_dir))
	if p.exists():
		input_dir = str(p.resolve())
	else:
		print(f'Input path: {p_input_dir} does not exist. Aborting.')
		exit(1)
	input_files = get_file_list(input_dir, '*.pdf')
	# Check for output directory...
	p = Path(os.path.expanduser(p_output_dir))
	if p.exists():
		output_dir = str(p.resolve())
	else:
		print(f'Output path: {p_output_dir} does not exist. Aborting.')
		exit(1)
	if (p_output_file is not None) and (p_output_file != ''):
		output_file = str(Path(output_dir, p_output_file).resolve())
	else:
		print(f'Output file name missing! Aborting...')
		exit(1)
	report_parser = r_parser.ReportParser()
	# Now let's iterate through files
	# Each file should have zero or more reports in it
	for filename in input_files:
		pdf_file = pdf_parser.PDFParser()
		print(f'Processing: {filename}')
		pdf_file.read_pages(filename)
		page_set = pdf_file.get_pages()
		for current_page in page_set.values():
			# Now parse the page
			report_parser.parse_report(current_page)

	# Processing finished!
	print(f'Processing finished. Writing {output_file}')
	report_parser.write_csv(output_file)


if __name__ == '__main__':
	get_options()
	do_processing(input_dir, output_dir, output_file)
