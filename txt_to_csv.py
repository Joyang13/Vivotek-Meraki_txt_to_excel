import os
import csv
import re
import time

LINE = r'(\n\s+.+:.+)?'
RESULT = r'\n\s+Result:(Pass|Fail)'

#how we are gonna do this is
#1. create header of csv file
#2. put all .txt file in a list
#3. pass in the files into regex and store it in a tuple, with all files in, we will have a list of tuples
#5. write the list of tuples into the csv file

def main():
    startime = time.time()    
    os.chdir('/Users/joseph/Documents/Paper Work/晶睿/MRKI_txt_excel')
# /Users/joseph/Desktop/log

    #create the header of csv file
    write_csv_head()

    #put all .txt files in files
    files = []              #contains all of the .txt files
    for f in os.listdir():
        if f.endswith(".txt"):
            files.append(f)
    
    tuples_list = []
    for file in files:
        #now input a file, output a list of tuples that we need
        tup = get_data(file)
        tuples_list.append(tup)
    
    csv_write(tuples_list)

    endtime = time.time()
    print(endtime - startime)


def write_csv_head():
    with open('meraki.csv', 'w', newline = '') as csv_file:   
        the_writer = csv.writer(csv_file)
        the_writer.writerow(['S/N', 'TestDate', 'Firmware version', 'Model Name',
                             'Network-Ping_time','Network-Minor Number from MES', 'Network-Result',
                             'Check Setting-Firmware version', 'Check Setting-Model Name', 'Check Setting-Result',
                             'Auto Test-Ethernet', 'Auto Test-DRAM', 'Auto Test-USB', 'Auto Test-Audio Record', 'Auto Test-Video Sensor', 'Auto Test-Wireless', 'Auto Test-BurnIn', 'Auto Test-RTC', 'Auto Test-Result', 
                             'Button-seconds','Button-Result', 
                             'LED-Orange', 'LED-Green', 'LED-Blue', 'LED-Red','LED-Result',
                             'Light Sensor-Led on criterial','Light Sensor-Led off criterial','Light Sensor-Led on of sensor value','Light Sensor-Led off of sensor value', 'Light Sensor-Result',
                             'VideoAudio-Led on & IR-cut off Y-value', 'VideoAudio-Led on & IR-cut on Y-value', 'VideoAudio-IR-Cut','VideoAudio-Led off & IR-cut on Y-value:', 'VideoAudio-Led','VideoAudio-Audio Record', 'VideoAudio-Video IR-Cut off', 'VideoAudio-Video IR-Cut on','VideoAudio-Result', 
                             'Upgrade Firmware-Upgrade FW Ping Time','Upgrade Firmware-Result', 
                             'Update Mac and Sn-Cable IP ', 'Update Mac and Sn-Meraki FW Ping Time', 'Update Mac and Sn-OP Scan MAC', 'Update Mac and Sn-DUT odm mac read','Update Mac and Sn-OP Scan SN', 'Update Mac and Sn-DUT odm serial_num read', 'Update Mac and Sn-Setting Product ID', 'Update Mac and Sn-DUT odm product_id read', 'Update Mac and Sn-Setting minor number', 'Update Mac and Sn-DUT odm hw_minor read','Update Mac and Sn-Result', 
                             'Check Mac and Sn-Cable IP', 'Check Mac and Sn-Meraki FW Ping Time', 'Check Mac and Sn-OP Scan MAC', 'Check Mac and Sn-DUT odm mac read','Check Mac and Sn-OP Scan SN', 'Check Mac and Sn-DUT odm serial_num read', 'Check Mac and Sn-Setting Product ID', 'Check Mac and Sn-DUT odm product_id read', 'Check Mac and Sn-Setting minor number', 'Check Mac and Sn-DUT odm hw_minor read','Check Mac and Sn-Result', 
                             'Security Boot-odm sec_boot_enable', 'Security Boot-Result'])

#input a .txt file
#output a tup that consists of all data
def get_data(file):
    total = ()             
    # store the file name into the tuple                      
    total = total + (file.split('.')[0], )

    with open(file, 'r') as raw:
        text = raw.read()   #text is a string

    #start with basic information, input string and tup we wanna return
    total = bi(text, total)

    #list of regex's that needs to be proceced
    reg_list = [r'Network' + line(3), r'Check Setting' + line(3), r'Auto Test' + line(9), r'Button' + line(2), 
                r'LED' + line(5), r'Light Sensor' + line(5), r'VideoAudio\n\s+.+' + LINE + LINE  + LINE  + LINE + LINE + LINE, 
                r'Video Verify' + line(3), r'Upgrade Firmware'+ line(2), r'Update Mac and Sn' + line(11), 
                r'Check Mac and Sn' + line(11), r'Security Boot' + LINE + r'\n.+\n.+\n.+' + LINE]
    
    for regex in reg_list:
        total = case_n(text, total, regex)

    return (total)

def bi(string, tuple):
    #regex for bi
    results = re.findall(r'Test Date:(.+)?\nFirmware version:(.+)?\nModel Name:(.+)?', string)
    
    #adding the information into tuple
    for i in range (0 , 3):
        tuple = tuple + (results[0][i], )
    return tuple

def line(count):
    return (LINE*(count - 1) + RESULT)


def case_n(string, tuple, reg):
    #regex for test case 1
    results = re.findall(reg, string)

    #check if the tuple is a line and only adds the data into the tuple
    for result in results:
        for res in result:
            checks = re.findall(r'\n\s+[^:]+:(.+)', res)
            if checks:
                for check in checks:
                    tuple = tuple + (check, )
            else:
                tuple = tuple + (res, )
    return (tuple)


def csv_write(tuples_list):       #inputs iterator, which contains data that should be written in csv
    with open('meraki.csv', 'a', newline = '') as csv_f:
        for i, data in enumerate(tuples_list):
            the_writer = csv.writer(csv_f)
            the_writer.writerow(data)



if __name__ == '__main__':
    main()