from pynput import keyboard
from pydbus import SessionBus

bus = SessionBus()
shell = bus.get('org.gnome.Shell')

keys_pressed = []


def on_release():
    global keys_pressed

    if len(keys_pressed) == 1 and keys_pressed[0] == keyboard.Key.shift:
        print('TOGGLE RUS ***********')
        shell.Eval('imports.ui.status.keyboard.getInputSourceManager().inputSources[1].activate()')
    elif len(keys_pressed) == 1 and keys_pressed[0] == keyboard.Key.shift_r:
        print('TOGGLE UKR ***********')
        shell.Eval('imports.ui.status.keyboard.getInputSourceManager().inputSources[2].activate()')
    elif len(keys_pressed) == 1 and keys_pressed[0] == keyboard.KeyCode(16777215):
        print('TOGGLE ENG ***********')
        shell.Eval('imports.ui.status.keyboard.getInputSourceManager().inputSources[0].activate()')
    else:
        pass
    keys_pressed = []


def on_press(key):
    global keys_pressed
    keys_pressed.append(key)


with keyboard.Events() as events:
    for event in events:
        if isinstance(event, events.Press):
            on_press(event.key)
        if isinstance(event, events.Release):
            on_release()