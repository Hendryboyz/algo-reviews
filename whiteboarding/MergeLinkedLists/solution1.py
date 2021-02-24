# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def mergeLinkedLists(headOne, headTwo):
	result_head = cur = None
	while headOne != None and headTwo != None:
		node = None
		if headOne.value <= headTwo.value:
			node = headOne
			headOne = headOne.next
		else:
			node = headTwo
			headTwo = headTwo.next
			
		if result_head == None:
			result_head = node
		else:
			cur.next = node
		cur = node
	if headOne != None:
		cur.next = headOne
	else:
		cur.next = headTwo
	return result_head
