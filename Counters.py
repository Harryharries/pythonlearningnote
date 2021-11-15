a_list = [1,2,2,3,4,4,4]
a_string = 'data'
a_dict = {'a': 5, 'b':3, 'c':5, 'd':5, 'e':1 }

#counting objects in a list
c_list = Counter(a_list)
#counting characters in a string
c_string = Counter(a_string)
#counting values in a dictionary
c_dict = Counter(a_dict.values())
print (c_list)
print (c_string)
print (c_dict)