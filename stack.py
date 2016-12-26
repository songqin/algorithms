# LIFO

def examine(stack, position):
	print stack[position]
stack=list()
stack.append(1)
stack.append(2)
print stack
print len(stack)
examine(stack, 0)
examine(stack, 1)
stack.pop()
print stack
stack.append(3)
print stack
stack.append(4)
print stack
# peak, examine
print stack[-1]
# check if the stack is empty
print len(stack)!=0
import collections
# deque pronouced "deck"
stack = collections.deque()
stack.append(1)
print stack
stack.appendleft(2)
print stack
stack.append(3)
print stack
stack.pop()
print stack
stack.popleft()
print stack
print len(stack)
