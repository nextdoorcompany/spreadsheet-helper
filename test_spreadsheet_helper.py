import openpyxl
import pytest
import spreadsheet_helper

@pytest.fixture
def blank_worksheet():
	return 'test.xlsx', 'blank'

@pytest.fixture
def standard_worksheet():
	return 'test.xlsx', 'standard'	

@pytest.fixture
def header_only_worksheet():
	return 'test.xlsx', 'headeronly'	

def test_read_blank(blank_worksheet):
	filename, sheetname = blank_worksheet
	result = spreadsheet_helper.read_with_headers(filename, sheetname)

	assert len(result) == 0

def test_read_header_only(header_only_worksheet):
	filename, sheetname = header_only_worksheet
	result = spreadsheet_helper.read_with_headers(filename, sheetname)

	assert len(result) == 0	

def test_read_standard(standard_worksheet):
	filename, sheetname = standard_worksheet
	result = spreadsheet_helper.read_with_headers(filename, sheetname)

	assert len(result) == 3
	assert result[0]['uid'] == 1
	assert result[0]['uname'] == 'mike'
	assert result[1]['uid'] == 2
	assert result[1]['uname'] == ''	
	assert result[2]['uid'] == 3
	assert result[2]['uname'] == 'henry'
