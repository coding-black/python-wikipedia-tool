import wikipedia

global title, url, content, find, result

find = input('\nEnter the thing of which  you need wikipedia :- ')

result = wikipedia.page(f'{find}')

print('\n\n')

print(result.title)
print('\n')
print(result.url)
print('\n')
print(result.content)
print('\n')

title = result.title
url = result.url
content = result.content

while True:
    option = input('Do you want to save this data in txt file? [y/n] ')

    if option == 'y' or option == 'Y':
        file = open(f'{find}.txt', 'a', encoding='utf-8')
        file.writelines(f'{title}')
        file.writelines('\n\n')
        file.writelines(f'{url}')
        file.writelines('\n\n')
        file.writelines(f'{content}')
        file.writelines('\n\n')
        file.close()
        print(f'\n\nSuccessfully wrote the data in your program folder in {find}.txt file\n')
        close = input('\nPress any key to exit.\n\n')
        break

    elif option == 'n' or option == 'N':
        print('\nThnx For Using.....\n')
        close = input('\nPress any key to exit.\n\n')
        break

    else:
        print('\n\nEnter valid option.\n\n')