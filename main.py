import pywhatkit
import json

with open('phones.json', encoding='utf-8') as file:
    list_of_number = json.load(file)
# list_of_number = [
#     '+996778010039',
#     '+996776760076',
#     '+996553929894'
# ]
# for k, v in list_of_number.items():
#     print(k,v)
def send_message_inst():
    message = """
😱НЕ ЗНАЕШЬ КАК ПРОВЕСТИ ЛЕТО ?🤔
💻ПРОГРАММИРОВАНИЕ + АНГЛИЙСКИЙ всего 5000с за месяц📚

Выбор направлений :
💻BACK END - 3 месяца 
💻FRONT END - 3 месяца
💻Ui UX DESIGN - 3 месяца

🔋Обучение проходит 3 месяца 6 дней интенсивно 
💻3 дня - программирование(вт,чт,сб)
📚3 дня - английский (пн,ср,пт)
по 4 часа в день 👌🏻
🧑🏻‍💻 максимум практики 99% 
🧑🏻‍💻 преподаватели (действующие программисты)
🧑🏻‍💻 комфортные условия 
🧑🏻‍💻 предоставляем компьютер
🧑🏻‍💻 удобный график 
🧑🏻‍💻 СЕРТИФИКАТ по окончанию 
🧑🏻‍💻 лучшим студентам поможем ТРУДОУСТРОИТЬСЯ 
🧑🏻‍💻 возможность далее обучаться зарубежом 🇺🇸🇲🇾🇨🇳🇮🇹🇦🇪

❗️Всего по 12 мест ❗️

❕Регистрация проходит у нас в Академии IT PARK
Адрес: г.Ош, ул. Ленина 318 (IT PARK)
Ориентир: старая мэрия, 3 этаж    
"""
    for k,v in list_of_number.items():
        phone = f"{v['phone']}"
        pywhatkit.sendwhatmsg_instantly(phone_no=phone,message=message, tab_close=True)
        if k ==1600:
            break
    
    # for i in list_of_number:
    #     pywhatkit.sendwhatmsg_instantly(phone_no=i,message=message, tab_close=False)
    
def main():
    send_message_inst()
    # pywhatkit.sendwhatmsg_instantly(phone_no="+996778010039",message="message", tab_close=False)
    
if __name__ == '__main__':
    main()