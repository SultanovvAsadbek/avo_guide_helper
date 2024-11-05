from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

import app.keybords as kb
from app.fsm_conditions import Reg

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.reply(
        f"Добро Пожаловать {message.from_user.full_name} !",
        reply_markup=kb.main,
    )


@router.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    await callback.answer('Выбрали пункт Каталог')
    await callback.message.answer('Каталог', reply_markup=await kb.inline_cars())


@router.message(Command('reg'))
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Reg.number1)
    await message.answer('Введите цифру')

@router.message(Reg.number1)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(number1=message.text)
    await state.set_state(Reg.number2)
    await message.answer('Введите цифру')

@router.message(Reg.number2)
async def two_three(message: Message, state: FSMContext):
    await state.update_data(number2=message.text)
    data = await state.get_data()
    await message.answer(f"{data['number1']} + {data['number2']} = {int(data['number1']) + int(data['number2'])}")
    await state.clear()


