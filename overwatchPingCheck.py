import os, platform

host = "24.105.62.129" # Overwatch central servers
hostWest = "24.105.30.129" # Overwatch West servers
print("----- Central Servers -----")
os.system("ping " + ("-n 1 " if platform.system().lower()=="windows" else "-c 1 ") + host)
print("\n----- West Coast Servers -----")
os.system("ping " + ("-n 1 " if platform.system().lower()=="windows" else "-c 1 ") + hostWest)
