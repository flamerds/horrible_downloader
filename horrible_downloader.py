# main menu

print('\n1. Check and download new episodes of anime in your currently watching list\t(type 1 to select this)'
      '\n2. Batch download of episodes of an anime\t(type 2 to select this)'
      '\n3. Update currently watching list\t(type 3 to select this)'
      '\n4. Update horrible downloader\t(type 4 to select this)'
      '\n5. Exit\t(type 5 to select this)')     # printing options
choice = input('Choice : ')

if choice == '5':
    exit(0)

elif choice == '1':
    print('\nStarting checks...')
    import horriblefiles.ongoing_downloader

elif choice == '4':
    import horriblefiles.updater

elif choice == '3':
    print('\nBringing up the currently watching list updater...')
    import horriblefiles.update_anime

elif choice == '2':
    print('\nStarting the batch downloader...')
    import horriblefiles.batch_downloader

else:
    print('Invalid option. Please try again.')
