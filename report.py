import platform
import os
def main():
    log.write("####REPORT####\n")
    names =  """system platform mac_ver node architecture machine processor""".split()
    for name in names:
            label = name.upper()
            getter = getattr(platform, name)
            value = getter()
            log.write('{}: {}\n'.format(label, value))
            log.write("##############\n")
    log.write("--------------\n" * 3)
    log.close()
lefile = os.path.exists("reportLog.txt")

if (lefile) == True:
        with open("reportLog.txt", "a") as log:
                main()
elif (lefile) == False:
        with open("reportLog.txt", "w") as log:
                main()
else:
    print("ERROR")
    exit

if __name__ == "__main___":
    print("[*] Running report...")
    main()
