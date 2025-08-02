Voice-Controlled Email Assistant for Visually Impaired Users
Overview
This application provides a completely voice-controlled email system designed specifically for blind or visually impaired users. It allows users to send emails and check their inbox using only voice commands, with comprehensive audio feedback at every step.

Key Accessibility Features
100% voice-controlled interface - No visual interaction required

Verification system - All recognized speech is read back for confirmation

Natural language processing - Understands email formats like "example at gmail dot com"

Clear audio feedback - Every action is verbally confirmed

Error tolerance - Multiple retry options for misunderstood commands

System Requirements
Windows, MacOS, or Linux

Python 3.6 or later

Internet connection (for speech recognition and email services)

Microphone

Installation Guide
Install Python from python.org

Open Command Prompt and install dependencies:

text
pip install SpeechRecognition pyglet gTTS
Download the script file

Setup Instructions for Blind Users
After installation, run the script with your screen reader active

The system will immediately begin speaking instructions

When prompted, say "send" to compose email or "check" to check inbox

Voice Commands
Main Menu:
"Send" or "Compose" - Start composing a new email

"Check" or "Inbox" - Check your unread emails

"Exit" - Quit the application (not currently implemented)

During Email Composition:
Speak naturally when providing email addresses (e.g., "john at gmail dot com")

For confirmation prompts, say "yes" to confirm or "no" to retry

Dictate your message naturally when prompted

Security Notice
The script currently contains hardcoded email credentials

For secure usage:

Create a dedicated email account for this application

Use an app-specific password if your email provider supports it

Consider using environment variables for credentials

Troubleshooting for Blind Users
If the application stops responding:

Wait for the current audio to finish playing

Speak clearly into the microphone

If no response, press Ctrl+C in the terminal to restart

Common issues:

"I didn't understand that" - Speak more clearly or reduce background noise

"Error with the service" - Check your internet connection

Emails not sending - Verify your email credentials are correct

Future Accessibility Improvements Planned
Keyboard shortcut integration for screen reader users

Volume control commands

Option to repeat instructions

Braille display support

Support
For assistance with this accessibility tool, please contact:
[Your contact information here]

Note: This application is designed to work with screen readers but operates independently once launched. All interactions are through voice only.
