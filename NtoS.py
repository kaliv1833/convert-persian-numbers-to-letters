*****************Persian Number To Persian Letter*****************
num = input("Nember: ")
#Check If Input Is A Number
try:
	int(num)
except:
	print("Pleas Enter A Number!")
	exit
#Remove Primary Zeros(ex: 00001=1)
while num[0]=='0':
    num = num[1:]
#Define Under 1000 Translations
dict1 = {'0':'صفر', '1':'یک', '2':'دو', '3':'سه', '4':'چهار', '5':'پنج', '6':'شیش','7':'هفت', '8':'هشت','9':'نه','10':'ده', '11':'یازده', '12':'دوازده', '13':'سیزده', '14':'چهارده', '15':'پانزده', '16':'شانزده', '17':'هفده', '18':'هجده', '19':'نوزده', '20':'بیست' ,'30':'سی', '40':'چهل', '50':'پنجاه', '60':'شصت', '70':'هفتاد', '80':'هشتاد', '90':'نود', '100':'صد', '200':'دویست', '300':'سیصد', '400':'چهارصد', '500':'پانصد', '600':'ششصد', '700':'هفتصد', '800':'هشتصد', '900':'نهصد'}
#Define Up 1000 Translations
dict2 = {'1000000000000000000000':'سکستیلیون', '1000000000000000000':'کویینتیلیون', '1000000000000000':'کوآدریلیون', '1000000000000':'تریلیون', '1000000000':'میلیارد', '1000000':'میلیون', '1000':'هزار'} 
#List For Translating More Than 1000 Numbers
bigers = [1000000000000000000000,1000000000000000000,1000000000000000,1000000000000,1000000000, 1000000, 1000]
#Function For 1-3 Digits
def oneTwoThree(num):
    if len(num)==1:
        return dict1.get(num)
    elif len(num)==2:
        if dict1.get(num):
            return dict1.get(num)
        else:
            return dict1.get(num[0]+'0') + ' و ' + dict1.get(num[1])
    elif len(num)==3:
        if dict1.get(num):
            return dict1.get(num)
        else:
            if num[1]=='1':
                return dict1.get(num[0]+'00') + ' و ' + dict1.get(num[1:])
            else:
                return dict1.get(num[0]+'00') + ' و ' + dict1.get(num[1]+'0') + ' و ' + dict1.get(num[2])

#Translate Big Ones
if oneTwoThree(num)==None:
    num = int(num)
    message = ''
    for i in bigers:
        if num // i >= 1:
            message = message + oneTwoThree(str(num//i))  +' '+ dict2.get(str(i)) + ' و'
            num = num - (num//i)*i
    if num>=1:
        message = message + ' '+ oneTwoThree(str(num))
        print(message)
    else:
        print(message[:-1])
else:
    print(oneTwoThree(str(num)))

#*****************Writen By: Alireza Zeraatkar*****************
#*****************My Telegram Id: @eweraohw*****************
#GOOOOOOOOOODDDDDDDDDDDDLLLLLLUUUUUCCCCKKKK
