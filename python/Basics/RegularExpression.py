# 🔹 What is a Regular Expression (Regex) in Python?
# Regular Expressions (Regex) are patterns used to search, match, and manipulate strings.
# In Python, regex is supported by the re module.
# import re

# 🔹 What are the main components of a Regular Expression?
# 1. Metacharacters
# 2. Quantifiers
# 3. Grouping
# 4. Alternation
# 5. Character Classes

# 🔹 How do you create a Regular Expression in Python?
# import re
# pattern = re.compile("pattern")
# pattern = re.compile("pattern", flags)

# Use regex functions like:
# re.match() → matches at the beginning of a string
# re.search() → finds the first match anywhere in a string
# re.findall() → finds all matches
# re.sub() → replaces pattern with text

# Common Metacharacters
# 1. . → Any character
# 2. \d → Any digit (0-9)
# 3. \D → Any non-digit
# 4. \w → Any word character (a-z, A-Z, 0-9, _)
# 5. \W → Any non-word character
# 6. \s → Any whitespace character (space, tab, newline)
# 7. \S → Any non-whitespace character
# 8. \b → Any word boundary
# 9. \B → Any non-word boundary
# 10. ^ → Start of string
# 11. $ → End of string
# 12. \A → Start of line
# 13. \Z → End of line
# 14. \b → Start of word
# 15. \B → End of word
# 16. \n → Newline
# 17. \t → Tab
# 18. \r → Carriage return
# 19. \f → Form feed
# 20. \v → Vertical tab
# 21. \cX → Control character X
# 22. \xHH → Character with hex value HH
# 23. \uHHHH → Character with Unicode value HHHH
# 24. \UHHHHHHHH → Character with Unicode value HHHHHHHH
# 25. \oOOO → Character with octal value OOO
# 26. * → 0 or more repetitions
# 27. + → 1 or more repetitions
# 28. ? → 0 or 1 repetitions
# 29. {n} → n repetitions
# 30. {n,} → n or more repetitions
# 31. {n,m} → n to m repetitions
# 32. ? → 0 or 1 occurrence
# 33. [] → character set
# 34. () → group
# 35. | → alternation
# 36. \ → escape

# 1. Simple Match
import re

text = "Python is powerful"
result = re.match("Python", text)  
print(result.group())  # Output: Python

# Note: 👉 re.match only checks at the start. 

# 2. Search
import re

text = "Python is powerful"
result = re.search("powerful", text)  
print(result.group())  # Output: powerful

# 3. Replace
import re

text = "Python is powerful"
result = re.sub("powerful", "great", text)  
print(result)  # Output: Python is great

# 4. Split
import re

text = "Python is powerful"
result = re.split(" ", text)  
print(result)  # Output: ['Python', 'is', 'powerful']

# 5. Findall
import re

text = "Python is powerful"
result = re.findall("powerful", text)  
print(result)  # Output: ['powerful']

# 6. Finditer
import re

text = "Python is powerful"
result = re.finditer("powerful", text)  
for match in result:
    print(match.group())

# Using Character Sets
text = "bat, cat, mat, hat"
matches = re.findall("[bcm]at", text)
print(matches)  # Output: ['bat', 'cat', 'mat']

# Using Quantifiers
text = "he, hee, heee"
matches = re.findall("he+", text)
print(matches)  # Output: ['he', 'hee', 'heee']

# Using Grouping
text = "he, hee, heee"
matches = re.findall("(he)+", text)
print(matches)  # Output: ['he', 'hee', 'heee']

# Using Alternation
text = "he, hee, heee"
matches = re.findall("he|hee", text)
print(matches)  # Output: ['he', 'hee']

# Using Metacharacters
text = "he, hee, heee"
matches = re.findall("[a-z]+", text)
print(matches)  # Output: ['he', 'hee', 'heee']

# Using Escape Character
text = "he, hee, heee"
matches = re.findall("\w+", text)
print(matches)  # Output: ['he', 'hee', 'heee']

# Using Flags
text = "he, hee, heee"
matches = re.findall("he", text, re.IGNORECASE)
print(matches)  # Output: ['he', 'hee', 'heee']

