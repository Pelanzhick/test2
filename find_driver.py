import win32api
driver_list = list()

drivers = win32api.GetLogicalDriveStrings()
drivers = drivers.split("\000")[:-1]

for i in drivers:
    x = i.replace("\\" ,"")
    driver_list.append(x)

print(driver_list)