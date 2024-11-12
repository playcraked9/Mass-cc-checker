import requests
import telebot,time
import time
from telebot import types
from gatet import Tele
import os
token = '8166823874:AAHC5qODSsODOwRYNiAdNPj52l7pKcnG5rQ' #bottoken
bot=telebot.TeleBot(token,parse_mode="HTML")
subscriber = '6191863486'
allowed_users = ['1790665950']  #Your ID
@bot.message_handler(commands=["start"])
def start(message):
    if str(message.chat.id) not in allowed_users:
        bot.reply_to(message, "🚫 𝐘𝐨𝐮 𝐜𝐚𝐧𝐧𝐨𝐭 𝐮𝐬𝐞 𝐭𝐡𝐞 𝐛𝐨𝐭 𝐭𝐨 𝐜𝐨𝐧𝐭𝐚𝐜𝐭 𝐝𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫𝐬 𝐭𝐨 𝐩𝐮𝐫𝐜𝐡𝐚𝐬𝐞 𝐚 𝐛𝐨𝐭 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 @Ownerxxxxx")
        return
    bot.reply_to(message, "𝐒𝐞𝐧𝐝 𝐭𝐡𝐞 𝐭𝐱𝐭 𝐟𝐢𝐥𝐞 𝐧𝐨𝐰")
@bot.message_handler(commands=["add"])
def add_user(message):
    if str(message.chat.id) == '6191863486':  # Only bot owner can add new users
        try:
            new_user_id = message.text.split()[1]  # Extract new user ID from the command
            allowed_users.append(new_user_id)
            bot.reply_to(message, f"User ID {new_user_id} Has Been Added Successfully.✅\nCongratulations! Premium New User🎉✅ ")
        except IndexError:
            bot.reply_to(message, "Please provide a valid user ID. Example: /add 123456789")
    else:
        bot.reply_to(message, "You do not have permission to add users.🚫")
@bot.message_handler(commands=["delete"])
def delete_user(message):
    if str(message.chat.id) == subscriber:  # Only bot owner can delete users
        try:
            user_id_to_delete = message.text.split()[1]  # Extract user ID from the command
            if user_id_to_delete in allowed_users:
                allowed_users.remove(user_id_to_delete)
                bot.reply_to(message, f"User ID {user_id_to_delete} has been removed successfully.✅")
            else:
                bot.reply_to(message, "User ID not found in the list.🚫")
        except IndexError:
            bot.reply_to(message, "Please provide a valid user ID. Example: /delete 123456789")
    else:
        bot.reply_to(message, "You do not have permission to delete users.🚫")
import random
import string

# List to store generated redeem codes
valid_redeem_codes = []

# Function to generate a random redeem code in the format XXXX-XXXX-XXXX
def generate_redeem_code():
    code = '-'.join(''.join(random.choices(string.ascii_uppercase + string.digits, k=4)) for _ in range(3))
    return code

# /code command handler to generate a new redeem code with a designed output
@bot.message_handler(commands=["code"])
def generate_code(message):
    if str(message.chat.id) == '6191863486':  # Only the bot owner can generate codes
        new_code = generate_redeem_code()  # Generate a new code
        valid_redeem_codes.append(new_code)  # Store the generated code
        # Send the redeem code in a designed format
        bot.reply_to(
            message, 
            f"<b>🎉 New Redeem Code 🎉</b>\n\n"
            f"<code>{new_code}</code>\n\n"
            f"Use this code to redeem your access!", 
            parse_mode="HTML"
        )
    else:
        bot.reply_to(message, "You do not have permission to generate redeem codes.🚫")

# /redeem command handler (as explained earlier)
@bot.message_handler(commands=["redeem"])
def redeem_code(message):
    try:
        redeem_code = message.text.split()[1]  # Extract redeem code from message
    except IndexError:
        bot.reply_to(message, "Please provide a valid redeem code. Example: /redeem XXXX-XXXX-XXXX")
        return

    if redeem_code in valid_redeem_codes:
        if str(message.chat.id) not in allowed_users:
            allowed_users.append(str(message.chat.id))  # Add user to allowed list
            valid_redeem_codes.remove(redeem_code)  # Remove used code
            bot.reply_to(message, f"Redeem code {redeem_code} has been successfully redeemed.✅ You now have access to the bot.")
        else:
            bot.reply_to(message, "You already have access to the bot.")
    else:
        bot.reply_to(message, "Invalid redeem code. Please check and try again.")

