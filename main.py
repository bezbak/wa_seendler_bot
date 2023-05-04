import pywhatkit
import json

with open('phones.json', encoding='utf-8') as file:
    list_of_number = json.load(file)
# list_of_number = [
#     '+996778010039',
#     '+996998767651',
#     '+996553929894'
# # ]
# for k, v in list_of_number.items():
#     print(k,v)
def send_message_inst():
    message = """Привет от Казахстана"""
    for k,v in list_of_number.items():
        phone = f"{v['phone']}"
        pywhatkit.sendwhatmsg_instantly(phone_no=phone,message=message, tab_close=True)
        if k ==1600:
            break
    
    # for i in list_of_number:
    #     pywhatkit.sendwhatmsg_instantly(phone_no=i,message=message, tab_close=True)
    #     print()
    
# def main():
#     send_message_inst()
    
# if __name__ == '__main__':
#     main()