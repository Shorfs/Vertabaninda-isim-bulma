class Worker:
    def __init__(self, name, age, mail):
        self.name = name
        self.age = age
        self.mail = mail

# Çalışanların listesi
workers = [
    Worker('Enes', 18, 'shorfinn90@gmail.com'),
    Worker('Ali', 25, 'ali@example.com'),
    Worker('Ayşe', 30, 'ayse@example.com')
]

def normalize_name(name):
    # Türkçe karakterlerin İngilizce karşılıklarına dönüştürülmesi
    replacements = {
        'ç': 'c', 'ğ': 'g', 'ı': 'i', 'ö': 'o', 'ş': 's', 'ü': 'u',
        'Ç': 'C', 'Ğ': 'G', 'İ': 'I', 'Ö': 'O', 'Ş': 'S', 'Ü': 'U'
    }
    for tr_char, en_char in replacements.items():
        name = name.replace(tr_char, en_char)
    return name

try:
    search_t = input("Aratmak istediğiniz kişinin ismini yazınız: ").title().strip()

    if not search_t:  # Eğer girdi boşsa
        raise ValueError("Boş bir isim girdiniz. Lütfen geçerli bir isim girin.")

    found = False  # Bulunup bulunmadığını kontrol etmek için
    normalized_search_t = normalize_name(search_t)  # Normalleştirilmiş arama ismi

    for worker in workers:
        if normalize_name(worker.name) == normalized_search_t:
            print(f"İsim: {worker.name}")
            print(f"Yaş: {worker.age}")
            print(f"E-posta: {worker.mail}")
            found = True
            break  # Eşleşme bulundu, döngüden çık

    if not found:
        print('Aradığınız isim veritabanında bulunmamaktadır.')

except ValueError as e:
    print(e)  # Hata mesajını yazdır
