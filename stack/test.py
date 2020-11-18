import stack

dishes = stack.Stack()

# Adding some data to our stack

dishes.push('Dish 1')
print('Dish 1 added')
dishes.push('Dish 2')
print('Dish 2 added')
dishes.push('Dish 3')
print('Dish 3 added')
# Viewing the top item in our stack
print(f'The top dish in our stack is {dishes.top()}')# Should be Dish 3
print(f'There are currently {dishes.size()} items in the stack')
print('The top dish is now being removed')
dishes.pop()
print(f'The top dish in our stack is now {dishes.top()}')# Should be Dish 2
print(f'There are now {dishes.size()} items in the stack')
print('Checking to see if the stack is empty...')
print(dishes.empty())
print('Creating new empty stack "papers"...')
papers = stack.Stack()
print('Checking if new stack is empty.')# Should return True
print(papers.empty())
