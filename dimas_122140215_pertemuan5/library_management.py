from abc import ABC, abstractmethod

# Abstract Class LibraryItem
class LibraryItem(ABC):
    def __init__(self, id, title):
        self.__id = id  # Private attribute
        self.__title = title

    @abstractmethod
    def display_info(self):
        """Method ini harus diimplementasikan oleh subclass"""
        pass

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title


# Subclass Book
class Book(LibraryItem):
    def __init__(self, id, title, author):
        super().__init__(id, title)
        self.__author = author  # Private attribute

    def display_info(self):
        return f"Book ID: {self.id}, Title: {self.title}, Author: {self.__author}"

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, new_author):
        print(f"Author updated from {self.__author} to {new_author}")
        self.__author = new_author


# Subclass Magazine
class Magazine(LibraryItem):
    def __init__(self, id, title, issue_number):
        super().__init__(id, title)
        self.__issue_number = issue_number  # Private attribute

    def display_info(self):
        return f"Magazine ID: {self.id}, Title: {self.title}, Issue: {self.__issue_number}"


# Class Library
class Library:
    def __init__(self):
        self.__items = []  # Private attribute to store library items

    def add_item(self, item):
        self.__items.append(item)
        print(f"Item '{item.title}' berhasil ditambahkan ke perpustakaan.")

    def display_items(self):
        if not self.__items:
            print("Perpustakaan kosong.")
        else:
            print("Daftar Item di Perpustakaan:")
            for item in self.__items:
                print(item.display_info())

    def search_by_title(self, title):
        results = [item for item in self.__items if title.lower() in item.title.lower()]
        if results:
            print(f"Hasil pencarian untuk '{title}':")
            for item in results:
                print(item.display_info())
        else:
            print(f"Tidak ditemukan item dengan judul '{title}'.")

    def search_by_id(self, id):
        results = [item for item in self.__items if item.id == id]
        if results:
            print(f"Hasil pencarian untuk ID '{id}':")
            for item in results:
                print(item.display_info())
        else:
            print(f"Tidak ditemukan item dengan ID '{id}'.")


# Main Program
if __name__ == "__main__":
    # Membuat instance Library
    library = Library()

    # Menambahkan beberapa item ke perpustakaan
    book1 = Book(id="B001", title="Python Programming", author="John Doe")
    book2 = Book(id="B002", title="Data Science with Python", author="Jane Smith")
    magazine1 = Magazine(id="M001", title="Tech Monthly", issue_number=15)
    magazine2 = Magazine(id="M002", title="Science Weekly", issue_number=42)

    library.add_item(book1)
    library.add_item(book2)
    library.add_item(magazine1)
    library.add_item(magazine2)

    # Menampilkan semua item di perpustakaan
    print("\nMenampilkan semua item di perpustakaan:")
    library.display_items()

    # Mencari item berdasarkan judul
    print("\nMencari item berdasarkan judul 'Python':")
    library.search_by_title("Python")

    # Mencari item berdasarkan ID
    print("\nMencari item berdasarkan ID 'M001':")
    library.search_by_id("M001")

    # Mengubah author sebuah buku
    print("\nMengubah author buku 'Python Programming':")
    book1.author = "John Updated"
    print(book1.display_info())