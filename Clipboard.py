import clipboard as cb
multi = ['Vicky']

def Init():
    print('Temporary Init() function is out of Service ;)')
#     yn = input('Wanna EMPTY Clipboard..? (y/n) : ')

#     if yn == 'y':
#         multi = []
#         print('\nClipboard has been set to Default = {}'.format(multi))
#     else:
#         print('\nClipboard is NOT ALTERED...')
        
def show():
    c=0
    line = '-'*30
    print()
    for i in multi:
        print(c+1, '). ', i, 
              end = '\n' + line + '\n')
        c += 1
    return c

def Append():
    multi.append(cb.paste())
    print('\n>>> Copied element : \n\t' + cb.paste() + '\nis Appended in Clipboard...')
    show()

def Remove():
    ask = input('Wanna remove elements from Clipboard..? (y/n) : ')
    if ask == 'y':
        r = show()
        p = int(input('\nEnter index, (less than ' + str(r+1) + ') : '))

        multi.pop(p-1)
        print('\nClipboard contains : ')
        show()
    else:
        print('\n >>> Nothing is Removed from Clipboard...')
        
def Copy():
    e = show()
    j = int(input('Enter index to Copy in Clipboard, (less than -> ' + str(e+1) + ') : '))
    cb.copy(multi[j-1])

    print('\n>>> Successfully Copied in Clipboard : ', cb.paste())

print('\n...go to Kernal -> Restart, to end While loop, or press alphabet instead of integer in Input.\n')

while True: # ...go to Kernal -> Restart, to end While loop, or press alphabet instead of integer in Input.
    print('\n>>> Menu ================================================\n')
    print('1: Init()')
    print('2: Append()')
    print('3: show()')
    print('4: Remove()')
    print('5: Copy()')

    print('\nKindly Press 2 after every Copy to append in Clipboard')
    
    try:
        opt = int(input('\n>>> Enter your Option : '))

        if opt == 1: Init()
        if opt == 2: Append()
        if opt == 3: show()
        if opt == 4: Remove()
        if opt == 5: Copy()
            
    except Exception as e:
        print('\n...Error = ', e)
        break
        
'Thanks for using this Code :)'