import time
import datetime
print("lütfen 3 saniye sonra yazınız")
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("basla!")
time.sleep(0.2)

once = datetime.datetime.now()

yazi = input("yazi yazin:")
sonra = datetime.datetime.now()
hiz = sonra-once
saniye = round(hiz.total_seconds(),2)
lps = round(len(yazi) / saniye,1)
print(f"you typed in : {saniye}seconds")
print(f"{lps}letter per seconds")