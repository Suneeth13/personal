import pywhatkit as pyw
import logging

def send_whatsapp_message(phonenumber, message, hours, minutes):
    """
    Send WhatsApp message using pywhatkit library.

    Args:
    - phone_number (str): Recipient's phone number (including country code).
    - message (str): The message to be sent.
    - hours (int): The hour when the message should be sent.
    - minutes (int): minute in which to send the message.
    """
    Try:
        # Send a WhatsApp message
        pyw.sendwhatmsg(phone_number, message, hours, minutes)
        
        # Record success
        logging.info("Message sent successfully")
        print("Message sent")
    except for an exception like e:
        # Log errors
        logging.error(f"Error sending message: {e}")
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Set logging
    logging.basicConfig(filename='message_log.txt', level=logging.INFO)

    # Usage example
    send_whatsapp_message('+918825402977', 'Hello', 20, 57)
