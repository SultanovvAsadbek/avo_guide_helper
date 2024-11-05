from aiogram.fsm.state import StatesGroup, State


class Reg(StatesGroup):
    number1 = State()
    number2 = State()

