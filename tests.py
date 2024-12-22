import pytest

from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_no_name_list_is_empty(self):
        collector = BooksCollector()

        collector.add_new_book('')
        assert len(collector.get_books_genre()) == 0

    def test_add_new_book_add_book_in_list(self):
        collector = BooksCollector()

        collector.add_new_book('Над пропастью во ржи')
        assert len(collector.get_books_genre()) == 1


    @pytest.mark.parametrize(
        'name, genre',
        [
            ['Кладбище домашних животных', 'Ужасы'],
            ['Лето в Простоквашино', 'Мультфильмы'],
            ['Снежная королева', 'Мультфильмы'],
            ['Снежная королева', '']
        ]
    )
    def test_set_book_genre_in_list_correct(self, name, genre):
        collector = BooksCollector()

        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre

    def test_get_book_genre_not_in_list_not_add(self):
        collector = BooksCollector()

        collector.add_new_book('Поющие в терновнике')
        collector.set_book_genre('Поющие в терновнике', 'Роман')
        assert len(collector.get_book_genre('Поющие в терновнике')) == 0

    @pytest.mark.parametrize(
        'book, genre',
        [
            ['Кладбище домашних животных', 'Ужасы'],
            ['Лето в Простоквашино', 'Мультфильмы'],
            ['Снежная королева', 'Мультфильмы']
        ]
    )
    def test_get_books_with_specific_genre_get_right_book(self, book, genre):
        collector = BooksCollector()

        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        assert collector.get_books_with_specific_genre(genre)[0] == book

    @pytest.mark.parametrize(
        'book, genre',
        [
            ['Кладбище домашних животных', 'Ужасы'],
            ['Лето в Простоквашино', 'Мультфильмы'],
        ]
    )
    def test_get_books_genre_check_list(self, book, genre):
        collector = BooksCollector()

        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        expected_list = {book: genre}
        assert collector.get_books_genre() == expected_list


    def test_get_books_not_for_children_not_in_list(self):
        collector = BooksCollector()

        collector.add_new_book('Клуб убийств по четвергам')
        collector.set_book_genre('Клуб убийств по четвергам', 'Детективы')

        assert len(collector.get_books_for_children()) == 0

    def test_add_book_in_favorites_not_in_list(self):
        collector = BooksCollector()

        collector.add_book_in_favorites('Кладбище домашних животных')
        assert len(collector.get_list_of_favorites_books()) == 0

    def test_delete_book_from_favorites_delete_one_book_list_not_empty(self):
        collector = BooksCollector()

        collector.add_new_book('Поющие в терновнике')
        collector.add_new_book('Унесенные ветром')

        collector.add_book_in_favorites('Поющие в терновнике')
        collector.add_book_in_favorites('Унесенные ветром')

        collector.delete_book_from_favorites('Унесенные ветром')
        assert len(collector.get_list_of_favorites_books()) != 0

    def test_get_list_of_favorites_books_check_list(self):
        collector = BooksCollector()

        collector.add_new_book('Черный обелиск')
        collector.add_book_in_favorites('Черный обелиск')

        assert collector.get_list_of_favorites_books()[0] == 'Черный обелиск'
