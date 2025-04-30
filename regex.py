import re

#*****************************************Dot*************************************************************
 
# (Dot.) In the default mode, this matches any character except a newline

#it will find a pattern which end with h and before h there is 5 any char
pattern_1 = r'.....h'

#it is similer to above pattern_1
pattern_2 = r'.{5}h'

#start with v and end with and there is 4 any charactor
pattern_3=r'v.{4}h'
text = "my name is vikesh"
matches = re.findall(pattern_3, text)
print(matches) 

# *************************************************Caret**********************************************************
# it make sure that hello should occure at the begining of the string and in MULTILINE mode also matches immediately after each newline

pattern = r'^hello' #<re.Match object; span=(0, 5), match='hello'>


text = "hello xyz this is hello world"
match = re.search(pattern, text)
print(match)

# *******************************************************************************************

# Matches the end of the string or just before the newline at the end of the string and in MULTILINE mode also matches before a newline

 
text = 'vikesh_foo1\n vk_foo2\n' # output ['foo1', 'foo2']

# it will print foo2 becuase string end with foo2
text_1 = 'vikesh_foo1 vk_foo2' # output ['foo2']

pattern = r'foo.$'  # Matches 'world' at the end of each line
matches = re.findall(pattern, text, flags=re.MULTILINE)
print(matches)


# ***********************************asterisk***************************************************************

# The asterisk (*) in regular expressions (regex) is a metacharacter known as the zero-or-more quantifier. It matches zero or more occurrences of the preceding regular expression
import re

text = "abb aab abb a"
# what is meaning of below pattern : there should be one 'a' and after 'a' there should be zeror or more b with a.
pattern = r'ab*'  #output ['abb', 'a', 'ab', 'abb', 'a']

#there should be 'aa' and after 'aa' there shoudl be zero or more b with 'aa'
pattern = r'aab*'  # output ['aab']
matches = re.findall(pattern, text)
print(matches)


# 
import re

text = "abb aab abc a"

pattern = r'aab*b'  # output ['aab']
matches = re.findall(pattern, text)
print(matches)

# *************************************************************************************************************
# The plus sign (+) in regular expressions (regex) is a metacharacter known as the one-or-more quantifier. It matches one or more occurrences of the preceding regular expression

import re

text = "abbbc abc ac"

# output ['abbb', 'ab']
pattern = r'ab+'  # Matches 'a' followed by one or more 'b's
matches = re.findall(pattern, text)
print(matches)


# *************************************************************************************************************

# Matches zero or one occurrence of the preceding element.The preceding element can be repeated zero or one time
# Matches zero or one occurrence of the preceding element
# The preceding element can be repeated zero or one time

import re

text = "aabb aab abc aa cc"
# match pattern either aab or aa-> there should be 'aa' then after 'aa' there should be zero b or one b ,if there is more then one b give me only 'aa' with one b only.
pattern = r'aab?'  # output ['aab', 'aab', 'aa', 'aab']
matches = re.findall(pattern, text)
print(matches)

# second exmaple
text = "aabbc aab abc aa aabc"
pattern = r'aab?c'  # ['aabc']
matches = re.findall(pattern, text)
print(matches)