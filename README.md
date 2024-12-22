# qa_python
Список тестов:
1. test_add_new_book_no_name_list_is_empty - тест проверяет, что при попытке добавления книги без названия список книг остаётся пустым
2. test_add_new_book_add_book_in_list - тест проверяет, что при использовании метода add_new_book в список добавляется книга
3. test_set_book_genre_in_list_correct - тест проверяет, что добавление существующего жанра книги происходит корректно
4. test_get_book_genre_not_in_list_not_add - тест проверяет, что функция get_book_genre не выводит жанр книги, если его нет в списке жанров
5. test_get_books_with_specific_genre_get_right_book - тест проверяет, что функция get_books_with_specific_genre выводит по заданному жанру верную книгу
6. test_get_books_genre_check_list - тест проверяет правильность вывода текущего слловаря books_genre
7. test_get_books_not_for_children_not_in_list - тест проверяет, что при попытке добавления в список книг для детей книги с запрещённым жанром список остаётся пустым
8. test_add_book_in_favorites_not_in_list - тест проверят, что список избранных книг остаётся пустым, если взята книга не из списка книг
9. test_delete_book_from_favorites_delete_one_book_list_not_empty - тест проверяет, что функция delete_book_from_favorite удаляет только одну книгу из списка, а не все сразу
10. test_get_list_of_favorites_books_check_list - тест проверяется правильность вывода текущего списка избранных книг