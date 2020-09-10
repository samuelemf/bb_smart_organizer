def welcome():
    with open('resource/welcome.txt', 'r') as welcome_file:
        for line in welcome_file:
            print(line, end='')
    print('\n')
    print('* | '*25, end='')
    print('*\n\nWelcome to the Black Board Smart Organizer, the automatic students submission organizer.')
    print('This was created with specific details based on the Polytechnic University of Puerto Rico at San Juan.')
    print('\nAuthor: Samuel Matos Flores\n\te:matos_130418@students.pupr.edu'
          '\n\tRepository: https://github.com/samuelemf/bb_smart_organizer\n')
    print('* | ' * 25, end='')
    print('*\n')
