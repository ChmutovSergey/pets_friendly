# coding: utf-8
import os
import smtplib
from configparser import ConfigParser, NoSectionError
from email.header import Header
from email.mime.text import MIMEText
from typing import Dict

from main_app import CONFIGS_PATH
from main_app.base_logger import logger


MAIL_CONFIG_FILE = 'smtp.ini'
MAIL_CONFIG_PATH = os.path.join(CONFIGS_PATH, MAIL_CONFIG_FILE)


def get_smtp_configs() -> Dict[str, str]:
    cfg = ConfigParser()
    cfg.read(MAIL_CONFIG_PATH)

    try:
        server, port = cfg.get('smtp_server', 'server'), cfg.get('smtp_server', 'port')
        sender_mail, sender_password = cfg.get('sender_mail', 'mail'), cfg.get('sender_mail', 'password')
        recipient_mail = cfg.get('recipient_mail', 'mail')
    except NoSectionError as err:
        err_msg = f'{err} in {MAIL_CONFIG_PATH} file'
        logger.error(err_msg)
        return {}

    return {
        'server': server,
        'port': port,
        'sender_mail': sender_mail,
        'sender_password': sender_password,
        'recipient_mail': recipient_mail,
    }


def send_mail(user_name: str, email: str, message_text: str) -> bool:
    send_message_status = False
    logger.info(f'Sending e-mail to {email}')
    smtp_configs = get_smtp_configs()

    if not (user_name and email and message_text):
        return send_message_status

    message_body = f'Отправитель: {user_name}\nE-mail: {email}\nСообщение: {message_text}'

    msg = MIMEText(message_body, 'plain', 'utf-8')
    msg['Subject'] = Header('Центр поддержки', 'utf-8')
    msg['From'] = smtp_configs['sender_mail']
    msg['To'] = smtp_configs['recipient_mail']

    smtp_obj = smtplib.SMTP(smtp_configs['server'], smtp_configs['port'], timeout=5)
    try:
        smtp_obj.starttls()
        smtp_obj.login(smtp_configs['sender_mail'], smtp_configs['sender_password'])
        smtp_obj.sendmail(smtp_configs['sender_mail'], smtp_configs['recipient_mail'], msg.as_string())
    except Exception as err:
        logger.error(err)
    else:
        send_message_status = True

    smtp_obj.close()
    return send_message_status
