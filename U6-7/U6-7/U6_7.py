print('Tal   Kvadrat   Kub')
for i in range(1, 21):
    tal1 = str(i).rjust(2)
    tal2 = str(i * i).rjust(3)
    tal3 = str(i * i * i).rjust(4)
    print(tal1 + '     ' + tal2 + '    ' + tal3)