import neo

def judul():
    print("BIODATA")

def nama(depan, tengah, belakang):
    lengkap = depan + tengah + belakang
    print ("Nama : " + lengkap)
    return lengkap

def hobi(*hobbies):
    print ("Hobi : " + hobbies[0])

def pendidikan(pend1, pend2, pend3, pend4):
    print ("Pendidikan saat ini : " + pend4)

def makanan_baru(food):
    food.append("mie aceh")
    print ('Makanan favorit : {}'.format(food))

food = ["bakso"]

judul()
nama("Kintan", "Puti", "Alami")
hobi("main game", "memasak", "dance")
pendidikan(pend1 = "sd", pend2 = "smp", pend3 = "sma", pend4 = "kuliah")
makanan_baru(food)
neo.neo()

print ("Bilangan genap anatara 1-10")
bil_genap = lambda x : x%2 == 0
print (list (filter(bil_genap, range(11))))

