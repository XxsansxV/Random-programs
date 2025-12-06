import random
import turtle

#number guess

def numguess():
    condition="no"
    number=random.randint(0,100)
    attcount=0
    while condition=="no":
        attcount=attcount+1
        guess=int(input("guess the number."))
        if guess>number:
            print(f"the number {guess} is bigger than the number")
        elif guess<number:
            print(f"the number {guess} is smaller than the number")
        elif guess==number:
            print(f"gg bro, you did it. it's {number}. you did it in {attcount} tries")
            condition="yes"
            break

#rock paper scissors
def rockpaperscissors():
    computerrps=random.choice(["rock","paper","scissors"])
    playerrps=input("rock, paper, or scissors.")
    if playerrps==computerrps:
        print("tie")
    elif (playerrps=="rock" and computerrps=="scissors")or(playerrps=="scissors" and computerrps=="paper")or(playerrps=="paper" and computerrps=="rock"):
        print(f"you chose {playerrps}, which beats {computerrps}, you won!")
    elif (playerrps=="scissors" and computerrps=="rock")or(playerrps=="paper" and computerrps=="scissors")or(playerrps=="rock" and computerrps=="paper"):
        print(f"you chose {playerrps}, which is absolutely and utterly inferior to {computerrps}, you lost, loser!")
    else :
        print("the computer got mad because you didn't input a proper action, you lost.")

#rand16int
def rand16int():
    i1=random.randint(0,9)
    i2=random.randint(0,9)
    i3=random.randint(0,9)
    i4=random.randint(0,9)
    i5=random.randint(0,9)
    i6=random.randint(0,9)
    i7=random.randint(0,9)
    i8=random.randint(0,9)
    i9=random.randint(0,9)
    i10=random.randint(0,9)
    i11=random.randint(0,9)
    i12=random.randint(0,9)
    i13=random.randint(0,9)
    i14=random.randint(0,9)
    i15=random.randint(0,9)
    i16=random.randint(0,9)
    print(f"{i1}{i2}{i3}{i4}{i5}{i6}{i7}{i8}{i9}{i10}{i11}{i12}{i13}{i14}{i15}{i16}")
    rand=f"{i1}{i2}{i3}{i4}{i5}{i6}{i7}{i8}{i9}{i10}{i11}{i12}{i13}{i14}{i15}{i16}"

#strand
def strand():
    strand=hash(rand16int())

#shapegen
def turtl():
    turt=turtle.Turtle()
    turt.color(str(input("input the color here.")))
    turt.pensize(int(input("insert a number between 1 to 5 for the size")))
    turt.speed(int(input("pick a number from 1 to 10 for the size, use 0 for the fastest speed.")))
    n=int(input("pick a shape using the amount of corners it has. eg. 4 for square."))
    size=int(input("pick a coeficient to be used for the size."))
    turnhowmuch=n-2
    turnhowmuchfi=turnhowmuch*180/n
    it=0
    while it<n:
        it=it+1
        turt.forward(size*10)
        turt.right(turnhowmuchfi)

while True:
    chosengame=input("welcome. pick between numguess and rockpaperscissors and rand16int and strand and turtle. \nuse ng/rps/16/str/t")
    if chosengame=="ng":
        numguess()
    elif chosengame=="rps":
        rockpaperscissors()
    elif chosengame=="16":
        rand16int()
    elif chosengame=="str":
        strand()
    elif chosengame=="t":
        turtl()
    else :
        print("urm, did you hear me? input the proper stuff.")