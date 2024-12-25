def send_email(message, recipient, *, sender = 'university.help@gmail.com'):
    sign = '@'
    while True:
        if recipient.endswith(('.com', '.ru', '.net')) and sender.endswith(('.com', '.ru', '.net')):
            if sign not in recipient and sender:
                print(f'It is not possible to send an email from {sender} to {recipient}')
                break
        else:
            print(f'It is not possible to send an email from {sender} to {recipient}')
            break
        if sender == recipient:
            print(f'You cant send an email to yourself')
            break
        elif sender == 'university.help@gmail.com':
            print(f'The email was successfully sent from {sender} to {recipient}')
            break
        elif sender != 'university.help@gmail.com':
            print(f'NON-STANDARD SENDER! The email was sent from {sender} to {recipient}')
            break


send_email('This is a communication check message.', 'vasyok1337@gmail.com')

send_email('You see this message as the best student of the course!', 'urban.fan@mail.ru', sender = 'urban.info@gmail.com')

send_email('Please correct the task.', 'urban.student@mail.ru', sender = 'urban.teacher@mail.uk')

send_email('I remind myself about the webinar', 'urban.teacher@mail.ru', sender = 'urban.teacher@mail.ru')
