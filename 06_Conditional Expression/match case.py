#Match case-Alternative method for if elif else
color = input("Enter color(red,yellow,green): ")
match color:
    case"Green":
        print("GO!!")
    case "Yellow":
        print("Wait...")
    case "Red":
        print("STOP!")
    case _ :
        print("Wrong Color :( ")