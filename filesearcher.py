import os

def main():
    Root='C:\\'

    #file to search For
    searchableItem=input("\ntype the name of the item you'r searching for = ")
    extension=input('\nwhat is the type of the file you are searching for (python/software/text ect...) = ')
    if extension=='python':
        searchableItem += '.py'
    elif extension == 'text':
        searchableItem += '.txt'
    elif extension == 'game':
        searchableItem += '.exe'
    elif extension == 'software':
        searchableItem += '.exe'
    elif extension == 'picture':
        searchableItem += '.png'
    elif extension == 'image':
        searchableItem += '.png'

    check=False
    for folder , sub , file in os.walk(Root):
        for f in file :
            if f == searchableItem:
                check=True
                print(folder+'\\'+searchableItem)
    
    if check == False :
        print(f'\nYour search - {searchableItem} - did not match any documents.\n\nSuggestions:\n\nMake sure that all words are spelled correctly.')

if __name__ == '__main__':
    main()
