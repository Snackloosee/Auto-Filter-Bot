from pyrogram import Client, filters, enums
from info import INDEX_CHANNELS, INDEX_EXTENSIONS
from database.ia_filterdb import save_file

media_filter = filters.document | filters.video | filters.audio


@Client.on_message(filters.chat(INDEX_CHANNELS) & media_filter)
async def media(bot, message):
   for file_type in ("document", "video", "audio"):
    media = getattr(message, message.media.value, file_type, None)
       if media is not None:
           break
    else:
        return
        media.file_type = file_type
        media.caption = message.caption
        await save_file(media)
    
       # if (str(media.file_name).lower()).endswith(tuple(INDEX_EXTENSIONS)):

#from pyrogram import Client, filters, enums
#from info import INDEX_CHANNELS, INDEX_EXTENSIONS
#from database.ia_filterdb import save_file

#media_filter = filters.document | filters.video | filters.audio


#@Client.on_message(filters.chat(INDEX_CHANNELS) & media_filter)
#async def media(bot, message):
#    """Media Handler"""
#    media = getattr(message, message.media.value, None)
#    if (str(media.file_name).lower()).endswith(tuple(INDEX_EXTENSIONS)):
#        media.caption = message.caption
#        await save_file(media)
