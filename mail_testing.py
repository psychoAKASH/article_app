import requests

API_KEY = ""  # Replace with your Brevo API key
sender_email = "ak****a@gmail.com"
receiver_email = "kr****@gmail.com"

url = "https://api.brevo.com/v3/smtp/email"

headers = {
    "accept": "application/json",
    "api-key": API_KEY,
    "content-type": "application/json"
}

data = {
    "sender": {"name": "Your Name", "email": sender_email},
    "to": [{"email": receiver_email, "name": "Recipient"}],
    "subject": "Brevo API Test Email",
    "htmlContent": "<html><body><h1>Hello from Brevo API!</h1><p>This is a test email sent using Brevo's API.</p></body></html>"
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 201:
    print("✅ Email sent successfully via Brevo API!")
else:
    print("❌ Failed to send email.")
    print("Status code:", response.status_code)
    print("Response:", response.text)
