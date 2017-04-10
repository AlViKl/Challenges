import re

print ("Enter e-mail:")

mail = input()

_in = re.search(r"(([a-zA-Z0-9_\-\.\+\^!#\$%&*+\/\=\?\`\|\{\}~']+)|(\"(([\x21\x23-\x5B\x5D-\x7F])|(\\[\x21-\x7F]))*\"))@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?", mail)

if _in:
	{
		print ("Okay: ", _in.group())
	}
else:
	{
		print ("It's not RFC2822")
	}
