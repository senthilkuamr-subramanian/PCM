# personalized cold mail

This project provides a GUI application for generating professional sales pitch emails using Hugging Face's AI models. The emails can be sent directly through Gmail. The application is built with Python and utilizes `tkinter` for the GUI.

## Features

- Generate professional sales pitch emails based on user inputs.
- Integrate Hugging Face's AI for text generation.
- Send emails directly via Gmail SMTP.

## Requirements

Ensure you have the following installed:

- Python 3.7 or higher
- Required Python libraries:
  - `smtplib`
  - `email`
  - `tkinter`
  - `requests`
  - `dnspython`

Install the required libraries with:
```bash
pip install requests dnspython
```

## How to Use

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/gui-email-pitch.git
cd gui-email-pitch
```

### 2. Run the Application

Run the main script:
```bash
python gui_email_pitch.py
```

### 3. Input Details

Fill in the following fields in the application:

- **Your Email**: Your Gmail address.
- **Email Password**: The app password generated from Gmail (not your Gmail account password).
- **Client Email**: The recipient's email address.
- **Your Name**: Your full name.
- **Your Profession**: Your job title or expertise.
- **Your Phone**: Your phone number.
- **Instagram Handle**: Your Instagram username.
- **Portfolio URL**: A link to your professional portfolio.
- **Client Summary**: A brief description of the client and the context.
- **API Key**: Your Hugging Face API key.

### 4. Generate and Send Email

- Click the **Send Email** button.
- The application will generate a sales pitch email and send it to the client.
- If any error occurs during the process, detailed error messages will be displayed.

## Troubleshooting

- **Hugging Face API Key Issues**: Ensure the API key is valid and the specified model is accessible.
- **SMTP Errors**: Use an app-specific password for Gmail and ensure you’ve enabled "Allow less secure apps" in Gmail settings.
- **Network Issues**: Check your internet connection and ensure the Hugging Face API endpoint is not blocked by a firewall.

## Notes

- This application is designed to work with Gmail. For other email services, you might need to modify the SMTP configuration.
- Make sure your Hugging Face API key has access to the specified model (`mistralai/Mistral-7B-Instruct-v0.2`).
- Be cautious with sharing sensitive information like email passwords and API keys.


## Contributing

Feel free to fork this repository and submit pull requests for any enhancements or bug fixes.

---

For questions or issues, please open an issue in this repository or contact the project maintainer.

