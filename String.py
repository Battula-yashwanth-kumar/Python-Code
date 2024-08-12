word='amazing';
# word[0:7]-> output: amazing it takes from 0to6 charcters.
# word[-7:0]-> outputs : amazing 
# word[ :5] -->output: amazi (takes 0 as default)
# word[3:]---> output:zing (takes length of the string as default)
# word[1:6:2]-->output:mzn (takes the every second character from substring of length 1 to 6);
print(len(word))
print(word.count('0'))  #count the no.of characters in the string of that particular char;
print(word.capitalize()) #capitalize the first character of the word
print(word.upper())
print(word.lower())
print(word.find('am'))  #return the index of the string
print(word.replace("am","YA"))
print(word.endswith("ing"))