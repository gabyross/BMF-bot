import telepot
token = '1243199877:AAE11yhQrE0CGjhY7AmjW_ikWQxr9a67ZBc'
TelegramBot = telepot.Bot(token)
print(TelegramBot.getMe())

print(TelegramBot.getUpdates())