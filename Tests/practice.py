import pytest
@pytest.mark.set1
def test_file1_method1():
	x=5
	y=6
	assert x+1 == y, "test failed"
	assert x == y, "test failed"

@pytest.mark.set1
def test_file1_method2():
	test = 2
	print(test)
	x=5
	y=6
	newYear=31
	print(newYear)
	assert x+1 == y, "test failed"