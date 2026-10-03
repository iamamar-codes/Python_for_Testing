#Match and Case
browser = str(input("Enter the browser name\n"))
browser = browser.lower()
match browser:
    case "chrome":
        print("Chrome code execuded!")
    case "firefox":
        print("Firefox code executed")
    case "opera":
        print("Opera code executed")
    case _:
        print("No browser found")