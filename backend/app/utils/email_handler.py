from fastapi_mail import ConnectionConfig, FastMail, MessageSchema
from app.core.config import settings

conf = ConnectionConfig(
    MAIL_USERNAME=settings.SMTP_USERNAME,
    MAIL_PASSWORD=settings.SMTP_PASSWORD,
    MAIL_FROM=settings.SMTP_FROM_EMAIL,
    MAIL_PORT=settings.SMTP_PORT,
    MAIL_SERVER=settings.SMTP_HOST,
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
)

async def send_email(subject: str, recipients: str, html_content: str):
    try:
      message = MessageSchema(
          subject=subject,
          recipients=[recipients],
          body=html_content,
          subtype="html",
      )

      fm = FastMail(conf)
      await fm.send_message(message)
    except Exception as e:
        print(f"Error sending email: {e}")