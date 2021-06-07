from markdownTree import Mark,Paragraph, Header, UnnumberedListItem, NumberedListItem, LineBreak
import re

def parseMD(filename:str):
	rawStringList = []
	with open(filename,'r+') as file:
		rawStringList = file.readlines()

	markList = []
	for rawString in rawStringList:
		if re.search('^#+',rawString) is not None:
			markList.append(Header(rawString))

		elif re.search('^\\s*- ',rawString) is not None:
			markList.append(UnnumberedListItem(rawString))

		elif re.search('^\\s*[0-9]+. ',rawString) is not None:
			markList.append(NumberedListItem(rawString))

		elif re.search('^(\t)*(\\r\\n|\\r|\\n)', rawString) is not None:
			markList.append(LineBreak())

		else:
			markList.append(Paragraph(rawString))

	return markList

def makeTree(markList:list[Mark]):
	root = SuperMark()
	currentHeader = root
	for mark in markList:
		while mark.level() <= currentHeader.level():
		 	currentHeader = currentHeader.parentMark()
		currentHeader.addMark(mark)
		currentHeader = mark


mList = parseMD('input.md')

print('marks')
for mark in mList:
	print(mark)