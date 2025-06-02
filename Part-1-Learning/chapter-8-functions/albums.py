def make_album(artist_name, album_title):
    dict = {}
    dict[artist_name] = album_title
    return dict

print(f'Select an option')

while True:
    user_input = int(input('1. Create an album\n2. Exit\n'))
    if user_input == 2:
        print('Exitting')
        break
    user_artist = input(f'Enter the artist name:\n')
    user_album = input(f'Enter the album name\n')
    a = make_album(artist_name = user_artist, album_title = user_album)
    print(a)




