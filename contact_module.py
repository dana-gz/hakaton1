
def add_contact():
    """This function adds a contact (name, surname, phone, emial) """
    entry = []
    name = input('Name: ').title()
    surname = input('Surname: ').title()
    phone = input('Phone number: ')
    email = input('E-mail :').lower()

    while name.isalpha() is False:
        name = input('Check name: ').title()
    else:
        entry.append(name)

    while surname.isalpha() is False:
        surname = input('Check surname: ').title()
    else:
        entry.append(surname)

    phone = phone_clear(phone)
    while phone.isdigit() is False:
        phone = input('Phone number (only digits): ')
        phone = phone_clear(phone)

    else:
        phone = phone_format(phone)
        entry.append(phone)

    while is_at(email) is False or is_dot(email) is False:
        email = input('email: ').lower()
    else:
        entry.append(email)

    return entry


def is_at(email):
    """to check the right format of email"""
    if email.count('@') != 1:
        print('Uncorrect e-mail format')
        if email.count('@') == 0:
            print('E-mail must contain [@]')
        elif email.count('@') > 1:
            print('E-mail must contain only 1 [@]')
        return False
    else:
        return True


def is_dot(email):
    """to check the right format of email"""
    if email.count('@') == 1:
        email_cut = email.split('@')
        ending = email_cut[1]
        if ending.count('.') == 0:
            print('Email must contain dot[.] after [@] ')
            return False
        else:
            return True


def phone_clear(phone):
    """clears phone  number from additional signs"""
    phone = phone.replace('.', '')
    phone = phone.replace('-', '')
    phone = phone.replace(' ', '')
    phone = phone.replace('\\', '')
    phone = phone.replace('/', '')
    phone = phone.replace('+', '')
    phone = phone.replace('*', '')
    phone = phone.replace('(', '')
    phone = phone.replace(')', '')
    return phone

def phone_format(phone):
    """adds spaces to phone  number for visibility"""
    phone = phone[0 :-6] + ' ' + phone[-6:-3] + ' ' + phone[-3:-1] + phone[-1]
    return phone


