# 2FA Authenticator GUI

Aplikacja generuje kody uwierzytelniania dwuskładnikowego co 30 sekund dla kluczy z pliku json. (Two-factor authentication).

## Instalacja

Zainstaluj pyton 3.12 <https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe>

```sh
# Install modules
phyton3 -m pip install tk, pyotp
phyton3 -m pip install customtkinter
phyton3 -m pip install Pillow
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
        "label_anchor": "w"
    },
}
```

### Python class

```python
self.scrollable_label_button_frame = ScrollableLabelButtonFrame(
    master=self, width=300, command=self.label_button_frame_event, 
    corner_radius=5,
    label_text="Scrollable List Frame",    
    label_text_color=("#fff", "gray23"),
    label_anchor="w",
```

### Update

```sh
# Upgrade
python3 -m pip install --upgrade SomePackage
python3 -m pip install --upgrade pip
```

## Debian 12 Install CustomTkinter

Debian 12 dodaj środowisko wirtualne w katalogu projektu.

- <https://code.visualstudio.com/docs/python/environments#_creating-environments>

### Instalacja .venv i pakietów

```sh
# Install
sudo apt install python3-full python3-venv python3-pip

# Create .venv
sudo python3 -m venv .venv

# Run venv in vscode select main.py file window
# Press Ctrl + Shift + p  Or F1 button then enter (or from vscode bottom bar):
Python: Select Interpreter

# Install project packages
pip install customtkinter
pip install Pillow
pip install pyotp
pip install tk

# Then run script from vscode integrated terminal
python3 main.py
```

### Lub uruchom z terminala

```sh
# Run virtual env from terminal
source .venv/bin/activate

# Install project packages
pip install customtkinter
pip install Pillow
pip install pyotp
pip install tk

# Run script
python3 main.py

# Deactivate venv if no more needed
deactivate
```
