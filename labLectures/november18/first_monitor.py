# from time import *
import csv
from time import sleep
# import time 
import psutil

#Lbrary for getting indicators -> https://psutil.readthedocs.io/en

def read_cpu_usage():
    #body of the function
    # return 1
    cpu_t = psutil.cpu_times()
    urs_sp_cputime = cpu_t.user
    idle_time = cpu_t.idle
    cpu_dict = {"idle_time": cpu_t.idle, "usr_time": cpu_t.user}
    cpu_dict["interrupt_time"] = cpu_t.interrupt
    return cpu_dict

def write_dict_to_csv(filename, dict_item, is_first_time):
    
    if(is_first_time):
        f = open(filename, 'w', newline="")
    else:
        f = open(filename, "a", newline="")
    w = csv.DictWriter(f, dict_item.keys())
    if(is_first_time):
        w.writeheader()
    w.writerow(dict_item)
    f.close()

# int main(char* argv, int argc){}

if __name__ == "__main__":

    is_first_time = True
    while True: 
        
        # cpu_usage = read_cpu_usage()
        # print(cpu_usage)

        # #some kind of sleep for 1 second
        # sleep(1)

        # u_t, i_t, cpu_t = read_cpu_usage()
        # print("user time: " + str(u_t) + " idle time: " + str(i_t))
        # print("user time: " + str(u_t) + " idle time: " + str(i_t))
        # sleep(1)
        cpu_dict = read_cpu_usage()
        write_dict_to_csv("my_first_dataset.csv", cpu_dict, is_first_time)
        is_first_time = False
        print(cpu_dict)
        sleep(1)
