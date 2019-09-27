from ast import literal_eval

op = {'*': "Multiplication operator", '/': "Division operator", '+': "Addition operator", '-': "Subtraction operator",
      '==': "Equality operator", '>': "Greater Than operator", '<':"Less Than operator", '!=': "Not Equals operator",
      '>=': "Greater Than Equal To operator", '<=': "Less Than Equal To operator", '&&': "And operator",
      '||': "Or operator", 'AND': "Logical And operator", 'OR': "Logical Or operator"}

x = input("Enter operator: ")
for i in op.keys():
    if x.upper() == i:
        print (i, ":", op[i])
        break

y = input("Enter value (Note: apply quotes if string value): ")
print ("Data type is:", type(literal_eval(y)))









