# 🧠 On-Screen Agent with OCR, AI, and Action Dispatching

A cross-platform screen analysis agent powered by hotkey activation, OCR, natural language prompts, and smart dispatching. It integrates AI summarization, IBM ACP hooks, and native app control (Word, Excel, PowerPoint), all in a lightweight Python framework.

---

## 🚀 Features

- ✅ Hotkey-triggered screen capture and OCR
- 🧠 Natural language command prompt via Tkinter
- 📝 Custom Notes App (GUI with AI text summarization)
- 📇 Simulated Contacts App
- 💼 Launches Word, Excel, PowerPoint directly
- 🪶 Minimal footprint, cross-platform support

---

## 📁 Project Structure


---

## ⚙️ Setup Instructions

### 1. Clone the Repository
git clone https://github.com/SuccessSoham/on-screen-agent.git
cd on-screen-agent

### 2. Set Up Virtual Environment
python -m venv env
# On Windows
env\Scripts\activate
# On macOS/Linux
source env/bin/activate

### 3. Install Requirements
pip install -r requirements.txt

### 4. Install Tesseract OCR
# Download from UB Mannheim build
# Make sure tesseract.exe is added to your system PATH

### 5. ▶️ Run the Agent
python agent.py

### Then press the x key to trigger the agent.

# You’ll be prompted with: "What would you like me to do?"

# Try commands like:

Open notes

Launch contact book

Start Word

exit (← shuts down the agent)

### 🛠️ Dev Tips
Press Ctrl+C or type exit into the prompt to cleanly stop the agent

Modify the hotkey in main.py (key.char == 'x') to whatever you like

Extend action_dispatcher.py to route more custom commands

### 📜 License
This project is open source and available under the MIT License.

### 💡 Ideas for Future
System tray toggle for agent lifecycle

Speech input + voice assistant trigger

Configurable command → script mapping (YAML or JSON)

ACP result feedback loop

Built with 🧠 and ☕ by Soham.
