from abc import ABC, abstractmethod
import re

class Mark(ABC):
	@abstractmethod
	def parentMark(self)->Mark:
		pass
	def setParentMark(self):
		pass
	def level(self)->int:
		pass

class LineBreak(Mark):
	def __init__(self):
		self.__parentMark = None

	def parentMark(self)->Mark:
		return self.__parentMark

	def setParentMark(self, newParentMark):
		self.__parentMark = newParentMark

	def level(self)->int:
		return 999

class SuperMark(Mark):
	def __init__(self):
		self.__subMarks = []

	def addMark(self, newSubMark: Mark):
		self.__subMarks.append(newSubMark)
		newSubMark.setParentMark(self)

	def level(self)->int:
		return 0

	def setParentMark(self, newParentMark):
		self.__parentMark = None #this should never be called

	def parentMark(self)->Mark:
		return None

class Paragraph(Mark):
	def __init__(self, input:str):
		self.__rawString:str = input
		self.__parentMark = None

	def level(self)->int:
		return 999

	def setParentMark(self, newParentMark):
		self.__parentMark = newParentMark

	def parentMark(self)->Mark:
		return None

class Header(Mark):
	def __init__(self, input:str):
		self.__rawString:str = input
		self.__parentMark = None
		self.__level = len(re.search('^#+',self.__rawString).group(0))
		self.__subMarks = []

	def level(self) -> int:
		return self.__level

	def addMark(self, newSubMark):
		self.__subMarks.append(newSubMark)
		newSubMark.setParentMark(self)

	def setParentMark(self, newParentMark):
		self.__parentMark = newParentMark

	def parentMark(self)->Mark:
		return self.__parentMark

class UnnumberedListItem(Mark):
	def __init__(self, input:str):
		self.__rawString:str = input
		self.__parentMark = None
		self.__subItems =[]
		self.__level = 99 + len(re.search('^(\\t)*', self.__rawString).group(0)) + 1

	def addItem(self, newSubItem: Mark):
		self.__subItems.append(newSubItem)
		newSubItem.setParentMark(self)

	def level(self) -> int:
		return self.__level

	def setParentMark(self, newParentMark):
		self.__parentMark = newParentMark

	def parentMark(self)->Mark:
		return self.__parentMark

class NumberedListItem(Mark):
	def __init__(self, input:str):
		self.__rawString:str = input
		self.__parentMark = None
		self.__subItems =[]
		self.__level = 99 + len(re.search('^(\\t)*', self.__rawString).group(0)) + 1

	def addItem(self, newSubItem: Mark):
		self.__subItems.append(newSubItem)
		newSubItem.setParentMark(self)

	def level(self) -> int:
		return self.__level

	def setParentMark(self, newParentMark):
		self.__parentMark = newParentMark

	def parentMark(self)->Mark:
		return self.__parentMark