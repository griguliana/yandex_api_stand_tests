import data
import sender_stand_request

kit_body_511 = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
kit_body_512 = "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"


# Тест 1. Допустимое количество символов (1)
def test_kit_creation_with_single_character_name_succeeds():
    assert_positive_response("a")


# Тест 2. Допустимое количество символов (511)
def test_kit_creation_with_maximum_allowed_characters_succeeds():
    assert_positive_response(kit_body_511)


# Тест 3. Количество символов меньше допустимого (0)
def test_kit_creation_with_empty_name_fails():
    assert_negative_response_with_name("")

# Тест 4. Допустимое количество символов (512)
def test_kit_creation_with_exceeding_maximum_characters_fails():
    assert_negative_response_with_name(kit_body_512)


# Тест 5. Разрешены английские буквы
def test_kit_creation_with_english_letters_in_name_succeeds():
    assert_positive_response("QWErty")


# Тест 6. Разрешены русские буквы
def test_kit_creation_with_russian_letters_in_name_succeeds():
    assert_positive_response("Мария")


# Тест 7. Разрешены спецсимволы
def test_kit_creation_with_special_symbols_in_name_succeeds():
    assert_positive_response("\"№%@\",")


# Тест 8. Разрешены пробелы
def test_kit_creation_with_spaces_in_name_succeeds():
    assert_positive_response("Человек и КО")


# Тест 9. Разрешены цифры
def test_kit_creation_with_numbers_in_name_succeeds():
    assert_positive_response("123")


# Тест 10. Параметр не передан в запросе
def test_kit_creation_with_no_name_fails():
    current_kit_body_without_name = data.kit_body.copy()
    current_kit_body_without_name.pop("name")
    assert_negative_response_without_name(current_kit_body_without_name)


# Тест 11. Передан другой тип параметра (число)
def test_kit_creation_with_numeric_type_name_fails():
    assert_negative_response_with_name(123)


def assert_positive_response(name):
    kit_body_with_name = get_updated_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit_with_authorization(kit_body_with_name)
    assert kit_response.json()["name"] == name
    assert kit_response.status_code == 201


def assert_negative_response_with_name(name):
    kit_body_with_name = get_updated_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit_with_authorization(kit_body_with_name)
    assert kit_response.status_code == 400


def assert_negative_response_without_name(kit_body):
    kit_response = sender_stand_request.post_new_client_kit_with_authorization(kit_body)
    assert kit_response.status_code == 400


def get_updated_kit_body(name):
    updated_kit_body = data.kit_body.copy()
    updated_kit_body["name"] = name
    return updated_kit_body
