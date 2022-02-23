import tkinter as tk
from PIL import Image, ImageTk
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

indice = 0
max = 0
tous = []
label = None
trombine = None
photo = None
email = None

def foward():
    global indice
    global max
    global label
    global trombine
    global photo
    global email

    if indice == max :
        indice = 0
    else : 
        indice = indice + 1

    # Récupération des informations:
    nom = tous[indice].formater_nom()
    image = tous[indice].formater_image()
    email = tous[indice].email

    label["text"] = nom
    photo = formater_image(image)
    trombine.config(image=photo)

def backwards():
    global indice
    global max
    global label
    global trombine
    global photo
    global email

    if indice == 0 : 
        indice = max
    else :
        indice = indice - 1

    # Récupération des informations:
    nom = tous[indice].formater_nom()
    image = tous[indice].formater_image()
    email = tous[indice].email

    label["text"] = nom
    photo = formater_image(image)
    trombine.config(image=photo)

def sendEmail():
    SENDER_MAIL = "nafoussinafoussinafoussi@gmail.com"
    SENDER_PASSWORD = "Ayaestneeen2016!"
    RECEIVER_MAIL = email
    
    mail_content = '''Salut,
        C'est un message test.
        '''
    # Setup the MIME.
    message = MIMEMultipart()
    message['From'] = SENDER_MAIL
    message['To'] = RECEIVER_MAIL
    message['Subject'] = 'A test mail sent by Python'   #The subject line
    
    # The body and the attachments for the mail.
    message.attach(MIMEText(mail_content, 'plain'))
    
    # Create SMTP session for sending the mail.
    session = smtplib.SMTP('smtp.gmail.com', 587) # Use gmail with port.
    session.starttls() # Enable security.
    session.login(SENDER_MAIL, SENDER_PASSWORD) # Login with mail_id and password.
    text = message.as_string()
    session.sendmail(SENDER_MAIL, RECEIVER_MAIL, text)
    session.quit()

    print('Mail Sent to: ', email)

def formater_image(image) :
    i = Image.open(image)
    photo = ImageTk.PhotoImage(i)
    resized_image= i.resize((300,300), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(resized_image)
    return photo

def afficher(elements):
    global tous
    global max
    global label
    global trombine
    global photo
    global email

    tous = elements
    max = len(tous) - 1

    # Toujours commencer par Tk()
    fenetre = tk.Tk()

    # Récupération des informations:
    nom = tous[indice].formater_nom()
    image = tous[indice].formater_image()
    email = tous[indice].email


    # (nom, image, email) = tous[indice]
    photo = formater_image(image)
    label = tk.Label(fenetre, text = nom)
    trombine = tk.Label(fenetre, image = photo)

    p = tk.PanedWindow(fenetre, orient=tk.HORIZONTAL)
    back_button = tk.Button(fenetre, text='<<', command=backwards)
    email_button = tk.Button(fenetre, text="Send Email", command=sendEmail)
    foward_button = tk.Button(fenetre, text='>>', command=foward)
    p.add(back_button)
    p.add(email_button)
    p.add(foward_button)

    label.pack()
    trombine.pack()
    p.pack()
    fenetre.mainloop()