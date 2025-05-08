from book import Book
from manager import Manager
# from electronic_library.user.user import user


def main():

    b = Book("simba", "Reza Nadian", "dram")
    m = Manager("simba", "Reza Nadian", "dram")
    print(f"title:{b.title} {m.title}")
    import sys
    print(sys.path)


if __name__ == "__main__":
    main()