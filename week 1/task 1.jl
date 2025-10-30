#Prompt user to insert value as an integer.
#Display menu
#option 1 - In one multi-branched decision
#option 2 - Independent if-statement decisions
#option 0 - Exit
#Prompt user to choose option
#Apply following math operations in the options 1 & 2
#One multi-branched decision structure:
#Value is 400 or more => add 44 to the existing value
#lue is 200 or more => add 22 to the existing value
#Value is 100 or more => add 11 to the existing value
#Independent if-statement decisions one after another:
#Value is 400 or more => add 44 to the existing value
#Value is 200 or more => add 22 to the existing value
#Value is 100 or more => add 11 to the existing value
#Exit: “Exiting…”
print("program starting.")
print("testing decision structures.")
Feed = input("insert an integer:")
Value = int(Feed)
print("options")
print("1-in one multi-branched decision")
print("2-in multiple independent if statements")
print("0-Exit")
Feed = input("your choice:")
choice=int(Feed)
if(choice ==1):
    print("choice two")
    elif(choice=0):
    print("Exiting...")
    if ("Value >=400")
        elif(value >=200):
        value+ 44# Do this in any case
      #  value=value+44
      if(value>=200):
        value+=22#Do this in ana case,the value is now 466
        print(f"Result is {value}")
        elif(choice==0):
        print(“Exiting…”)
    else:
        print("unknown option.")
