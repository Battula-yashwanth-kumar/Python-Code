import re 

pattern =r"[A-Z]+yclone"
text="Cyclone Dumazile was a strong tropical cyclone in the South-West Indian Ocean that affected Madagascar and Réunion in early March 2018. Dumazile originated from a cyclone Dyclone low-pressure area that formed near Agaléga on 27 February. It became a tropical disturbance on 2 March, and was named the next day after attaining tropical storm status. Dumazile reached its peak intensity on 5 March, with 10-minute sustained winds of 165 km/h (105 mph), 1-minute sustained winds of 205 km/h (125 mph), and a central atmospheric pressure of 945 hPa (27.91 inHg). As it tracked southeastwards, Dumazile weakened steadily over the next couple of days due to wind shear, and became a post-tropical cyclone on 7 March"

match= re.search(pattern,text)
print(match)   #you can get only one match


matches =re.finditer(pattern, text)
for match in matches:
    print(match.span())
    print(text[match.span()[0]:match.span()[1]])



# Regular Expression :

# /([A-Z])\w+\g :
# --> [A-Z] - case sensitive 
# --> \w+ - atleast single character or numeric need to be present after any character betweeen [A-Z] case senstivie
# --> \ regex \g - is common syntax for all the exrpression and \g indicates global search
