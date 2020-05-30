# python automation program to check all running processes information (process id, process name, username, memory usage) write information in text file
import psutil;
import time;
import schedule;


def ProcessDisplay():
    filename = "processlogger.txt"

    line = "-" * 40;
    fobj = open(filename, 'w');

    fobj.write(line + "\n");
    fobj.write("Process Logger at : %s\n" % time.ctime());
    fobj.write(line + "\n");

    for pobj in psutil.process_iter():
        fobj.write(str(pobj));
        fobj.write("\n");

    fobj.close();
    print("File stored !!")

def main():
    schedule.every(1).minute.do(ProcessDisplay); #scheduler to run function after every 1 minute

    while True:
        schedule.run_pending();
        time.sleep(1);


if __name__ == "__main__":
    main();
