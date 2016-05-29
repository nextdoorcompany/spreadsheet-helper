import openpyxl

def read_with_headers(filename, sheetname):
	result = []
	wb = openpyxl.load_workbook(filename)
	sheet = wb.get_sheet_by_name(sheetname)
	c = 1
	headers = {}
	while sheet.cell(row=1, column=c).value:
		headers[c] = sheet.cell(row=1, column=c).value
		c += 1
	max_col = c
	max_row = sheet.max_row
	for row in range(2, max_row + 1):
		row_data = {}
		for col in range(1, max_col):
			val = sheet.cell(row=row, column=col).value
			if val is None:
				val = ''
			row_data[headers[col]] = val
		result.append(row_data)	
	return result