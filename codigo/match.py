value = 11

 #match es esquivalente al switch de java
match value:
    case 10|11: # | es o
        print("ok")
    case 15:
        print("Warning")
    case _:
        print("Unknown code")


