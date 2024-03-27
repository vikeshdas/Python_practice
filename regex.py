
import re
import os
# Get the list of all files and directories
path = "C://Users//vk001"
dir_list = os.listdir(path)


dir_list=(" ".join(dir_list))
# print(dir_list)
dir_list="Recent Saved Games Searches SendTo Start Menu Templates vikeos vikesh"
pattern = '[vik]+'
print(re.findall(pattern,dir_list))

print("*******************match()***************************search()*********************findall()********************findfilter()**************")
# match():-Determine if the RE matches at the beginning of the string.

# search():-Scan through a string, looking for any location where this RE matches.

# findall():- Find all substrings where the RE matches, and returns them as a list.

# finditer():-Find all substrings where the RE matches, and returns them as an iterator

print("*********************************************************************************************************************************************")
#  Since the match() method only checks if the RE matches at the start of a string, start() will always be zero. 
# However, the search() method of patterns scans through the string
import re
p = re.compile('[a-z]+')
m=p.match('tempo')
print("group",m.group())
print("start",m.start())
print("end",m.end())
print("span",m.span())

print(p.match('::: message'))#output: None
m = p.search('::: message')#output :<re.Match object; span=(4, 11), match='message'>
print(m)
print(m.group())#output 'message
print(m.span())#(4, 11)

#  findall() returns a list of matching strings:
p = re.compile('\d+')
f=p.findall('12 drummers drumming, 11 pipers piping, 10 lords a-leaping')
print(f)

# findall() has to create the entire list before it can be returned as the result.
# The finditer() method returns a sequence of match object instances as an iterator
iterator = p.finditer('12 drummers drumming, 11 ... 10 ...')
print(iterator)
for match in iterator:
    print(match.span())

# You don’t have to create a pattern object and call its methods
# the re module also provides top-level functions called match(), search(), findall(), sub()
# These functions take the same arguments as the corresponding pattern method,and still return
# either None or a match object instance
    
#these method internally creates pattern sobject and call method(match).They also store the compiled object in a cache
print(re.match(r'From\s+', 'Fromage amk')) #just pass pattern and text in match similer to previus

# If you’re accessing a regex within a loop, pre-compiling it will save a few function calls. Outside of loops,
# there’s not much difference

print('*********************************************Compilation Flags*****************************************************')

# re.IGNORECASE:- it will match upper and lowercase letter both.Full Unicode matching also works for example 
# r'spam will match ['Spam', 'spam', 'SPAM', 'ſpam'] in text="Spam, spam, SPAM, and ſpam.""
# it can match ASCII and non ASCII value  in text = "abcİıſK" pattern=[a-z] will match ['a', 'b', 'c', 'İ', 'ı', 'ſ', 'K']
# "Full Unicode" means considering and supporting the entire range of characters defined by the Unicode standard. This includes 
# characters from scripts such as Latin, Cyrillic, Arabic, Chinese, Japanese, Korean, emojis, mathematical symbols, and many others

import re
text = "Spam, spam, SPAM!, and ſpam"
pattern = "spam"
matches = re.findall(pattern, text, re.IGNORECASE)
print("Matched:", matches)

# ***************************************************************************************************

# In Python's re module, the re.X (or re.VERBOSE) flag allows you to write regular expressions in a more readable 
# and organized manner by ignoring whitespace and comments within the pattern string. This flag enables you to add
# comments and whitespace to the regular expression, making it easier to understand and maintain.comment will be ignored
# as other language do.

phone_number = "(123) 456-7890"

# Regular expression pattern with re.X
pattern_verbose = r'''
    \(      # Match opening parenthesis
    \d{3}   # Match three digits for area code
    \)      # Match closing parenthesis
'''

matches_verbose = re.findall(pattern_verbose, phone_number, re.X)
print("Matches with verbose pattern:", matches_verbose)

# *******************************************************************************************************
# re.A
# re.ASCII: Make \w, \W, \b, \B, \s and \S perform ASCII-only matching instead of full Unicode matching

print('*************************************************or(|)********************************************************')

# | :- the “or” operator. If A and B are regular expressions, A|B will match any string that matches either A or B. 
import re
text = "I like apples and bananas."
pattern = r"apple|banana"

matches = re.search(pattern, text)
print("Matches:", matches)

