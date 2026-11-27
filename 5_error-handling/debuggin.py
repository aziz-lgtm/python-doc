# 1. print() and f-strings
# Purpose: Quickly check what values your variables hold and in what order your code runs.
def add(a, b):
    result = a + b
    print(f'Adding {a} and {b} gives {result}')
    return result

# result = a + b: Performs the calculation you want to test.

# print(f'Adding {a} and {b} gives {result}'): Prints the inputs (a, b) and output (result) to your console before the function finishes so you can immediately see if the math or logic went wrong.

# return result: Hands the result back to whatever called the function so the program continues normally.

# 2. The pdb Module (Interactive Terminal Debugger)
# Purpose: Pause your code mid-run in the terminal so you can inspect variables and test things live instead of guessing with print()

import pdb

def divide(a, b):
    pdb.set_trace()
    return a / b

print(divide(10, 2))

# import pdb: Loads Python’s built-in debugger.

# pdb.set_trace(): Acts as a manual pause button. When Python hits this line, it freezes the program and opens the (Pdb) prompt in your terminal right before running return a / b.

# print(divide(10, 2)): Runs the function so it actually triggers the pause.

# What you type inside the (Pdb) prompt:

# help: Shows all available debugger commands.

# whatis a / whatis divide: Tells you the exact data type of a variable or object at that frozen moment (e.g., <class 'int'> or Function divide), helping you catch type bugs.

# continue (or cont / c): Unfreezes the program and lets it finish running (5.0).


# 3. IDE Debugger (VS Code)
# Purpose: Give you a visual interface (clickable pauses, variable panels, step buttons) so you don't have to modify your code with print() or pdb.set_trace()

def divide(a, b):
    result = a / b
    return result

print(divide(10, 2))
print(divide(15, 3))

# Click in the gutter (left margin) next to line 2 (result = a / b) to set a breakpoint

# A red dot will appear, indicating the breakpoint is set

# Step 3: Start debugging

# Press F5 or go to Run > Start Debugging

# Select "Python File" when prompted

# The debugger will pause execution at your breakpoint

# Step 4: Inspect variables

# Hover over variables to see their current values

# Use the Variables panel on the left to see all local variables

# Use the Debug Console at the bottom to evaluate expressions

# Step 5: Step through code

# Use the debug toolbar to:

# Continue (F5): Resume execution until the next breakpoint

# Step Over (F10): Execute the current line and move to the next

# Step Into (F11): Enter into function calls

# Step Out (Shift + F11): Exit the current function

# IDE debugging tools provide a visual interface to examine the state of your program, making it easier to identify and fix issues compared to using print statements alone.

# By mastering these foundational debugging techniques (print() statements, the pdb module, and IDE tools), you can effectively identify and resolve issues in your Python code. Each technique has its place: print() statements for quick checks, pdb for interactive exploration, and IDE debuggers for visual inspection.