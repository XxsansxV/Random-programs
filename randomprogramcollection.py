import random
import turtle
from datetime import datetime

#numguess
def numguess():
    smallest_number = 0
    biggest_number = 100
    condition="no"
    number=random.randint(smallest_number,biggest_number)
    attcount=0
    while condition=="no":
        attcount+=1
        while(True):
            try:
                guess=int(input("guess the number.").strip())
                break
            except ValueError:
                print("try again, put a number")
        if guess>number:
            print(f"the number {guess} is bigger than the number")
        elif guess<number:
            print(f"the number {guess} is smaller than the number")
        elif guess==number:
            print(f"gg bro, you did it. it's {number}. you did it in {attcount} tries")
            condition="yes"
            break

#rockpaperscissors
def rockpaperscissors():
    while True:
        computerrps=random.choice(["rock","paper","scissors"])
        playerrps=input("rock, paper, or scissors.").strip().lower()
        if playerrps==computerrps:
            print("tie")
            break
        elif (playerrps=="rock" and computerrps=="scissors")or(playerrps=="scissors" and computerrps=="paper")or(playerrps=="paper" and computerrps=="rock"):
            print(f"you chose {playerrps}, which beats {computerrps}, you won!")
            break
        elif (playerrps=="scissors" and computerrps=="rock")or(playerrps=="paper" and computerrps=="scissors")or(playerrps=="rock" and computerrps=="paper"):
            print(f"you chose {playerrps}, which is absolutely and utterly inferior to {computerrps}, you lost, loser!")
            break
        else :
            print("please try again")

#shapegen
def shapegen():
    def inputvalercatchturt(prompt):
        while True:
            try:
                return int(input(prompt).strip())
            except ValueError as e:
                print(f'{e} is not an integer, try again.')
    turt=turtle.Turtle()
    while True:
        try:
            turt.color(str(input("input the color here.").strip().lower()))
            break
        except turtle.TurtleGraphicsError as e:
            print(f'sorry, {e} is not a proper color. try again.')
    turt.width(inputvalercatchturt("input the line's width : "))
    turt.speed(inputvalercatchturt("set the speed from 0-10, 0 is the fastest: "))
    size = inputvalercatchturt("pick a coefficient for the size : ")
    n = inputvalercatchturt("input n of n-gons : ")
    turnhowmuchfinal=360/n
    it=0
    while it<n:
        it+=1
        turt.forward(size*10)
        turt.right(turnhowmuchfinal)

#above are old programs
#from this point on, the programs are new and better.

#salaman
def salaman():
    nama = input("masukkan namamu:")
    salam = "selamat pagi "
    Response = salam + nama
    print(Response)
    while True:
        try:
            tahun = int(input("masukkan tahun lahir:").strip())
            break
        except ValueError:
            print("coba lagi")
    # Ricco from july 17th 2026, you should futureproof this.
    hasil_umur = datetime.now().year-tahun
    print(f'Kamu tahun ini berumur {str(hasil_umur)} tahun kan?')
    alamat = input("alamatmu apa ya?")
    print(f'alamatmu {alamat} ya? cukup jauh ya dari sekolah!')

#kalkulator
def kalkulator():
    print("\nKalkulator sederhana")
    print("<<hanya menerima bilangan bulat!>>")
    print("________________________________")

    def valerinput(tbc,counter):
        while(True):
            try:
                tbc=int(input(f'Masukkan angka {counter}: ').strip())
                return tbc
            except ValueError:
                print("try again. I think you put a space or some dumb characters in there. absolutely numbers only bro")

    num1=valerinput(0,"pertama")
    num2=valerinput(0,"kedua")
    hasil = 0

    print("_ _")
    operasi=input("masukkan operasi (+,-,*,/)").strip()
    print('\n ________________________________')
    if operasi=="+":
        hasil = num1+num2
    elif operasi=="-":
        hasil= num1-num2
    elif operasi=="*":
        hasil = num1*num2
    elif operasi == "/":
        try:
            hasil = round(num1/num2)
        except ZeroDivisionError:
            hasil="Dividing zero with zero does not make sense at all. To put it simply, imagine trying to find out how many 0s it would take to make a 0. How are you supposed to do that? every single number multiplied by zero is 0 anyways, which would mean that 0/0 is every single number to exist, something that makes absolutely no sense.\nSo please, insert something else. here's your punishment for doing that to this innocent program bro, i knew you just wanted to error me, but not today.\nthe result is Not a number."
    else:
        print("ERRORRRRR broh, masukkin + - * /. Gini deh, balik aja lu ke awal.")
        kalkulator()
    print(f'Hasil dari {num1}{operasi}{num2} adalah {hasil}\n')

#gambling
def gamble():
    money = 100
    while True:
        print(f'there is {money} pypiahs in your bank account. \nhow much money would you like to gamble today?')
        while True:
            try:
                gambledmoney=int(input("insert the amount of money to gamble : "))
                if gambledmoney<=money:
                    break
                elif gambledmoney>money:
                    print("try again.")
            except ValueError:
                print(f'try again.')
        gamblingmult = random.randint(1,10)
        finalgamblingmult = gamblingmult * random.choice([-1,-1,1])
        finalgamblingresult = gambledmoney * finalgamblingmult
        money = finalgamblingresult + money
        if finalgamblingmult<0:
            print(f'you lost {finalgamblingresult} money!')
        elif finalgamblingmult>0:
            print(f'you won {finalgamblingresult} money!')
        if money<=0:
            print('you lost all your money.')
            break


#pemilih program
def choicer():
    try:
        while(True):
            choice=input("pilih salaman atau kalkulator atau numguess atau rps atau shapegen atau gamble. .\nGunakan Q untuk keluar.\n").lower().strip()
            if choice==("kalkulator"):
                kalkulator()
            if choice==("salaman"):
                salaman()
            if choice==("numguess"):
                numguess()
            if choice==("rps"):
                rockpaperscissors()
            if choice==("shapegen"):
                shapegen()
            if choice == "gamble":
                gamble()
            if choice==("q"):
                print("bye.")
                break
            elif choice not in ["kalkulator", "salaman","numguess","rps","shapegen"]:
                print("._.")
    except KeyboardInterrupt:
        print("\nbye byeeee")

choicer()
