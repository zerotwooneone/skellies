# skellies
fun with servos and raspberry-pi

## Hardware
* ds3218mg 
  * 20kg digital servo
* Pololu Maestro 
  * 18 channel usb servo controller
* bench power supply
* raspberry pi 3

## Maestro Controller Doc
https://www.geneseo.edu/~pogo/LabVIEW/Assignments/Demos/maestro.pdf

### Linux Software
http://www.pololu.com/file/download/maestro-linux-100507.tar.gz?file_id=0J315

#### From the README.txt
* in order to run the GUI application
  * `sudo apt install libusb-1.0-0-dev mono-runtime libmono-system-windows-forms4.0-cil`
* to get the usb to connect
  * `copy the file 99-pololu.rules to /etc/udev/rules.d/`
  * `sudo udevadm control --reload-rules`
* to get commands to work, run the GUI app and change Serial Settings -> Serial Mode to 'USB Dual Mode' 
  * !!! and don't forget to click 'Apply Settings' !!!

### Python Library
`git clone https://github.com/FRC4564/Maestro`

#### From the README.md
`python3 -m pip install pyserial`

### Windows software (untested)
http://www.pololu.com/file/download/maestro-windows-130422.zip?file_id=0J266
