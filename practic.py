# this is my 5th programe
# topic: string analysis,indexing,slicing and built-in functions 

# 1 cleaning the string and removing the extra spaces using strip() method
raw_text = input("Enter the text: ")
text = raw_text.strip()

print("\n"+"="*40)
print("           string analysis")
print("="*40)

# 2 calculate string length using len() method
print("Original string:", raw_text)
print("total characters:", len(text))

# 3 indexing (positive and negative indexing)

print("\n--------- indexing ---------")
print("first indexing: [0]",text[0])
print("second indexing: [1]",text[1])
print("last indexing: [-1]",text[-1])

#4 slicing [start:end:step] (end index is excluded)
print("\n---------slicing---------")
print("first 5 characters:",text[0:5])
print("from index 2 to end:",text[2:])
print("last 3 characters:",text[-3:])

#5 string methods
print("\n---------string methods---------")
print("uppercase     :",text.upper())
print("lowercase    :",text.lower())
print("capitalize   :",text.capitalize())
print("endswith '.' :",text.endswith('.'))
print("count 'a'    :",text.count('a'))
print("replace space to '_' :",text.replace(' ','_'))

print("="*40)