#Phone Number Info Finder Program

#Importing Libarires
import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone
from time import sleep

print('\nAdd Country Code before adding Phone No. EXAMPLE" +91 "')
sleep(3)

while(True):
    
    print('\n\tPress Enter to Exit\n')
    
    #Phone Number Input From User

    phone_number = input('Enter ur phone no. :')
    if not phone_number:
        break
    
    #Converting To String
    str(phone_number)

    phone_number_parse = phonenumbers.parse(phone_number, "CH")

    #Printing Phone No, Country Name, Carrier Name, Time Zone
    print('\nPhone No :\t', phone_number)
    print('Country Name :\t', geocoder.description_for_number(phone_number_parse, "en"))
    print('Carrier Name :\t', carrier.name_for_number(phone_number_parse, "en"))
    print('Time Zone :\t', timezone.time_zones_for_number(phone_number_parse), '\n')

