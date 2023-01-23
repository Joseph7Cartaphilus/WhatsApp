import pywhatkit


def send_message_now():
    """Отправка сообщения получателя (сразу)"""
    mobile = input('Введите номер получателя: ')
    message = input('Введите текс сообщения: ')

    pywhatkit.sendwhatmsg_instantly(phone_no=mobile, message=message)


def send_message_time():
    """Отправка сообщения получателя (в указанное время)"""
    mobile = input('Введите номер получателя: ')
    message = input('Введите текс сообщения: ')
    hours = int(input('Введите часы: '))
    minutes = int(input('Введите минуты: '))

    pywhatkit.sendwhatmsg(phone_no=mobile, message=message, time_hour=hours, time_min=minutes)


def main():
    send_message_now()


if __name__ == "__main__":
    main()
