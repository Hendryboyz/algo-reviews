# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

def mergeLinkedLists(headOne, headTwo):
	pointer1 = headOne
	pointer2 = headTwo
	prev = None
	while pointer1 != None and pointer2 != None:
		node = None
		if pointer1.value < pointer2.value:
			node = pointer1
			pointer1 = pointer1.next
		else:
			node = pointer2
			pointer2 = pointer2.next
		if prev != None and prev.next != node:
			node.next = prev.next
			prev.next = node
		prev = node
	
	if pointer1 != None:
		prev.next = pointer1
	else:
		prev.next = pointer2
	return headOne if headOne.value < headTwo.value else headTwo
