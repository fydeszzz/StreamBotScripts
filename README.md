# StreamBotScripts

> A collection of Python bot scripts for [Streamlabs Chatbot](https://streamlabs.com/chatbot), designed to enhance live stream interactivity and automation.

---

## 📁 Project Structure

```
StreamBotScripts/
├── AutoResponse/
│   ├── AutoResponse_StreamlabsSystem.py   # Main script
│   ├── UI_Config.json                     # UI configuration
│   ├── keywordlist.txt                    # Keyword-response mapping
│   ├── UI.png                             # UI screenshot
│   └── README.txt
├── CallDragon/
│   ├── CallDragon_StreamlabsSystem.py     # Main script
│   ├── UI_Config.json                     # UI configuration
│   └── README.txt
├── Clock_Notify/
│   ├── Clock_Notify_StreamlabsSystem.py   # Main script
│   ├── UI_Config.json                     # UI configuration
│   └── README.txt
└── GoSleep/
    ├── GoSleep_StreamlabsSystem.py        # Main script
    ├── UI_Config.json                     # UI configuration
    └── README.txt
```

---

## ✅ Prerequisites

- [Streamlabs Chatbot](https://streamlabs.com/chatbot) (Windows only)
- Python 2.7 *(bundled with Streamlabs Chatbot — no separate install needed)*
- A Twitch account connected to Streamlabs Chatbot

---

## 🚀 Installation

1. Download or clone this repository:
   ```bash
   git clone https://github.com/fydeszzz/StreamBotScripts.git
   ```
2. Open **Streamlabs Chatbot**.
3. Navigate to **Scripts** tab in the left sidebar.
4. Click the **Import** button (folder icon), and select the script folder you want to use (e.g., `AutoResponse/`).
5. The script will appear in the script list — click it to configure settings via the UI panel.
6. Enable the script by toggling it **ON**.

---

## 📜 Scripts

### 1. AutoResponse — 自動回應機器人
**Version:** 1.0.0 | **Released:** 2020/12/06

Automatically responds in chat when a viewer types a matching keyword.

**Features:**
- Keyword detection (supports partial match on first character or whitespace-separated tokens)
- Customizable response messages
- Built-in variables: `$username` (viewer's name), `$now` (current local time)
- Optional random emote/emoji in responses
- Permission control (Everyone / Subscriber / etc.)
- Can be toggled on/off based on stream live status

**Keyword format** (in `keywordlist.txt`):
```
hello,$username Hello there!
gg,$username Well played!
```

---

### 2. CallDragon — 召喚神龍（小遊戲）
**Version:** 1.0.0 | **Released:** 2020/12/04

A mini-game where viewers collectively type a command. Once the count reaches the configured goal, all participating viewers receive reward currency.

**Features:**
- Customizable trigger command
- Configurable participation goal count
- Reward currency payout to all participants
- Cooldown settings to prevent abuse
- Permission control

---

### 3. Clock Notify — 報時語音機器人
**Version:** 1.0.0 | **Released:** 2020/11/08

Plays a voice response based on the current local time when triggered by a viewer command.

**Features:**
- Time-based audio file selection
- Custom audio files required (`.mp3` / `.wav`)
- Configurable trigger command and permissions

> ⚠️ **Note:** You must prepare your own audio files and place them in the script folder.

---

### 4. GoSleep — 自動播放語音機器人
**Version:** 1.0.0 | **Released:** 2020/11/29

Automatically plays a specified audio file at a user-configured local time — useful for sending a "time to sleep" reminder during late-night streams.

**Features:**
- Scheduled playback based on local time
- Fully configurable time and audio file path
- Runs in the background without viewer interaction

> ⚠️ **Note:** You must prepare your own audio files and configure the file path in the script settings.

---

## ⚙️ Configuration

Each script includes a **UI panel** inside Streamlabs Chatbot where you can adjust settings without editing code. Common configurable options include:

| Option | Description |
|---|---|
| Command | The chat command that triggers the script |
| Permission | Who can use the command (Everyone, Subscriber, etc.) |
| Cooldown | Seconds before the command can be used again |
| Response Message | The bot's reply text |
| Audio File Path | Path to the audio file (for voice scripts) |

---

## 📝 License

This project is for personal and educational use. Feel free to modify and adapt for your own streams.
