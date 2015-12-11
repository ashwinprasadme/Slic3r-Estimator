import smtplib
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_ACK(to_addr,name,order_id):

    fromaddr = '<email>'
    toaddrs  = to_addr
    # msg = 'There was a terrible error that occured and I wanted you to know!'

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Acknowledgement - Order No: " + str(order_id)
    msg['From'] = fromaddr
    msg['To'] = toaddrs

    # Create the body of the message (a plain-text and an HTML version).
    text = "Thanks for your interest, You'll receive an email with the estimations soon..."
    html = """
    <html>
      <head></head>
      <body>
      </body>
    </html>
    """
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)


    # Credentials (if needed)
    username = '*
    password = '*'

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg.as_string())
    server.quit()

def send_estimation(to_addr,time,cost,name,filename,order_id):

    first = os.path.splitext(os.path.basename(filename))[0]
    gcode_Sliced = first + '.gcode'
    path_to_gcode = "<host>/uploads/" + gcode_Sliced

    fromaddr = '<email>'
    toaddrs  = to_addr
    # msg = 'There was a terrible error that occured and I wanted you to know!'

    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Estimation for Order No: " + str(order_id)
    msg['From'] = fromaddr
    msg['To'] = toaddrs

    # Create the body of the message (a plain-text and an HTML version).
    text = "html disabled?  Time: " + str(time) + "Cost: " + str(cost)
    html = """\
    <html>
      <head></head>
      <body>
              </body>
      <h6 style="color: #444"> NOTE: Time & Cost are auto-generated and sometimes vary! </h6>
    </html>
    """

    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    msg.attach(part1)
    msg.attach(part2)


    # Credentials (if needed)
    username = 'email'
    password = 'pass'

    # The actual mail send
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg.as_string())
    server.quit()
