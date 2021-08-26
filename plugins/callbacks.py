elif query.data == "about":
            await query.answer()
            keyboard = InlineKeyboardMarkup(
                   [
               [
                   InlineKeyboardButton('Update Channel', url='https://t.me/subin_works'),
                   InlineKeyboardButton('Source Code', url='https://github.com/subinps/Media-Search-bot')
               ]
            ]
        )
        await query.message.edit_(
             Script.HELP_MSG,
             reply_markup=keyboard,
             disable_web_page_preview=True
       )
