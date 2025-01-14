import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import re
import socket
from dns import resolver
import requests
import os

# Helper functions
def generate_pitch(name, profession, portfolio_url, client_summary, api_key):
    try:
        API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
        headers = {"Authorization": f"Bearer {api_key}"}

        prompt = f"""<s>[INST]Write a professional and engaging sales pitch email with the following details:
        - Sender: {name}, a {profession}
        - Portfolio: {portfolio_url}
        - Client Context: {client_summary}

        The email should:
        1. Be warm and professional
        2. Reference specific details about the client
        3. Highlight relevant expertise
        4. Include a clear value proposition
        5. Have a compelling call to action

        Write only the email body without any subject line or contact information section.[/INST]</s>"""

        response = requests.post(API_URL, headers=headers, json={
            "inputs": prompt,
            "parameters": {
                "max_length": 1000,
                "temperature": 0.7,
                "top_p": 0.95
            }
        })

        if response.status_code != 200:
            error_message = f"API request failed with status code: {response.status_code}\nDetails: {response.text}"
            raise Exception(error_message)

        generated_text = response.json()[0]["generated_text"]
        return generated_text.split("[/INST]")[-1].strip()

    except Exception as e:
        messagebox.showerror("Error", f"Error generating pitch: {str(e)}")
        return None

def create_email_body(generated_pitch, name, phone, instagram, sender_email):
    contact_section = f"""

Best regards,
{name}

Contact Information:
\ud83d\udcde Phone: {phone}
\ud83d\udcf8 Instagram: {instagram}
\u2709\ufe0f Email: {sender_email}
"""
    return generated_pitch + contact_section

def send_email(sender_email, sender_password, receiver_email, subject, body):
    try:
        smtp_server = "smtp.gmail.com"
        port = 587
        
        message = MIMEMultipart('alternative')
        message['Subject'] = subject
        message['From'] = sender_email
        message['To'] = receiver_email
        
        message.attach(MIMEText(body, 'plain'))
        
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
            messagebox.showinfo("Success", "Email sent successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to send email: {str(e)}")

# GUI Application
def main():
    root = tk.Tk()
    root.title("Sales Pitch Email Sender")
    
    # Input fields
    fields = {
        "Your Email": None,
        "Email Password": None,
        "Client Email": None,
        "Your Name": None,
        "Your Profession": None,
        "Your Phone": None,
        "Instagram Handle": None,
        "Portfolio URL": None,
        "Client Summary": None,
        "API Key": None
    }

    entries = {}

    def on_send():
        try:
            sender_email = entries["Your Email"].get()
            sender_password = entries["Email Password"].get()
            receiver_email = entries["Client Email"].get()
            name = entries["Your Name"].get()
            profession = entries["Your Profession"].get()
            phone = entries["Your Phone"].get()
            instagram = entries["Instagram Handle"].get()
            portfolio_url = entries["Portfolio URL"].get()
            client_summary = entries["Client Summary"].get("1.0", "end").strip()
            api_key = entries["API Key"].get()

            if not all([sender_email, sender_password, receiver_email, name, profession, phone, instagram, portfolio_url, client_summary, api_key]):
                raise ValueError("All fields must be filled out.")

            generated_pitch = generate_pitch(name, profession, portfolio_url, client_summary, api_key)
            if not generated_pitch:
                return

            email_body = create_email_body(generated_pitch, name, phone, instagram, sender_email)
            send_email(sender_email, sender_password, receiver_email, f"Collaboration Opportunity with {name}", email_body)

        except Exception as e:
            # Display the error message in a popup with full details
            tk.Toplevel().withdraw()
            detailed_error = tk.Toplevel()
            detailed_error.title("Error Details")
            error_label = tk.Label(detailed_error, text=f"Error Details:\n{str(e)}", justify=tk.LEFT, wraplength=400)
            error_label.pack(pady=10, padx=10)

    row = 0
    for label in fields:
        tk.Label(root, text=label).grid(row=row, column=0, sticky="e")
        if label == "Client Summary":
            text_widget = tk.Text(root, height=5, width=40)
            text_widget.grid(row=row, column=1, padx=10, pady=5)
            entries[label] = text_widget
        else:
            entry = tk.Entry(root, show="*" if label == "Email Password" else None)
            entry.grid(row=row, column=1, padx=10, pady=5)
            entries[label] = entry
        row += 1

    tk.Button(root, text="Send Email", command=on_send).grid(row=row, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
