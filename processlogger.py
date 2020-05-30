# python automation program to check all running processes information (process id, process name, username, memory usage) write information in text file
import psutil;
import schedule;
import time;

def ProcessDisplay():
    filename = "processlogger.txt"      # file name
    listprocess = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid','name','username'])
            pinfo['vms'] = proc.memory_info().vms/(1024*1024)
            listprocess.append(pinfo);
        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    line = "-" * 40;
    fobj = open(filename, 'w'); # open file
    fobj.write(line+"\n");
    fobj.write("Process Logger at : %s\n"%time.ctime());
    fobj.write(line+"\n");

    for elem in listprocess:
        fobj.write("PID is : %s " %str(elem['pid']) + ", Name : %s " %str(elem['name']) + ", Memory : %s " %str(elem['vms']) + ", Username : %s " %str(elem['username'])) # write information in file
        fobj.write("\n")

    fobj.close()
    print("File generated !!")

def main():
    print("Process Monitor with memory usage")
    schedule.every(20).seconds.do(ProcessDisplay) #scheduler to run function after every 20 seconds
    while True:
        schedule.run_pending();
        time.sleep(1);

if __name__ == "__main__":
    main()
