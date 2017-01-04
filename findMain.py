import idautils
import idaapi

def main():
	print "--------------- findMain ---------------"
	
	for func in idautils.Functions():
		if GetFunctionName(func).lstrip("_") != "start": 
			continue 
		for addr in idautils.FuncItems(func): 
			if GetMnem(addr) == "call": 
				MakeName(LocByName(GetOpnd(PrevHead(addr, func), 0).split()[1]), "main")
				break

main()



