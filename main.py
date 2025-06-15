import threading
from pynput import keyboard

# Ensure agent modules are available
try:
    from agent import screen_analyzer, action_dispatcher
except ImportError as e:
    print(f"❗ Import failed: {e}")
    print("Make sure 'agent/screen_analyzer.py' and 'agent/action_dispatcher.py' exist and are working.")
    exit(1)

def on_activate() -> None:
    """Triggered when the hotkey key is pressed."""
    def run_agent():
        print("🔍 Hotkey pressed! Capturing screen and analyzing...")
        try:
            screenshot = screen_analyzer.capture_screen()
            screen_text = screen_analyzer.run_ocr(screenshot)
            print("📝 Extracted Text:\n", screen_text)
            command = action_dispatcher.prompt_user_command()
            if command:
                action_dispatcher.dispatch_action(command, screen_text)
        except Exception as e:
            print(f"⚠️ Error during analysis: {e}")

    threading.Thread(target=run_agent, daemon=True).start()

def on_press(key: keyboard.Key) -> None:
    try:
        if isinstance(key, keyboard.KeyCode) and key.char == 'y':
            print("✅ Hotkey 'y' detected.")
            on_activate()
    except AttributeError:
        pass  # Ignore special keys

def on_release(key: keyboard.Key) -> None:
    pass  # We don't track key releases for single-key hotkeys

def start_listener() -> None:
    print("🚀 Listener started. Press the 'y' key to activate the agent.")
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("🛑 Listener stopped by user.")

if __name__ == "__main__":
    start_listener()