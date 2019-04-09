# String Examples
server_type = 'Ubuntu'
server_name = "rnsServer_01"
server_desc = """ My test server
at Rise n Shine
"""

print ("Server name: ",  server_name)
print ("Length of the String : ",  len(server_desc))

server_desc = "Server " + server_name + " is running " + server_type
print (server_desc)

server_desc = " ".join(("Server", server_name, "is running ", server_type))
print (server_desc)
print ("Length of the String  After Concatnation -- ", len(server_desc))

#Searching a string (is case-sensitive):
print ("Server Desc            :  ", server_desc)
print ("Searching a string	:  ", 'Ubuntu' in server_desc)
print ("Searching a string	:  ", "UbuntU" in server_desc)

#Location of a substring:
print ("Location of a substring:  ", server_desc.find("Ubuntu"))

#Splicing or creating a substring:
# characters 7 to 19
print ("characters 7 to 19 :  ",  server_desc[7:19])
# all characters up to the 6th one
print ("all characters up to the 6th one :  ", server_desc[0:6])
print ("all characters up to the 6th one : ", server_desc[:6])
# last 6 characters
print ("last 6 characters :  ", server_desc[-6:])
# from the 7th to the end
print ("from the 7th to the end : ", server_desc[7:])
