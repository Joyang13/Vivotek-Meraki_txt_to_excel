import re

string = '''Test Date:2018-05-15 17:33:34
Firmware version:FD9172-MRKI-0400d
Model Name:FD9172HVW-MRKI
--------------------------------------------------
Test Case 1:Network
    Ping_time:0.450000047684
    Minor Number from MES:415
    Result:Pass
Test Case 2:Check Setting
    Firmware version:FD9172-MRKI-0400d
    Model Name:FD9172HVW-MRKI
    Result:Pass
Test Case 3:Auto Test
    Ethernet:Pass
    DRAM:memtester 2M 2 Pass
    USB:Pass
    Audio:Pass
    Video Sensor:Pass
    Wireless:Pass
    BurnIn:Pass
    RTC:Mon Feb 26 14:59:54 2018  0.000000 seconds
    Result:Pass
Test Case 4:Button
    seconds:4.96199989319
    Result:Pass
Test Case 5:LED
    Orange:Pass
    Green:Pass
    Blue:Pass
    Red:Pass
    Result:Pass
Test Case 6:Light Sensor
    Led on criterial:25000
    Led off criterial:100
    Led on of sensor value:33004
    Led off of sensor value:0
    Result:Pass
Test Case 7:VideoAudio
  IR Cut
    Led on & IR-cut off Y-value:36
    Led on & IR-cut on Y-value:88
    IR-Cut:off < on
    Led off & IR-cut on Y-value:17
    Led:off < on
  Audio Record:Pass
  Video Verify
    Video IR-Cut off:Pass
    Video IR-Cut on:Pass
    Result:Pass
Test Case 8:Upgrade Firmware
    Upgrade FW Ping Time:23.0
    Result:Pass
Test Case 9:Update Mac and Sn
    Cable IP:192.168.200.99
    Meraki FW Ping Time:3.28299999237
    OP Scan MAC:34:56:FE:A4:0E:A3
    DUT odm mac read:34:56:FE:A4:0E:A3
    OP Scan SN:Q2EV-3F3L-T65M
    DUT odm serial_num read:Q2EV-3F3L-T65M
    Setting Product ID:meraki_MV12N
    DUT odm product_id read:meraki_MV12N
    Setting minor number:415
    DUT odm hw_minor read:415
    Result:Pass
Test Case 10:Check Mac and Sn
    Cable IP:192.168.200.99
    Meraki FW Ping Time:0.552000045776
    OP Scan MAC:34:56:FE:A4:0E:A3
    DUT odm mac read:34:56:FE:A4:0E:A3
    OP Scan SN:Q2EV-3F3L-T65M
    DUT odm serial_num read:Q2EV-3F3L-T65M
    Setting Product ID:meraki_MV12N
    DUT odm product_id read:meraki_MV12N
    Setting minor number:415
    DUT odm hw_minor read:415
    Result:Pass
Test Case 11:Security Boot
    odm sec_boot_enable:0+1 records in
0+1 records out
436 bytes (436B) copied, 0.004520 seconds, 94.2KB/s
Secure boot written. Device must be rebooted to take effect.
    Result:Pass
Test Result Pass
--------------------------------------------------
'''

#1   Test Date:(.+)?\nFirmware version:(.+)?\nModel Name:(.+)?\n.+?\n.+?\n.+Ping_time:(.+)?\n.+Minor Number from MES:(\d+)?\n.+Result:(.+)?\n
#    .+\n.+Firmware version:(.+)?\n.+Model Name:(.+)?\n.+Result:(.+)?\n
#    .+\n.+Ethernet:(.+)?\n.+DRAM:(.+)?\n.+USB:(.+)?\n.+Audio:(.+)?\n.+Video Sensor:(.+)?\n.+Wireless:(.+)?\n.+BurnIn:(.+)?\n.+RTC:(.+)?\n.+Result:(.+)?\n
#    .+\n.+seconds:(.+)?\n.+Result:(.+)?\n
#5   .+\n.+Orange:(.+)?\n.+Green:(.+)?\n.+Blue:(.+)?\n.+Red:(.+)?\n.+Result:(.+)?\n


