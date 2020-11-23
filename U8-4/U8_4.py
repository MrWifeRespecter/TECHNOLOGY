månader=["Januari", "Februari", "Mars", "April", "Maj", "Juni", "Juli", "Augusti", "September", "Oktober", "November", "December"]
månad=int(input("Vilket månadsnummer vill du göra om till månad? "))
if månad in range(1,13):
    print(månader[månad-1])
else:
    print("Svara med siffror mellan 1-12")
input()