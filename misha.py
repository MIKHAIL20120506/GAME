import random 
print("Здраствуйте это игра spider man:Begin Сюжет: Bас укусил радиоактивный паук и у вас поевились силы ходить по стенам стрелять паутиной вы сильные и у вас чуйка")
playerhp = 100
playerenergy = 100
bosshp = 100
playeractiv = None
bossact = None
#x=input("выберете 1.пойти драться ")
#if x== "1":
#    print("вы полетели на паутине к боссу")
x=input(f"вы прилетели к боссу у вас есть выбор 1."+
        f"ударить рукой но усталость минус 5(у вас {playerenergy} "+
        f"сил каждый удар рукой по -5 сил)2.ударить ногой -15 сил ")
if x== "1":
    playeractiv = "бить рукой"
bossactiv = ["бить рукой","уворачиваться"]
bossrandom = random.choice(bossactiv)
if bossrandom == "бить рукой":
    playerhp -= 5
    print(f"босс ударил вас рукой у вас осталось {playerhp} хп")
if bossrandom == "уворачиваться":
    print("босс увернулся хп ему не наносяться ")
#if x== "2":
#    print("вы ударирили ногой минус 15 хп босса у него 85 хп")

