# 2FA Authenticator

Aplikacja generuje kody uwierzytelniania dwuskładnikowego co 30 sekund dla kluczy z pliku json. (Two-factor authentication).

## Instalacja

Zainstaluj pyton 3.12

```sh
# Install modules
phyton -m pip -m install tk
phyton -m pip -m customtkinter
phyton -m pip -m Pillow
```

## Uruchom z Windows

```sh
# With console
main.py

# No console
main.pyw
```

## Gui

<img src="https://raw.githubusercontent.com/atomjoy/2fa-gui/main/2FA_Python.png" width="480">

## Tests

Customtkinter nie zmienia koloru tektu i anchora CTkScrollableFrame z json, trzeba zmienić przy tworzeniu objektu klasy.

### Json

```json
{
    "CTkScrollableFrame": {
        "label_fg_color": ["#55cc55", "gray23"],
        "label_text_color": ["#fff", "gray23"],
        "label_anchor": ["w","w"]
    },
}
```

### Python class

```python
self.scrollable_label_button_frame = ScrollableLabelButtonFrame(
    master=self, width=300, command=self.label_button_frame_event, 
    corner_radius=5,
    label_text="Scrollable List Frame",    
    label_text_color=["#fff", "gray23"],
    label_anchor=["w", "w"],    
```

### Update

```sh
# Upgrade
python -m pip install --upgrade SomePackage
python -m pip install --upgrade pip
```
