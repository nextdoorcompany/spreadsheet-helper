import pprint
import sys
import spreadsheet_helper

filename = sys.argv[1]
sheetname = sys.argv[2]
header_row = sys.argv[3]
start_col = sys.argv[4]

result = spreadsheet_helper.read_with_headers(filename, sheetname, header_row, start_col)

pprint.pprint(result)