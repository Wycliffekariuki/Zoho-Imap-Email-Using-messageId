import imaplib
import email
from django.conf import settings

def fetch_email_by_message_id(message_id):
    try:
        imap = imaplib.IMAP4_SSL(settings.IMAP_SERVER, settings.IMAP_PORT)
        imap.login(settings.SMTP_OPTI_USER, settings.SMTP_OPTI_PASS)
        
        imap.select("Inbox")
        # Do not append anything to the message_id just parse it as is
        _, msgnums = imap.search('UID', '1741689685336130300')
        
        for msgnum in msgnums[0].split():
            _, data = imap.fetch(msgnum, "(RFC822)")
            
            message = email.message_from_bytes(data[0][1])
            
            # You can obtain more data from the message Array as needed
            return {"error": False, "data": f"From: {message.get('From')},To: {message.get('To')}"}
        
    except Exception as e:
        return {"error": True, "message": e}
        
