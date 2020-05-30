# python automation program to check specific process information (process id, process name, username, memory usage) using psutil
import psutil;
import time
import schedule

def ProcessDisplay(processName):
    listprocess = [];
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'username'])
            pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
            if processName == pinfo['name']:
                listprocess.append(pinfo)
        except(psutil.NoSuchProcess, psutil.AccessDenied,psutil.ZombieProcess):
            pass

    if len(listprocess) > 1 :
        print("Process is running | details are :")
        for elem in listprocess:
            print(elem)
    else:
        print("Process is not running")

def main():
    process_name = 'chrome.exe' #process name here to check process information
    print("Program to find process details")
    schedule.every(20).seconds.do(ProcessDisplay,process_name) #scheduler to run function after every 20 seconds
    # ProcessDisplay('')
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()