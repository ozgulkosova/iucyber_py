#odev1

yaricap = float(input("Yarıçap giriniz: "))
pi = 3.14
cevre = float(2 * pi * yaricap)
alan = float(pi * yaricap**2)

print("Dairenin çevresi:", cevre, "cm\nDairenin alanı:", alan, "m2")


#odev2

email = "ozgul@gmail.com"
parola = "werty"
harf_notu = ""

if input("Elektronik posta adresinizi giriniz: ") == email:
    if input("Parolanızı giriniz: ") == parola:
        
        vize_notu = int(input("Vize notunuzu giriniz: "))
        final_notu = int(input("Final notunuzu giriniz: "))
        sinav_notu = (vize_notu + final_notu) / 2
        
        if sinav_notu > 100 or sinav_notu < 0:
            print("Notunuzu yanlış girdiniz.")
        else:
            
            if sinav_notu <= 35:
                harf_notu = "FF"
            elif sinav_notu <= 45:
                harf_notu = "DD"
            elif sinav_notu <= 55:
                harf_notu = "DC"
            elif sinav_notu <= 65:
                harf_notu = "CC"
            elif sinav_notu <=75:
                harf_notu = "CB"
            elif sinav_notu <= 85:
                harf_notu = "BB"
            elif sinav_notu <= 95:
                harf_notu = "BA"
            elif sinav_notu <= 100:
                harf_notu = "AA"
                
print("\nNotunuz: ",harf_notu)










