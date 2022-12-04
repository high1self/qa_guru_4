def func_name(func, *args):
    function_name = func.__name__
    array = function_name.split("_")

    for word in range(0, len(array)):
        array[word] = array[word].capitalize()

    nice_name = " ".join(array)
    print("Имя функции:", nice_name, "|", "Аргументы:", *args)


def open_browser(browser_name):
    func_name(open_browser, browser_name)


def go_to_companyname_homepage(page_url):
    func_name(go_to_companyname_homepage, page_url)


def find_registration_button_on_login_page(page_url, button_text):
    func_name(find_registration_button_on_login_page, page_url, button_text)


open_browser(browser_name="Chrome")
go_to_companyname_homepage(page_url="ya.ru")
find_registration_button_on_login_page(page_url="ya.ru", button_text="registration")

