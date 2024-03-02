# 2FA Authenticator GUI

Aplikacja generuje kody uwierzytelniania dwuskładnikowego co 30 sekund dla kluczy z pliku json. (Two-factor authentication).

## Instalacja

Zainstaluj pyton 3.12 <https://www.python.org/ftp/python/3.12.2/python-3.12.2-amd64.exe>

```sh
# Install modules
phyton3 -m pip -m install tk
phyton3 -m pip -m customtkinter
phyton3 -m pip -m Pillow
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

Debian 12 vitrual environment

```sh
# Install
sudo apt install python3-full python3-pip

# Check Debian 12
sudo which python3
sudo python3 --version
sudo pip3 --version

# Create virtual env python3 Debian 12 
sudo python3 -m venv ~/tutorial-venv

# Run virtual env
source tutorial-venv/bin/activate

# Run install
pip3 install customtkinter
pip3 install Pillow

# Or install
sudo ~/tutorial-venv/bin/pip3 install Pillow
sudo ~/tutorial-venv/bin/pip3 install customtkinter
sudo ~/tutorial-venv/bin/pip3 install darkdetect

# Run script
python3 ~/tutorial-venv/main.py

# Deactivate virtual env
deactivate
```
