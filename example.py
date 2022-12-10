from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

STATE = None
TASTE_OF_CAKE = 1
TYPE_OF_CAKE = 2
DECOR_OF_CAKE = 3
WEIGHT_OF_CAKE = 4
DATE_OF_ORDER = 5
COST_OF_ORDER = 6


# function to handle the /start command
def start(update, context):
    first_name = update.message.chat.first_name
    chat = update.effective_chat
    update.message.reply_text(f"Здравствуйте, {first_name}, мы рады, что вы хотите заказать у нас тортик!")

    start_getting_order(update, context)


def start_getting_order(update, context):
    global STATE
    STATE = TASTE_OF_CAKE
    update.message.reply_text(
        f"Какой вкус торта, вы хотите заказать? \n "
        f"Выберите из: морковный/ванильный/шоколадный")


def received_taste_of_cake(update, context):
    global STATE

    try:
        taste = str(update.message.text).lower()

        if taste != 'морковный' and taste != 'ванильный' and taste != 'шоколадный':
            raise ValueError("invalid value")
        else:
            context.user_data['taste_of_cake'] = taste
            update.message.reply_text(
                f"Какой тип торта вы хотите заказать? \n "
                f"(выберите из: бенто/по весу)")
            STATE = TYPE_OF_CAKE
    except:
        update.message.reply_text(
            "Выберите вкус из предложенных: морковный/ванильный/шоколадный")


def received_type_of_cake(update, context):
    global STATE

    try:
        weight = update.message.text.lower()

        if weight != 'по весу' and weight != 'бенто':
            raise ValueError("invalid value")
        if weight == 'по весу':

            update.message.reply_text(
                f"Какой вес торта, вы хотите заказать? \n "
                f"(вес от 1 кг)")
            STATE = WEIGHT_OF_CAKE
        else:
            context.user_data['weight_of_cake'] = 'бенто'
            update.message.reply_text(f"Круто! Теперь выберите декор для торта? \n "
                                      f"(Выберите из: с ягодами/с цветами/с надписью)")
            STATE = DECOR_OF_CAKE
    except:
        update.message.reply_text(
            "Выберите тип торта из предложенных: бенто/по весу")


def received_weight_of_cake(update, context):
    global STATE

    try:
        weight = float(update.message.text)

        if weight < 1:
            raise ValueError("invalid value")
        context.user_data['weight_of_cake'] = weight
        update.message.reply_text(f"Круто! Теперь выберите декор для торта?\n  "
                                  f"(Выберите из: с ягодами/с цветами/с надписью) ")
        STATE = DECOR_OF_CAKE
    except:
        update.message.reply_text(
            "Вес от 1 кг")


def received_decor_of_cake(update, context):
    global STATE

    try:
        decor = update.message.text.lower()

        if decor != 'с ягодами' and decor != 'с цветами' and decor != 'с надписью':
            raise ValueError("invalid value")
        context.user_data['decor_of_cake'] = decor
        update.message.reply_text(f"Классс! Теперь скажите дату вашего заказа.\n "
                                  f"Напишите в формате - день-месяц (Пример 11-ноября)")
        STATE = DATE_OF_ORDER
    except :
        update.message.reply_text(
            "Ой, такого декора нет. Выберите из предложенных: с ягодами/с цветами/с надписью.")


def received_date_of_order(update, context):
    global STATE
    try:
        date = update.message.text
        context.user_data['date_of_order'] = date
        update.message.reply_text(f"Хотите узнать стоимость вашего заказа? (Да/Нет)")
        STATE = COST_OF_ORDER
    except :
        update.message.reply_text(
            "Ой, что-то не то с датой!")


def calculate_cost_of_сake(update, context):
    global STATE
    try:
        answer = update.message.text.lower()
        if answer == 'да':
            weight = context.user_data['weight_of_cake']
            decor = context.user_data['decor_of_cake']
            taste = context.user_data['taste_of_cake']

            if weight == 'бенто':
                if decor == 'с ягодами':
                    cost = 1300 + 400
                elif decor == 'с цветами':
                    cost = 1300 + 200
                elif decor == 'с надписью':
                    cost = 1300
            else:
                if decor == 'с ягодами':
                    cost = (1800 * weight) + 400
                elif decor == 'с цветами':
                    cost = (1800 * weight) + 200
                elif decor == 'с надписью':
                    cost = (1800 * weight)
            if weight == 'бенто' :
                update.message.reply_text(f"Ваш заказ:\n"
                                          f"Вкус - {taste}\n"
                                          f"Тип торта - {weight}\n"
                                          f"Декор - {decor}\n"
                                          f"Стоимость вашего заказа - {cost}")
            else :
                update.message.reply_text(f"Ваш заказ:\n"
                                          f"Вкус - {taste}\n"
                                          f"Вес торта - {weight} кг\n"
                                          f"Декор - {decor}\n"
                                          f"Стоимость вашего заказа - {cost}")
        else:
            raise ValueError("invalid value")
        STATE = None
    except:
        update.message.reply_text(
            "Ой, ну и ладно")


# function to handle the /help command
def help(update, context):
    update.message.reply_text('help command received')


# function to handle errors occured in the dispatcher
def error(update, context):
    update.message.reply_text('an error occured')


# function to handle normal text
def text(update, context):
    global STATE

    if STATE == TASTE_OF_CAKE:
        return received_taste_of_cake(update, context)

    if STATE == TYPE_OF_CAKE:
        return received_type_of_cake(update, context)

    if STATE == WEIGHT_OF_CAKE:
        return received_weight_of_cake(update, context)

    if STATE == DECOR_OF_CAKE:
        return received_decor_of_cake(update, context)

    if STATE == DATE_OF_ORDER:
        return received_date_of_order(update, context)

    if STATE == COST_OF_ORDER:
        return calculate_cost_of_сake(update, context)


def main():
    TOKEN = "5630280874:AAHj0jFVeJCWq4xtjL58tpgQKETNAHgs_eU"

    # create the updater, that will automatically create also a dispatcher and a queue to
    # make them dialoge
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # add handlers for start and help commands
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help))
    # add an handler for our biorhythm command

    # add an handler for normal text (not commands)
    dispatcher.add_handler(MessageHandler(Filters.text, text))

    # add an handler for errors
    dispatcher.add_error_handler(error)

    # start your shiny new bot
    updater.start_polling()

    # run the bot until Ctrl-C
    updater.idle()


if __name__ == '__main__':
    main()
