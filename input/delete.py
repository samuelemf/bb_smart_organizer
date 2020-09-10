def delete_processed_directories_validation():
    while True:
        choice = input('Do you wish to delete the processed directories? (Y, N): ').lower()
        if choice in ['n', 'y']:
            break
    return (False, True)[choice == 'y']