# -*- coding: utf-8 -*-

def send_email(message: str, recipient: str, *, sender: str = 'university.help@gmail.com') -> None:
    email_char = '@'
    head_domain = ['.com', '.ru', '.net']

    # Проверка наличия '@' в адресе получателя
    if email_char not in recipient:
        print(f'Получатель имеет не верный адрес <{recipient}>.')
        return

    # Проверка домена получателя
    if not any(recipient.endswith(domain) for domain in head_domain):
        print(f'Невозможно отправить письмо на адрес <{recipient}>.')
        return

    # Проверка самопосылки
    if recipient.lower() == sender.lower():
        print('Нельзя отправить письмо самому себе!')
        return

    # Отправка письма
    if sender.lower() == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса <{sender}> на адрес <{recipient}>.')
    else:
        print(f'НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса <{sender}> на адрес <{recipient}>.')


if __name__ == "__main__":
    send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
    send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
    send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
    send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
