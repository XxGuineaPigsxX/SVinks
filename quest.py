import time
print('неизвестный: здраствуйте, вы находитесь в лабораторие..')
time.sleep(3)
print('другой неизвестный: я ваш врач..')
time.sleep(3)
print('*когда врач ушел у вас есть возможность обследовать комнату или попробовать открыть железную дверь.Ваша цель сбежать*')
time.sleep(3)
v = input("выберите: обследовать комнату или попробовать открыть железную дверь: ") 
while v != "обследовать комнату" and v != "попробовать открыть железную дверь":
    v = input("выберите: обследовать комнату или попробовать открыть железную дверь ")
if v == "обследовать комнату":
    time.sleep(1)
    print("ты находишься в маленькой комнате,под кроватью ты нашел перачинный нож ")
    time.sleep(2)
    v = input("выберите: попробовать открыть дверь или взять перачинный нож: ")
    if v == "попробовать открыть дверь":
        print("на твои стуки в дверь и громкие удары пришел врач и вколол какую-то жидкость в шприце")
        time.sleep(2)
        print("вы уснули и больше не проснетесь")
        print("Game over")
        exit()
    else:
        print("вы взяли ножик и положили себе в карман, на проверке у вас нашли перачинный нож и отобрали")
        v = input("Выберите:отобрать нож обратно или промолчать : ")
        while v != "отобрать нож" and v != "промолчать":
            v = input("Выберите:Выберите:отобрать нож обратно или промолчать " )
        if v == "промолчать":
            print("вас отвели обратно в палату, дали какие-то таблетки и вы уснули")
            print("врач с незнакомцем в это время что-то обсуждали вышли из комнаты и забыли закрыть железную дверь")
        else:
            print("много врачей сбегаются и пытаются утихомерить вас, в конечном итоге вас застрелили")
            print("Game over")
            exit()
              
          
    #####################################################################################
     
     
        v = input("Выберите:сбежать или остаться в комнате: ")
        while v != "сбежать" and v != "остаться в комнате":
            v = input("Выберите:сбежать или остаться в комнате " )
        if v == "сбежать":
            print("вас пытались останавливать шокированные врачи, но у вас был один шанс сбежать поэтому вы всех отталкивали и бежали со всех сил")
            print('только в конце когда вы уже были в шаге от свободы в вас попали пулей в голову но вы успель ступить на свободу')
            print('теперь ваша душа живет на свободе вы выполнили свою цель...все остальное позади')
            print('вы можете отправляться к богу или остаться на земле и пугать детей...........')
            print("С победой!")    
         
         
           
           
           