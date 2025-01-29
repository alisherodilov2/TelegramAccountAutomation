from telethon import TelegramClient, events

api_id = "TELEGRAM_API_ID"
api_hash = "TELEGRAM_API_HASH"

client = TelegramClient("session_name", api_id, api_hash)

@client.on(events.NewMessage)
async def auto_reply(event):
    sender = await event.get_sender()
    message = event.message.text

    if sender and not sender.bot:  # Ignore bots
        await event.reply(f"Hello {sender.first_name}, I received your message: {message}")


async def send_message_to_contacts():
    contacts = ["@Islombek_Ravshanov", "@Ahmedov_0304"]  # Replace with real usernames or phone numbers
    for contact in contacts:
        await client.send_message(contact, "Hello! This is an automated message.")


with client:
    client.loop.run_until_complete(send_message_to_contacts())


client.start()
client.run_until_disconnected()
