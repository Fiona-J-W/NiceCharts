
red	=["#460101","#980101","#d40000","#f44800","#fb8b00","#eec73e","#d9bb7a","#fdd99b"]
blue	=["#000442","#0F1781","#252FB7","#3A45E1","#656DDE","#8A91EC"]
gray	=["#222222","#444444","#666666","#888888","#aaaaaa","#cccccc","#eeeeee"]
contrast=["#0000FF","#FF0000","#00FF00","#CF9100","#FF00FF","#00FFFF"]

default=red

table={
"default":default,
"red":red,
"blue":blue,
"gray":gray,
"contrast":contrast
}


def get_color_scheme(name="default"):
	try:
		returnval=table[name.lower()]
	except:
		returnval=default
	
	return returnval