print("*************************************************Caret(^)**********************************************")
# catet check that patter matched in biginer of text if it is matched then its will give you indexs else it will
# give you None.for example Good is at the begining in text so it return start,end index.in second patter morning
# is not at begining so it wil print None
# In MULTILINE mode, this also matches immediately after each newline within the string

text = "Good morning every one"
pattern = r"^Good"
matches=re.findall(pattern,text)
print(matches)

print("*************************************************dollar($)*********************************************")
# it is apposite to catet sign it match end of the string if pattern find at the end of string then it returns
# start and end index else None.
text = '''Good morning every one
    Good morning every one'''
pattern = r"one$"

matches = re.findall(pattern, text, re.MULTILINE)
print("Matches", matches)

print("*************************************************\A****************************************************")

# Matches only at the start of the string. When not in MULTILINE mode, \A and ^ are effectively the same.
# In MULTILINE mode, they’re different: \A still matches only at the beginning of the string,
# but ^ may match at any location inside the string that follows a newline character

print("*************************************************\Z****************************************************")

# Matches only at the end of the string.regardless of whether the string ends with a newline character or not
text = '''Good morning every one
    Good morning every'''
pattern = r"one\Z" #return None becuase .it is multiline so first line end with one it should pirnt one but no

matches = re.findall(pattern, text, re.MULTILINE)
print("Matches", matches)

print("*************************************************\ b****************************************************")
# it finds the words character between non-word character.word character is [a-z,A-Z,and digit].non-word char
# include space(" "),tab("\t"),new line(\n) etc.Period (.), comma (,), colon (:), semicolon (;), exclamation mark (!), question mark (?), etc.
# Parentheses (()), square brackets ([]), braces ({}), angle brackets (< >), quotation marks (' " ), etc.
# Ampersand (&), asterisk (*), plus sign (+), minus sign (-), slash (/), backslash (), pipe (|), etc all are non-
# word character.

p = re.compile(r'\bclass\b')

print(p.search('no class at all'))#in this p will match becasue class is between " "class" " ,sspace is non-word char

print(p.search('the declassified algorithm'))#in this class is between (de)class(ified) which are word char so it will return non

print(p.search('one subclass is')) #class is between (sub)class(" ") sub is word char so it will return none

# \B Another zero-width assertion, this is the opposite of \b, only matching when the current position is not at a word boundary

print('*************************************************\w*********************************************************************************')

# Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_]
p = re.compile('\w')
result=p.findall('vikesh kumar das')#if we use finall method it will match all char from [a-zA-Z0-9_]
print(result)

result=p.search('vikesh kumar das')#if we use search() method it will match first char 'v'
print(result)

result=p.match('vikesh kumar das')#if we use search() method it will match first char 'v'
print(result)

print('*****************************************************Grouping*************************************************************************')

# (ab)* will match zero or more repetitions of ab becuae ab is in group
p = re.compile('(ab)*')
print(p.match('ababababab').span())


# Groups indicated with '(', ')' also capture the starting and ending index of
# the text that they match; this can be retrieved by passing an argument to group(), start(), end(), and span()
p = re.compile('(a)b')
m = p.match('ab')
print(m.group())
print(m.group(0))

# Sub group
p = re.compile('(a(b)c)d')
m = p.match('abcd')
# there whill be 3 group becuase there is two parenthesis
print(m.group(0))
print(m.group(1))
print(m.group(2))
# or
print(m.group(0,1,2))
# The groups() method returns a tuple containing the strings for all the subgroups, from 1 up to however many there are.
print("groups()",m.groups())

print('****************************************************** \1 in subgroup ***************************************************************')
p = re.compile(r'\b(\w+)\s+\1\b')
# The regex engine starts at the beginning of the string.
# \b(\w+) matches the word "Paris".it start match from (w+) because it is in lowest level of grouping
# \s+ matches the space after "Paris".
# \1 is a backreference, which tries to match the exact text captured by the first capturing group, which is "Paris". So, it tries to find another occurrence of "Paris".
# The regex engine fails to find another occurrence of "Paris" immediately after the space.
# The regex engine continues to search.
# It matches the next occurrence of "the".
# \s+ matches the space after "the".
# \1 tries to find another occurrence of "the" immediately after the space.
# It successfully finds another occurrence of "the".
# The regex engine matches the entire pattern "the the".
# The matched substring is returned as the result.
print(p.search('Paris in the the spring').group())
