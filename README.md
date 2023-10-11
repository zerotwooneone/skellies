# skellies
fun with servos and raspberry-pi

# Hardware

* ds3218mg
  * 20kg digital servo
* Pololu Maestro
  * 18 channel usb servo controller
* bench power supply
* raspberry pi 3

## Maestro Controller Doc

* <https://www.geneseo.edu/~pogo/LabVIEW/Assignments/Demos/maestro.pdf>
* <https://www.pololu.com/docs/0J41>

### From the README.md

install from file
`pip3 install -r requirements.txt`

Old (depricated)
`python3 -m pip install pyserial`

## Serial on Pi

### Might have to disable onboard Bluetooth

<https://www.abelectronics.co.uk/kb/article/1035/raspberry-pi-3-serial-port-usage>

* `sudo nano /boot/config.txt`
  * Add at the end of the file
  * `dtoverlay=disable-bt`
* `sudo systemctl disable hciuart`

### Disable Pi Serial in Config

Disable Serial Terminal
`sudo raspi-config select interfacing options -> Serial -> No -> Yes save & exit`

## Python Library

`git clone https://github.com/FRC4564/Maestro`

## Linux Software (tested, not used)

<http://www.pololu.com/file/download/maestro-linux-100507.tar.gz?file_id=0J315>

### From the README.txt

* in order to run the GUI application
  * `sudo apt install libusb-1.0-0-dev mono-runtime libmono-system-windows-forms4.0-cil`
* to get the usb to connect
  * `copy the file 99-pololu.rules to /etc/udev/rules.d/`
  * `sudo udevadm control --reload-rules`
* to get commands to work, run the GUI app and change Serial Settings -> Serial Mode to 'USB Dual Mode'
  * !!! and don't forget to click 'Apply Settings' !!!

## Windows software (untested)

http://www.pololu.com/file/download/maestro-windows-130422.zip?file_id=0J266
