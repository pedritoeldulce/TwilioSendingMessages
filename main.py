
from twilio.rest import Client
auth_token = "6331c4be4a683ea005536163cdb256d2"

sid_id = "AC24f635585d6a23f204af962429a23daa"

client = Client(sid_id, auth_token)

# this is the Twilio sandbox testing number
from_whatsapp_number='whatsapp:+14155238886'
# replace this number with your own WhatsApp Messaging number
to_whatsapp_number='whatsapp:+51960400758'

client.messages.create(body='Hola, Noa canoa Xd',
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)

