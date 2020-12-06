===============================================================================
 Name: 		Auto Response for Streamlabs Bot
 Description: Bot will automatically reply when users input keywords in chat.
 Version: 	1.0.0
 Creator: 	Tristia
 Website:	https://github.com/fydeszzz/StreamBotScripts
 Recently Release Date: 2020/12/6
===============================================================================
 - Enable/Disable using the command when the stream is offline
   是否限定實況中才能使用
 - Customisable permission for using the command
   自訂使用者權限(所有人、訂閱者等)
 - Customisable emotes when response (use comma as seperator)
   自訂機器人回應時使用隨機表情符號(使用,號區隔)
 - Customisable keywords
   自訂關鍵字(僅包含首字)
===============================================================================
 Examples and rules 使用範例
 
 - You can use "OPEN'KEYWORDLIST'" button in UI to open txt file,
 do not change filename or filepath.
 使用介面中的"OPEN'KEYWORDLIST'"按鈕打開關鍵字名單，不要更改檔名或檔案路徑
 
 - Write down keywords on keyword.txt, and bot response behind ',';
 press enter to type another keyword on new line.
 將想偵測的關鍵字寫在keyword.txt中，機器人回應的語句用,符號隔開寫在後方；
 並使用enter鍵換行分隔其他關鍵字。
 
 - 關鍵字與回應輸入範例如下：
 ex: hello,$username HELLO!
 
 - When a user input "hello" in chat, bot will reply:
 當使用者在聊天室輸入"Hello"時，機器人會做出以下回覆:
 
 Apollo123: hello!
 bot: Apollo123 HELLO!

 ※需為使用者輸入的首字或使用空白鍵分隔，才可被機器人偵測到。
 若首字後方有表情符號、特殊符號(!@#$等)也會被列為關鍵字。
===============================================================================
 Usable Variable 可使用參數定義
 
 $username : username 使用者名稱
 $now : local time 現在當地時間
