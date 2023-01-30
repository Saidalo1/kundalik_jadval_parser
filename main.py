import logging
# import time

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

from config import TOKEN, week_day

from models import session, Schedule, ErrorSchedule

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    message_text = f"{message.from_user.first_name}, xush kelibsiz! \n Dars jadvalini bilish uchun /dars_jadvali " \
                   f"komandasiga murojaat qiling"
    return await message.answer(message_text)


@dp.message_handler(commands=['dars_jadvali'])
async def main(message: types.Message):
    # start_time = time.time()
    schedule_elements_query = session.query(Schedule).filter(Schedule.weekday == week_day)
    schedule_list = [subject.name for subject in schedule_elements_query]
    message_text = ""
    if len(schedule_list) > 0:
        for subject in schedule_list:
            message_text += f'\n{subject}'
    else:
        errors = session.query(ErrorSchedule).filter(ErrorSchedule.weekday == week_day)
        errors_list = [error.error_text for error in errors]
        if len(errors_list) > 0:
            for error in errors_list:
                message_text += f'\n{error}'
        else:
            message_text += 'Dars jadvali topilmadi'
    # print("--- %s seconds ---" % (time.time() - start_time))
    return await message.answer(message_text)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
