from contact_module import add_contact
"""it imports the functions responsible for adding contacts to address_book"""

def main():
    intro = ''
    while intro != 'q':
        # to keep the entry screen present
        intro = ''
        print('\n-------------------------------\n')
        print('S - Show all contacts')
        print('D - Delete a contact')
        print('E - Enter a contact')
        print('Q - Quit')
        print('\n-------------------------------\n')
        intro = input('Press a key to start: ').lower()

        if intro == 's':
            counter1 = len(address_book)
            for index in range(counter1):
                print(index + 1, ' - '.join(address_book[index]))
                # for a nice format on the screen

        elif intro == 'd':
            get_out = ''
            get_out = int(input('Which contact to delete?: '))
            address_book.pop(get_out - 1)
            # a common citizen counts form 1 not from 0


        elif intro == 'e':
            entry = add_contact()
            address_book.append(entry)
            # using the functions form contact_module.py


        elif intro == 'q':
            quit()



address_book = [
                ['Ewa', 'Guz', '333 777 555', 'ewcia@wp.pl'],
                ['Adam', 'Kij', '888 000 777', 'adam@gmail.com'],
                ['Janusz', 'Joki', '999 777 666', 'jaty@wp.pl'],
                ['Marzena', 'Loki', '688 848 849', 'poco@tutu.pl']
                ]


if __name__ == '__main__':

    print('\nAddress Book')


main()
