supported = ["Lights off", "Lock the door", 
    "Open the door", "Make coffee", "Shut down"]
task=input("Şimdi ne yapmak istersiniz: ")
if task in supported:
    print("OK")
else:
    print("Unknown")