class stack:
    def __init__(self):
        self.item=[]
    
    def is_empty(self): #untuk memeriksa apaka stack kosong
        return len(self.item)==0
    
    def push(self, item): #untuk menambahkan item di posisi paling atas
        self.item.append(item)
    
    def pop(self): #untuk mengapus item paling atas
        if self.is_empty():
            return 'buku kosong'
        return self.item.pop()
    
    def peek(self): #melihat data pada tumpukan paling aatas
        if self.is_empty():
            return 'buku kosong'
        return self.item[-1]
    
    def size(self): #untuk mengetahui jumlah jumlah data d
        return len(self.item)
 
class queue:
    def __init__(self):
        self.item=[]
        
    def is_empty(self): #untuk memeriksa apakah queue kosong
        return len(self.item)==0
        
    def enqueue(self, item): #menambahkan antrian pada list
        self.item.append(item)
        
    def dequeue(self): #menghapus antrian pada lis
        if self.is_empty():
            return 'antrian kosong'
        return self.item.pop(0)
        
    def size(self): #untuk mengetahui jumlah jumlah data 
        return len(self.item)
        
class buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis

    def __str__(self):
        return f'{self.judul} oleh {self.penulis}'

   
book_stack = stack()
book_queue = queue()

#array 2 dimensi untuk menyimpan buku
borrowed_book = []

#fungsi untuk menyumbangkan buku
def add_book():
    jml = int(input('masukan jumlah buku yg ingin anda sumbangkan: ')) 

    for i in range(jml):
        print('buku ke -' + str(i+1))
        judul = input('masukan judul buku: ')
        penulis = input('masukan nama penulis: ')
        book = buku(judul, penulis)
        book_stack.push(book)
        book_queue.enqueue(book)
        print(f"buku '{judul}' telah ditambahkan")

#fungsi untuk meminjam buku 
def borrow_book(): 
    if book_stack.is_empty():
        print('buku kosong,')
        print('sumbang buku anda untuk membantu kami')
    else:
        print('buku yg tersedia')
        for i, book in enumerate(book_stack.item, 1):
            print(f'{i}. {book}')

        choice = int(input('masukan nama buku yang ingin dipinjam: '))
        if choice < 1 or choice > book_stack.size():
            print ('gagal pilih ulang')
        else:
            book = book_stack.item[choice - 1]
            book_stack.item.pop(choice - 1)
            borrowed_book.append(book)
            print(f"kamu telah meminjam buku '{book.judul}'")

#fungsi untuk mengembalikan buku
def return_book():
    if len(borrowed_book) == 0:
        print('tidak ada buku yg kamu pinjam')
    else:
        print('buku yang dipinjam: ')
        for i, book in enumerate(borrowed_book):
            print(f"{i+1}. {book.judul} oleh {book.penulis}")
        choice = int(input('masukan buku yang ingin kamu kembalikan: '))
        if choice < 1 or choice > len(borrowed_book):
            print('gagal, silahkan coba lagi')
        else:
            book = borrowed_book.pop(choice -1)
            book_stack.push(book)
            print(f"kamu telah mengembalikan {book.judul}")
            

#fungsi untuk menampilkan buku
def display_book():
    if book_stack.is_empty():
        print('buku sedang kosong')
    else:
        print('buku yang tersedia: ')
        for book in book_stack.item:
            print('-', book)

#menu utama
def main_menu():
    print('\n\n|===================================================|')
    print('|         SELAMAT DATANG DI PERPUSTAKAAN KAMI!      |')
    print('|===================================================|')
    print('|===================================================|')
    print('|             pilih opsi dibawah ini                |')
    print('|---------------------------------------------------|')
    print('| 1. menyumbangkan buku ke tempat kami              |')
    print('| 2. meminjam buku                                  |')
    print('| 3. mengembalikan buku                             |')
    print('| 4. melihat buku yang tersedia                     |')
    print('| 5. exit                                           |')
    print('|---------------------------------------------------|')
    choice=input('pilih opsi: ')

    if choice == '1':
        add_book()  #memanggil fungsi menyumbangkan buku
        a = input('ada yang ingin memilih opsi lagi(y/n)?  ')
        if a == 'y':
            return main_menu()
        else:
            print('terima kasih telah mengunjungi perpustakaan kami')
            breakpoint

    elif choice == '2':
        borrow_book() #memanggil fungsi minjam buku
        a = input('ada yang ingin memilih opsi lagi(y/n)?   ')
        if a == 'y':
            return main_menu()
        else:
            print('terima kasih telah mengunjungi perpustakaan kami')
            breakpoint
    elif choice == '3':
        return_book()  #memanggil fungsi mengembalikan buku
        a = input('ada yang ingin memilih opsi lagi(y/n)?   ')
        if a == 'y':
            return main_menu()
        else:
            print('terima kasih telah mengunjungi perpustakaan kami')
            breakpoint
    elif choice == '4':
        display_book() #memanggil fungsi menampilkan buku
        a = input('ada yang ingin memilih opsi lagi(y/n)?   ')
        if a == 'y':
            return main_menu()
        else:
            print('terima kasih telah mengunjungi perpustakaan kami')
            breakpoint
    elif choice == '5':
        print('terima kasih telah mengunjungi perpustakaan kami kami')
        breakpoint()
    else:
        print('=========pilih angka 1-5===========')
        main_menu()
    
    
main_menu()