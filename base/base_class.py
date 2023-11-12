from datetime import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver

    # Method Get current url
    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current url ' + get_url)

    # Method assert word
    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print(f'Word {value_word} = {result}!')

    # Method screenshot word
    def get_screenshot(self):
        now_time = datetime.utcnow().strftime('%H.%M.%S.%d.%m.%Y.')
        name_screenshot = 'screenshot_' + now_time + '.png'
        self.driver.save_screenshot('S:\\Projects_1\\main_project\\screenshots\\' + name_screenshot)

    # Method screenshot word
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print(f'{get_url} url is equal to {result}')
