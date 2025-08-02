import speech_recognition as sr
import smtplib
import imaplib
import email
from gtts import gTTS
import pyglet
import os
import time

# Function to play audio using pyglet
def play_audio(text, file_path):
    if text:  # Ensure text is not empty
        tts = gTTS(text=text, lang='en')
        tts.save(file_path)
        music = pyglet.media.load(file_path, streaming=False)
        music.play()
        time.sleep(music.duration)
        os.remove(file_path)

# Function to get simple voice input (used for confirmation)
def get_simple_voice_input(prompt_text="Please say your confirmation."):
    play_audio(prompt_text, r"C:\Users\Abdul Qadir\Desktop\prompt.mp3")
    recognizer = sr.Recognizer()
    
    with sr.Microphone() as source:
        # Adjust for ambient noise and display message
        print("Adjusting for ambient noise, please wait...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Ambient noise adjustment complete.")
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio, language='en-US')
    except sr.UnknownValueError:
        play_audio("Sorry, I did not understand that.", r"C:\Users\Abdul Qadir\Desktop\error.mp3")
    except sr.RequestError as e:
        play_audio(f"Error with the Google Speech Recognition service: {e}", r"C:\Users\Abdul Qadir\Desktop\error.mp3")
    return None

# Function to get voice input with confirmation (includes ambient noise adjustment)
def get_voice_input_with_confirmation(prompt_text):
    while True:
        play_audio(prompt_text, r"C:\Users\Abdul Qadir\Desktop\prompt.mp3")
        recognizer = sr.Recognizer()
        
        with sr.Microphone() as source:
            # Adjust for ambient noise and display message
            print("Adjusting for ambient noise, please wait...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Ambient noise adjustment complete.")
            print(prompt_text)
            audio = recognizer.listen(source)

        try:
            print("Recognizing speech...")
            text = recognizer.recognize_google(audio, language='en-US')
            text = text.strip()  # Remove any leading/trailing whitespace
            print(f"Recognized text: {text}")

            # Ask user to confirm the recognized text
            play_audio(f"Did you say {text}? Please say yes or no.", r"C:\Users\Abdul Qadir\Desktop\confirm.mp3")
            confirmation = get_simple_voice_input()  # No empty string passed

            if confirmation.lower() in ["yes", "yeah", "correct"]:
                return text
            elif confirmation.lower() in ["no", "nope", "incorrect"]:
                play_audio("Let's try again.", r"C:\Users\Abdul Qadir\Desktop\retry.mp3")
            else:
                play_audio("Sorry, I did not understand your confirmation.", r"C:\Users\Abdul Qadir\Desktop\error.mp3")

        except sr.UnknownValueError:
            play_audio("Sorry, I did not understand that.", r"C:\Users\Abdul Qadir\Desktop\error.mp3")
        except sr.RequestError as e:
            play_audio(f"Error with the Google Speech Recognition service: {e}", r"C:\Users\Abdul Qadir\Desktop\error.mp3")

# Function to send an email
def send_email():
    # Step 1: Get the receiver's email address using voice input
    receiver_email = get_voice_input_with_confirmation("Please say the receiver's email address.")

    if receiver_email:
        # Step 2: Remove any whitespaces, replace 'at' with '@', and 'dot' with '.'
        receiver_email = receiver_email.lower().replace(" at ", "@").replace(" dot ", ".").replace(" ", "").strip()

        # Step 3: Display the correctly formatted email address on screen (no 'at' or 'dot')
        print(f"Formatted Email: {receiver_email}")

        # Step 4: Verbally confirm the email address, but replace '@' and '.' with 'at' and 'dot' for speech
        formatted_email_for_speech = receiver_email.replace("@", " at ").replace(".", " dot ")
        play_audio(f"The email address is {formatted_email_for_speech}. Please confirm.", r"C:\Users\Abdul Qadir\Desktop\email_confirm.mp3")
        confirmation = get_simple_voice_input("Is the email correct? Please say yes or no.")

        if confirmation.lower() in ["yes", "yeah", "correct"]:
            # Step 5: Get the message content using voice input
            message = get_voice_input_with_confirmation("Please say your message.")

            if message:
                try:
                    # Step 6: Send the email using the correctly formatted email address
                    mail = smtplib.SMTP('smtp.gmail.com', 587)
                    mail.ehlo()
                    mail.starttls()
                    mail.login('muibudeenabdulquadri@gmail.com', 'szsi gmjn kguv lkbq')  # Use app password if 2FA is enabled
                    mail.sendmail('muibudeenabdulquadri@gmail.com', receiver_email, message)
                    mail.close()

                    play_audio("Congrats! Your mail has been sent.", r"C:\Users\Abdul Qadir\Desktop\send.mp3")
                except Exception as e:
                    play_audio(f"Error sending email: {e}", r"C:\Users\Abdul Qadir\Desktop\error.mp3")
            else:
                play_audio("No message provided. Email not sent.", r"C:\Users\Abdul Qadir\Desktop\error.mp3")
        else:
            play_audio("Email address was not confirmed. Please try again.", r"C:\Users\Abdul Qadir\Desktop\error.mp3")
    else:
        play_audio("No email address provided. Email not sent.", r"C:\Users\Abdul Qadir\Desktop\error.mp3")

# Function to check inbox (includes ambient noise adjustment)
def check_inbox():
    try:
        # Connect to the email server
        mail = imaplib.IMAP4_SSL('imap.gmail.com', 993)
        mail.login('muibudeenabdulquadri@gmail.com', 'szsi gmjn kguv lkbq')  # Use app password if 2FA is enabled

        # Select inbox
        mail.select('inbox')

        # Search for unseen emails
        status, unseen_emails = mail.search(None, 'UNSEEN')

        # Get email details
        if unseen_emails[0]:
            num_unseen = len(unseen_emails[0].split())
            play_audio(f"You have {num_unseen} unseen emails.", r"C:\Users\Abdul Qadir\Desktop\unseen.mp3")
        else:
            play_audio("You have no new emails.", r"C:\Users\Abdul Qadir\Desktop\no_unseen.mp3")

        # Fetch and display the latest email
        if unseen_emails[0]:
            status, email_data = mail.fetch(unseen_emails[0].split()[-1], '(RFC822)')
            raw_email = email_data[0][1].decode("utf-8")
            email_message = email.message_from_string(raw_email)

            play_audio(f"From: {email_message['From']}. Subject: {email_message['Subject']}.", r"C:\Users\Abdul Qadir\Desktop\latest_email.mp3")

        # Logout
        mail.logout()
    except Exception as e:
        play_audio(f"Error checking inbox: {e}", r"C:\Users\Abdul Qadir\Desktop\error.mp3")

# Main Program Loop
def main():
    play_audio("Please say 'send' to compose an email or 'check' to check your inbox.", r"C:\Users\Abdul Qadir\Desktop\options.mp3")
    
    while True:
        option = get_voice_input_with_confirmation("Please select an option.")
        
        if option.lower() in ['send', 'compose']:
            send_email()
        elif option.lower() in ['check', 'inbox']:
            check_inbox()
        else:
            play_audio("Invalid option, please try again.", r"C:\Users\Abdul Qadir\Desktop\error.mp3")

if __name__ == "__main__":
    main()
