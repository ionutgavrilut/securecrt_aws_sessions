#$language = "Python"
#$interface = "1.0"

def Main():
 crt.Screen.SendSpecial("MENU_TOGGLE_SESSION_MANAGER")
 crt.Sleep(500)
 crt.Screen.SendSpecial("MENU_TOGGLE_SESSION_MANAGER")
 crt.Sleep(100)	 
	 
Main()
