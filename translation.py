class Translation(object):
    START_TEXT = """Siz /help buyrug'i yordamida mendan qanday foydalanishni bilib olishingiz mumkin 

Siz /upgrade buyrug'i yordamida yuqori funktsiyalarga ega bo'lishingiz mumkin 

By: @All_Url_DownloaderBot ."""
    RENAME_403_ERR = "Kechirasiz. Faylni nomlash uchun sizda etarli ruxsat yo'q"
    ABS_TEXT = " Iltimos, xudbinlik qilmang"
    UPGRADE_TEXT = "@All_Url_DownloaderBot <a href='https://t.me/SalomovAsliddin'> To'lovlar </a> \nTo'lovni to'lagandan so'ng, siz to'lovning skrinshotini @SalomovAsliddin_2oo4 yoki @SalomovAsliddinga yuborishingiz kerak."
    FORMAT_SELECTION = "Istagan formatingizni tanlang: <a href='{}'>fayl hajmi </a> \nAgar siz maxsus eskiz o'rnatmoqchi bo'lsangiz, quyidagi tugmalardan birini bosishdan oldin yoki keyin rasm yuboring."
    SET_CUSTOM_USERNAME_PASSWORD = """File formatini tanlang:
URL | filename | username | password"""
    NOYES_URL = "@All_Url_DownloaderBot URL manzili aniqlandi. Iltimos, xizmatni buzmang!"
    DOWNLOAD_START = "Server yuklanmoqda..."
    UPLOAD_START = "Telegram yuklanmoqda..."
    RCHD_BOT_API_LIMIT = "Ruxsat etilgan maksimal hajmdan kattaroq (50MB) Biroq, Biz uni o'rnatishga harakat qilyapmiz."
    RCHD_TG_API_LIMIT = "Serverga  {} sekunda yuklandi. \nFile hajmi: {}\nUzur. Ammo Telegramga max 1.5 GB fayl yuklash imkoni mavjud."
    AFTER_SUCCESSFUL_UPLOAD_MSG = "Iltimos, menga foydali deb baho bering. https://t.me/SalomovAsliddin "
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "Server yuklash {} sekundda. \nA'zo bo'ling : @SalomovAsliddin \nTelegramga yuklash {} sekund."
    NOT_AUTH_USER_TEXT = "Iltimos, /upgrade buyrug'i yordamida obunangizni yangilang."
    NOT_AUTH_USER_TEXT_FILE_SIZE = "Aniqlangan fayl hajmi: {}. Bepul foydalanuvchilar faqat yuklashi mumkin: {} \n Iltimos, /upgrade buyrug'i yordamida obunani yangilang. \n Botda xato topsangiz, bu erda men bilan bog'lanishingiz mumkin <a href='https://uzfilms.rf.gd'> @SalomovAsliddin </a>"
    SAVED_CUSTOM_THUMB_NAIL = "Custom video / file thumbnail saved. This image will be used in the video / file."
    DEL_ETED_CUSTOM_THUMB_NAIL = "✅  Maxsus eskiz muvaffaqiyatli o'chirildi."
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media  tozalandi"
    SAVED_RECVD_DOC_FILE = "Hujjat muvaffaqiyatli yuklandi."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_CUSTOM_THUMB_NAIL_FOUND = "Maxsus eskiz topilmadi."
    NO_VOID_FORMAT_FOUND = "ERROR...\n<b>Havola berkitilgan</b>: {}"
    USER_ADDED_TO_DB = "User <a href='tg://user?id={}'>{}</a> added to {} till {}."
    CURENT_PLAN_DETAILS = """Loyihamiz
--------
Telegram ID: <code>{}</code>
Loyiha nomi: Tezkor Bot
Expires on: 01/10/2021"""
    HELP_USER = """Salom sizga yordam berishga tayyormiz:
    
1. File/video url ni yuboring...
2. Tugmalardan foydalanib birini tanlang...
3. Tugmalar:
   SVideo - Give File as video with Screenshots
   DFile  - Give File with Screenshots
   Video  - Give File as video without Screenshots
   DFile  - Give File without Screenshots
   


--------
Send /me to know current plan details

Support Group : @SalomovAsliddin_2004
By: @SalomovAsliddin"""
    REPLY_TO_DOC_GET_LINK = "Reply to a Telegram media to get High Speed Direct Download Link"
    REPLY_TO_DOC_FOR_C2V = "Reply to a Telegram media to convert"
    REPLY_TO_DOC_FOR_SCSS = "Reply to a Telegram media to get screenshots"
    REPLY_TO_DOC_FOR_RENAME_FILE = "Reply to a Telegram media to /rename with custom thumbnail support"
    AFTER_GET_DL_LINK = "Direct Link <a href='{}'>Generated</a> valid for {} days.\n @All_Url_DownloaderBot"
    FF_MPEG_RO_BOT_RE_SURRECT_ED = """Syntax: /trim HH:MM:SS [HH:MM:SS]"""
    FF_MPEG_RO_BOT_STEP_TWO_TO_ONE = "First send /downloadmedia to any media so that it can be downloaded to my local. \nSend /storageinfo to know the media, that is currently downloaded."
    FF_MPEG_RO_BOT_STOR_AGE_INFO = "Video Duration: {}\nSend /clearffmpegmedia to delete this media, from my storage.\nSend /trim HH:MM:SS [HH:MM:SS] to cu[l]t a small photo / video, from the above media."
    FF_MPEG_RO_BOT_STOR_AGE_ALREADY_EXISTS = "A saved media already exists. Please send /storageinfo to know the current media details."
    USER_DELETED_FROM_DB = "User <a href='tg://user?id={}'>{}</a> deleted from DataBase."
    REPLY_TO_DOC_OR_LINK_FOR_RARX_SRT = "Reply to a Telegram media (MKV), to extract embedded streams"
    REPLY_TO_MEDIA_ALBUM_TO_GEN_THUMB = "Reply /generatecustomthumbnail to a media album, to generate custom thumbail"
    ERR_ONLY_TWO_MEDIA_IN_ALBUM = "Media Album should contain only two photos. Please re-send the media album, and then try again, or send only two photos in an album."
    INVALID_UPLOAD_BOT_URL_FORMAT = "URL format is incorrect. make sure your url starts with either http:// or https://. You can set custom file name using the format link | file_name.extension"
    ABUSIVE_USERS = "You are not allowed to use this bot. If you think this is a mistake, please check /me to remove this restriction."
    FF_MPEG_RO_BOT_AD_VER_TISE_MENT = "@SalomovAsliddin"
    EXTRACT_ZIP_INTRO_ONE = "Send a compressed file first, Then reply /unzip command to the file."
    EXTRACT_ZIP_INTRO_THREE = "Analyzing received file. ⚠️ This might take some time. Please be patient. "
    UNZIP_SUPPORTED_EXTENSIONS = ("zip", "rar")
    EXTRACT_ZIP_ERRS_OCCURED = "Sorry. Errors occurred while processing compressed file. Please check everything again twice, and if the issue persists, report this to <a href='https://telegram.dog/ThankTelegram'>@SpEcHlDe</a>"
    EXTRACT_ZIP_STEP_TWO = """Select file_name to upload from the below options.
You can use /rename command after receiving file to rename it with custom thumbnail support."""
    CANCEL_STR = "Process Cancelled"
    ZIP_UPLOADED_STR = "Server yuklangan  {}  file {} sekunt."
    FREE_USER_LIMIT_Q_SZE = """Cannot Process.
Free users only 1 request per 30 minutes.
/upgrade or Try 1800 seconds later."""
    SLOW_URL_DECED = "Gosh that seems to be a very slow URL. Since you were screwing my home, I am in no mood to download this file. Meanwhile, why don't you try this:==> https://shrtz.me/PtsVnf6 and get me a fast URL so that I can upload to Telegram, without me slowing down for other users."