#this is where we write the super long as list of regex
# #long list of regex expression
# r = [
# # Dates
# r'Test Date:' + DATUM + TAB + r'Firmware version:' + DATUM + TAB + r'Model Name:' + DATUM,
# #Test Case 1 
# r'Ping_time:' + DATUM + TAB + r'Minor Number from MES:' + DATUM + TAB + r'Result:' + DATUM,
# #Test Case 2
# r'Firmware version:' + DATUM + TAB + r'Model Name:' + DATUM + TAB +  r'Result:' + DATUM,
# #Test Case 3
# r'Ethernet:' + DATUM + TAB + r'DRAM:' + DATUM + TAB + r'USB:' + DATUM + TAB + r'Audio:' + DATUM + TAB + r'Video Sensor:' + DATUM + TAB + r'Wireless:' + DATUM + TAB + r'BurnIn:' + DATUM + TAB + r'RTC:' + DATUM + TAB + r'Result:' + DATUM + TAB
# #Test Case 4
# r'seconds:' + DATUM + TAB + r'Result:' + DATUM,
# #Test case 5 
# r'Orange:' + DATUM + TAB + r'Green:' + DATUM + TAB + r'Blue:' + DATUM + TAB + r'Red:' + DATUM + TAB + r'Result:' + DATUM,
# #Test case 6
# r'Led on of sensor value:' + DATUM, r'Led on:' + DATUM, r'Led off of sensor value:' + DATUM, r'Led off:' + DATUM, r'Result:' + DATUM,
# #Test case 7
# r'Led on & IR-cut off Y-value:' + DATUM r'Led on & IR-cut on Y-value:' + DATUM r'IR-Cut:' + DATUM, r'Led off & IR-cut on Y-value:' + DATUM r'Led:' + DATUM, r'Video IR-Cut off:' + DATUM, r'Video IR-Cut on:' + DATUM, r'Result:' + DATUM,
# #Test case 8
# r'Upgrade FW Ping Time:' + DATUM, r'Result:' + DATUM,
# #Test case 9
# r'Cable IP:' + DATUM, r'Meraki FW Ping Time:' + DATUM, r'OP scan MAC:' + DATUM, r'DUT odm mac read:' + DATUM, r'OP Scan SN:' + DATUM, r'DUT odm serial_num read:' + DATUM, r'Setting Product ID:' + DATUM, r'DUT odm product_id read:' + DATUM, r'Setting minor number:' + DATUM, r'DUT odm hw_minor read:' + DATUM, r'Result:' + DATUM,
# #Test case 10
# r'Cable IP:' + DATUM, r'Meraki FW Ping Time:' + DATUM, r'OP Scan MAC:' + DATUM, r'DUT odm mac read:' + DATUM, r'OP Scan SN:' + DATUM, r'DUT odm serial_num read:' + DATUM, r'Setting Product ID:' + DATUM, r'DUT odm product_id read:' + DATUM, r'Setting minor number:' + DATUM, r'DUT odm hw_minor read:' + DATUM, r'Result:' + DATUM,
# #Test case 11
# r'odm sec_boot_enable:' + DATUM, r'Result:' + DATUM
# ]





#store all of the regex expressions in a long list
#run the list so that all variables are stored in one iterator
#we only need that one iterator and store it in a tuple
#one .txt file has one tuple, later, 100 .txt files we will have 1 list having 100 tuples
#we only need that one list the consists of 100 tuples and store it in .csv file


#this function is to input a file, output a tuble of data we want
#inside the function we store the file in a string
#declare a globale var of a list of regex for data


test_7 = '''
Test Case 7:VideoAudio
  IR Cut
    Led on & IR-cut off Y-value:36
    Led on & IR-cut on Y-value:88
    IR-Cut:off < on
    Led off & IR-cut on Y-value:17
    Led:off < on
  Audio Record:Pass
  Video Verify
    Video IR-Cut off:Pass
    Video IR-Cut on:Pass
    Result:Pass
'''

test_7_1 = '''
Test Case 7:VideoAudio
  IR Cut
    Led on & IR-cut off Y-value:35
    Led on & IR-cut on Y-value:86
    IR-Cut:off < on
    Led off & IR-cut on Y-value:23
    Result:Fail
Test Result Fail
'''

test_7_2 = '''
Test Case:fake
    a_tag:63
    b_tag:13
    result:fail
'''

#6
#r'Test Case 6:Light Sensor' + CAT + DATUM + CAT + DATUM + CAT + DATUM + CAT + DATUM + CAT + DATUM


LINE = r'(\n\s+.+:.+)?'
RESULT = r'\n\s+Result:(Pass|Fail)'
#[^:]*:(.*)\n([^:]*:(.*)\n)?(result):(pass|fail)
# l = [r'Test Case:fake(\n\s+.+:.+)?(\n\s+.+:.+)?\n\s+result:(pass|fail)']
#l = [r'Test Case:fake' + LINE + LINE + RESULT]
l = [r'Test Case 7:VideoAudio\n\s+.+' + LINE + LINE + LINE + LINE+ LINE+ LINE + LINE + LINE + RESULT]
y = [r'\s+Video Verify' + LINE + RESULT]

total = ()
for i in range(0,1):
    results = re.findall(l[i], test_7_1)

for result in results:
    for res in result:
        checks = re.findall(r'\n\s+.+:(.+)', res)
        if checks:
            for check in checks:
                total = total + (check, )
        if not checks:
            total = total + (res, )

print(total)





patterns = re.findall(r'Test Date:(.+)?\nFirmware version', string)
