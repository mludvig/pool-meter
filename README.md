# Pool water pH and temperature meter

- measure pool water pH and temperature
- report to MQTT topic

## Platform

- Raspberry Pi

## Sensors

- [Atlas Scientific pH probe](https://www.atlas-scientific.com/ph.html)
- DS18B20 temperature sensors accessed through [OWFS](https://owfs.org/)

## Notes

- The *pH circuit* must be electrically isolated from the ground and other electrical equipment like pumps to ensure accurate readings.
    - One way is to use [Atlas Scientific Isolated Carrier Board](https://www.atlas-scientific.com/product_pages/components/single_carrier_iso.html) 
    - Another option is to isolate the whole Raspberry Pi using an isolated 5V power supply (eg. search for [5V 2A isolated power supply](https://www.ebay.com/sch/i.html?_nkw=5V+2A+isolated+power+supply))

## Author

[Michael Ludvig](https://github.com/mludvig/)