@bot.message_handler(content_types=["document"])
def main(message):
	if str(message.chat.id) not in allowed_users:
		bot.reply_to(message, "🚫 𝐘𝐨𝐮 𝐜𝐚𝐧𝐧𝐨𝐭 𝐮𝐬𝐞 𝐭𝐡𝐞 𝐛𝐨𝐭 𝐭𝐨 𝐜𝐨𝐧𝐭𝐚𝐜𝐭 𝐝𝐞𝐯𝐞𝐥𝐨𝐩𝐞𝐫𝐬 𝐭𝐨 𝐩𝐮𝐫𝐜𝐡𝐚𝐬𝐞 𝐚 𝐛𝐨𝐭 𝐬𝐮𝐛𝐬𝐜𝐫𝐢𝐩𝐭𝐢𝐨𝐧 @Ownerxxxxx")
		return
	dd = 0
	live = 0
	incorrect = 0
	ch = 0
	ko = (bot.reply_to(message, "𝐏𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 𝐂𝐚𝐫𝐝 𝐂𝐡𝐞𝐜𝐤𝐢𝐧𝐠 ...⌛").message_id)
	ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
	with open("combo.txt", "wb") as w:
		w.write(ee)
	try:
		with open("combo.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
			for cc in lino:
				current_dir = os.getcwd()
				for filename in os.listdir(current_dir):
					if filename.endswith(".stop"):
						bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @Ownerxxxxx')
						os.remove('stop.stop')
						return
				try: data = requests.get('https://bins.antipublic.cc/bins/'+cc[:6]).json()
				except: pass
				try:
					brand = data['brand']
				except:
					brand = 'Unknown'
				try:
					card_type = data['type']
				except:
					card_type = 'Unknown'
				try:
					country = data['country_name']
					country_flag = data['country_flag']
				except:
					country = 'Unknown'
					country_flag = 'Unknown'
				try:
					bank = data['bank']
				except:
					bank = 'Unknown'
				
				start_time = time.time()
				try:
					last = str(Tele(cc))
				except Exception as e:
					print(e)
					last = "Error"
				if 'Your card could not be set up for future usage.' in last:
					last='Your card could not be set up for future usage.'
				if 'Your card was declined.' in last:
				    last='Your card was declined.'
				if 'success' in last:
					last='APPROVED ✅'
				if 'Card Expired' in last:
						last='Your Card Expired'
				if 'Live' in last:
					    last='APPROVED ✅'
				if 'Unable to authenticate' in last:
				    last='Declined - Call Issuer'
				elif 'Proxy error' in last:
					last='Proxy error '
				mes = types.InlineKeyboardMarkup(row_width=1)
				cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
				status = types.InlineKeyboardButton(f"• 𝐒𝐓𝐀𝐓𝐔𝐒  : {last} ", callback_data='u8')
				cm3 = types.InlineKeyboardButton(f"• 𝐀𝐏𝐏𝐑𝐎𝐕𝐄𝐃 ✅ : [ {live} ] •", callback_data='x')
				cm4 = types.InlineKeyboardButton(f"• 𝐅𝐀𝐊𝐄 𝐂𝐀𝐑𝐃 ⚠️ : [ {incorrect} ] •", callback_data='x')
				cm5 = types.InlineKeyboardButton(f"• 𝐃𝐄𝐂𝐋𝐈𝐍𝐄𝐃 ❌ : [ {dd} ] •", callback_data='x')
				cm6 = types.InlineKeyboardButton(f"• 𝐓𝐎𝐓𝐀𝐋 🎉       :  [ {total} ] •", callback_data='x')
				stop=types.InlineKeyboardButton(f"[ 𝐒𝐓𝐎𝐏 🚫 ]", callback_data='stop')
				mes.add(cm1,status, cm3, cm4, cm5, cm6, stop)
				end_time = time.time()
				execution_time = end_time - start_time
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''𝐖𝐚𝐢𝐭 𝐟𝐨𝐫 𝐩𝐫𝐨𝐜𝐞𝐬𝐬𝐢𝐧𝐠 
𝐁𝐲 ➜ <a href='t.me/About_GSIX'>『ᝯׁhׁׅ֮ꪱׁׅtׁׅꪀׁׅᧁׁꫀׁׅܻ 』【𝐂𝐇】ᶜⁿꪜ 💤</a> ''', reply_markup=mes)
				msg = f'''
<a href='https://envs.sh/j9_.jpg'>-</a> 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
<a href='t.me/addlist/u2A-7na8YtdhZWVl'>┏━━━━━━━━━━━⍟</a>			
<a href='t.me/addlist/u2A-7na8YtdhZWVl'>┃</a>𝐂𝐂 <code>{cc}</code><a href='t.me/addlist/u2A-7na8YtdhZWVl'>┗━━━━━━━⊛</a>
<a href='t.me/addlist/u2A-7na8YtdhZWVl'>-</a> 𝐆𝐚𝐭𝐞𝐰𝐚𝐲: ⤿ 𝘚𝘛𝘙𝘐𝘗𝘌 𝘈𝘜𝘛𝘏 🟢 ⤾		
<a href='t.me/AboutGSIX'>-</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: ⤿ 𝘕𝘪𝘤𝘦! 𝘕𝘦𝘸 𝘱𝘢𝘺𝘮𝘦𝘯𝘵 𝘮𝘦𝘵𝘩𝘰𝘥 𝘢𝘥𝘥𝘦𝘥 ✅ ⤾

<a href='t.me/addlist/u2A-7na8YtdhZWVl'>-</a> 𝐈𝐧𝐟𝐨: <code>{cc[:6]}-{card_type} - {brand}</code>
<a href='t.me/addlist/u2A-7na8YtdhZWVl'>-</a> 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {country_flag}</code>
<a href='t.me/addlist/u2A-7na8YtdhZWVl'>-</a> 𝐁𝐚𝐧𝐤: <code>{bank}</code>

<a href='t.me/addlist/u2A-7na8YtdhZWVl'>-</a> 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝</code> 
<a href='t.me/addlist/u2A-7na8YtdhZWVl'>-</a> 𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/addlist/u2A-7na8YtdhZWVl'>⏤͟͞𝑮𝑺𝑰𝑿 𓆩 𝑪𝑯𝑲 𓆪ꪾᶜⁿꪜ</a>'''
				print(last)
				if 'success' in last or '𝗖𝗛𝗔𝗥𝗚𝗘𝗗💰' in last or 'APPROVED ✅' in last or 'APPROVED ✅' in last or "Your card's security code is invalid." in last:
					live += 1
					bot.reply_to(message, msg)
				elif 'Card Not Activated' in last:
					incorrect+=1
				elif '𝟯𝗗 𝗟𝗜𝗩𝗘 💰' in last:
					msg = f'''
<a href='https://envs.sh/j9_.jpg'>-</a> 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
<a href='t.me/addlist/u2A-7na8YtdhZWVl'>┏━━━━━━━━━━━⍟</a>			
<a href='t.me/addlist/u2A-7na8YtdhZWVl'>┃</a>𝐂𝐂 <code>{cc}</code><a href='t.me/addlist/u2A-7na8YtdhZWVl'>┗━━━━━━━⊛</a>
<a href='t.me/addlist/u2A-7na8YtdhZWVl'>-</a> 𝐆𝐚𝐭𝐞𝐰𝐚𝐲: ⤿ 𝘚𝘛𝘙𝘐𝘗𝘌 𝘈𝘜𝘛𝘏 🟢 ⤾		
<a href='t.me/addlist/u2A-7na8YtdhZWVl'>-</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: ⤿ 𝘕𝘪𝘤𝘦! 𝘕𝘦𝘸 𝘱𝘢𝘺𝘮𝘦𝘯𝘵 𝘮𝘦𝘵𝘩𝘰𝘥 𝘢𝘥𝘥𝘦𝘥 ✅ ⤾

<a href='t.me/addlist/u2A-7na8YtdhZWVl'>-</a> 𝐈𝐧𝐟𝐨: <code>{cc[:6]}-{card_type} - {brand}</code>
<a href='t.me/addlist/u2A-7na8YtdhZWVl'>-</a> 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {country_flag}</code>
<a href='t.me/addlist/u2A-7na8YtdhZWVl'>-</a> 𝐁𝐚𝐧𝐤: <code>{bank}</code>

<a href='t.me/addlist/u2A-7na8YtdhZWVl'>-</a> 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝</code> 
<a href='t.me/addlist/u2A-7na8YtdhZWVl'>-</a> 𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/addlist/u2A-7na8YtdhZWVl'>⏤͟͞𝑮𝑺𝑰𝑿 𓆩 𝑪𝑯𝑲 𓆪ꪾᶜⁿꪜ</a>'''
					live += 1
					bot.reply_to(message, msg)
				elif 'Card Not Activated' in last:
					incorrect+=1
				elif '𝗖𝗖𝗡/𝗖𝗩𝗩' in last or 'Your card has insufficient funds.' in last or 'tree_d' in last:
					msg = f'''
<a href='https://envs.sh/j9_.jpg'>-</a> 𝐀𝐩𝐩𝐫𝐨𝐯𝐞𝐝 ✅
<a href='t.me/addlist/u2A-7na8YtdhZWVl'>┏━━━━━━━━━━━⍟</a>			
<a href='t.me/addlist/u2A-7na8YtdhZWVl'>┃</a>𝐂𝐂 <code>{cc}</code><a href='t.me/addlist/u2A-7na8YtdhZWVl'>┗━━━━━━━⊛</a>
<a href='t.me/addlist/u2A-7na8YtdhZWVl'>-</a> 𝐆𝐚𝐭𝐞𝐰𝐚𝐲: ⤿ 𝘚𝘛𝘙𝘐𝘗𝘌 𝘈𝘜𝘛𝘏 🟢 ⤾		
<a href='t.me/addlist/u2A-7na8YtdhZWVl'>-</a> 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: ⤿ 𝘕𝘪𝘤𝘦! 𝘕𝘦𝘸 𝘱𝘢𝘺𝘮𝘦𝘯𝘵 𝘮𝘦𝘵𝘩𝘰𝘥 𝘢𝘥𝘥𝘦𝘥 ✅ ⤾

<a href='t.me/addlist/u2A-7na8YtdhZWVl'>-</a> 𝐈𝐧𝐟𝐨: <code>{cc[:6]}-{card_type} - {brand}</code>
<a href='t.me/addlist/u2A-7na8YtdhZWVl'>-</a> 𝐂𝐨𝐮𝐧𝐭𝐫𝐲: <code>{country} - {country_flag}</code>
<a href='t.me/addlist/u2A-7na8YtdhZWVl'>-</a> 𝐁𝐚𝐧𝐤: <code>{bank}</code>

<a href='t.me/addlist/u2A-7na8YtdhZWVl'>-</a> 𝐓𝐢𝐦𝐞: <code>{"{:.1f}".format(execution_time)} 𝐬𝐞𝐜𝐨𝐧𝐝</code> 
<a href='t.me/addlist/u2A-7na8YtdhZWVl'>-</a> 𝐁𝐨𝐭 𝐀𝐛𝐨𝐮𝐭: <a href='t.me/addlist/u2A-7na8YtdhZWVl'>⏤͟͞𝑮𝑺𝑰𝑿 𓆩 𝑪𝑯𝑲 𓆪ꪾᶜⁿꪜ</a>'''
					live += 1
					bot.reply_to(message, msg)
				elif 'Card Not Activated' in last:
					incorrect+=1
				else:
					dd += 1
					time.sleep(1)
	except Exception as e:
		print(e)
	bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @Ownerxxxxx')
# Mock of Tele function for demonstration

        
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	with open("stop.stop", "w") as file:
		pass
logop = f'''━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
'''
print(logop)
bot.polling()
