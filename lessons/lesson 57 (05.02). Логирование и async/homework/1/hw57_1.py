import logging
from datetime import datetime, timedelta
logger = logging.getLogger('registration_logger')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('registration_log.txt')
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
def register_user(username: str):
    try:
        if username.isalpha():
            logger.info(f'Пользователь{username} зарегистрирован')
        else:
            raise ValueError('Имя пользователя некорректно')
    except Exception as Error:
        logger.error(f'Ошибка:{Error}')

    next_date = datetime.now() + timedelta(days=7)
    return next_date


print("Дата повторной регистрации: ", register_user('Ivan').strftime('%Y-%m-%d'))