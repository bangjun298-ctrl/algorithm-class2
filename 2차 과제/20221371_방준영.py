class Book:
    def __init__(self, book_id, title, author, year):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"책 번호: {self.book_id}, 제목: {self.title}, 저자: {self.author}, 출판연도: {self.year}"


class Node:  # 단순 연결 리스트 노드 클래스
    def __init__(self, elem, next=None):
        self.data = elem
        self.link = next

    def append(self, new):
        if new is not None:
            new.link = self.link
            self.link = new

    def popNext(self):
        deleted_node = self.link
        if deleted_node is not None:
            self.link = deleted_node.link
        return deleted_node


class LinkedList:  # 단순 연결 리스트
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def insert(self, elem):
        new_node = Node(elem)
        if self.isEmpty():
            self.head = new_node
        else:
            cur = self.head
            while cur.link is not None:
                cur = cur.link
            cur.link = new_node

    def find_by_title(self, title):
        cur = self.head
        while cur is not None:
            if cur.data.title == title:
                return cur.data
            cur = cur.link
        return None

    def find_pos_by_title(self, title):
        cur = self.head
        prev = None
        while cur is not None:
            if cur.data.title == title:
                return prev, cur
            prev = cur
            cur = cur.link
        return None, None

    def print_list(self):
        if self.isEmpty():
            print("현재 등록된 도서가 없습니다.")
            return
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.link


class BookManagement:
    def __init__(self):
        self.book_list = LinkedList()

    def add_book(self, book_id, title, author, year):
        if self.is_duplicate_id(book_id):
            print("이미 존재하는 책 번호입니다.")
            return
        book = Book(book_id, title, author, year)
        self.book_list.insert(book)
        print("도서 추가 완료")

    def is_duplicate_id(self, book_id):
        cur = self.book_list.head
        while cur is not None:
            if cur.data.book_id == book_id:
                return True
            cur = cur.link
        return False

    def remove_book(self, title):
        prev, target = self.book_list.find_pos_by_title(title)
        if target is None:
            print("해당 제목의 도서가 존재하지 않습니다.")
            return

        if prev is None:
            self.book_list.head = target.link
        else:
            prev.link = target.link

        print("도서 삭제 완료!")

    def search_book(self, title):
        result = self.book_list.find_by_title(title)
        if result is None:
            print("해당 제목의 도서가 없습니다.")
        else:
            print("조회 도서 정보:")
            print(result)

    def display_books(self):
        self.book_list.print_list()

    def run(self):
        while True:
            print("\n===== 도서 관리 프로그램 =====")
            print("1. 도서 추가")
            print("2. 도서 삭제 (책 제목으로 삭제)")
            print("3. 도서 조회 (책 제목으로 조회)")
            print("4. 전체 도서 목록 출력")
            print("5. 프로그램 종료")
            choice = input("메뉴 선택: ")

            if choice == '1':
                book_id = input("책 번호 입력: ")
                title = input("제목 입력: ")
                author = input("저자 입력: ")
                year = input("출판 연도 입력: ")
                self.add_book(book_id, title, author, year)

            elif choice == '2':
                title = input("삭제할 책 제목 입력: ")
                self.remove_book(title)

            elif choice == '3':
                title = input("조회할 책 제목 입력: ")
                self.search_book(title)

            elif choice == '4':
                self.display_books()

            elif choice == '5':
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다. 다시 선택해주세요.")

if __name__ == "__main__":
    bm = BookManagement()
    bm.run()