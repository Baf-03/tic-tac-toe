#tic tac toe

#starting
zero=one=two=three=four=five=six=seven=eight=" "

print(f"\n\t\t{zero}      | {one}      | {two}")
print(f"\t\t-------|--------|--------")
print(f"\t\t{three}      |      {four} | {five}")
print(f"\t\t-------|--------|--------")
print(f"\t\t{six}      | {seven}      | {eight}")




#for first player
n=True
k=True
used_places = []
wins= [[0,4,8],[0,3,6],[2,5,8],[0,1,2],[2,4,6],[3,4,5],[6,7,8],[1,4,7]]

tot_turns=0
while True:

    if tot_turns!=8:
        xstate=int(input("player one's turns"))
        while xstate>8 or xstate<0:
            xstate =int(input("plz enter between 0(including) and 8(including)"))
        while xstate in used_places :
            xstate =int(input("this place is not empty try again: "))
    else:
        print("Draw")
        break
            
    if xstate not in used_places:
        tot_turns+=1
        if xstate==0:
            zero="X"
        if xstate==1:
            one="X"
        if xstate==2:
            two="X"
        if xstate==3 :
            three="X"
        if xstate==4 :
            four="X"
        if xstate==5 :
            five="X"
        if xstate==6 :
            six ="X"
        if xstate==7:
            seven ="X"
        if xstate==8 :
            eight="X"
    used_places.append(xstate)
        
        
    print(f"\n\t\t{zero}      | {one}      | {two}")
    print(f"\t\t-------|--------|--------")
    print(f"\t\t{three}      |      {four} | {five}")
    print(f"\t\t-------|--------|--------")
    print(f"\t\t{six}      | {seven}      | {eight}")
    
    
    winnner =[[zero,four,eight],[zero,three,six],[two,five,eight],[zero,one,two],[two,four,six],[three,four,five],[six,seven,eight],[one,four,seven]]
    for win in winnner :
        if win[0]==" " or win[1]==" " or win[2]==" ":
            pass 
        elif win[0]=="X" and win[1]=="X" and win[2]=="X":
            print("player one wins:")
            n=False
            break
    if n==False:
        break
    
    
#for second player:
    if tot_turns!=8:
        zstate =int(input("player's two turn"))
        while zstate>8 or zstate<0:
            zstate =int(input("plz enter between 0(including) and 8(including)"))
        while zstate in used_places :
            zstate =int(input("this place is not empty try again: "))
            
    else:
        print("Draw")
        break
    
    if zstate not in used_places :
        tot_turns+=1
        if zstate==0 :
            zero="#"
        if zstate==1:
            one="#"
        if zstate==2:
            two="#"
        if zstate==3:
            three="#"
        if zstate==4:
            four="#"
        if zstate==5:
            five="#"
        if zstate==6:
            six="#"
        if zstate==7:
            seven="#"
        if zstate==8:
            eight="#"
        
        used_places.append(zstate)
        
        
    print(f"\n\t\t{zero}      | {one}      | {two}")
    print(f"\t\t-------|--------|--------")
    print(f"\t\t{three}      |      {four} | {five}")
    print(f"\t\t-------|--------|--------")
    print(f"\t\t{six}      | {seven}      | {eight}")
    
    winnner =[[zero,four,eight],[zero,three,six],[two,five,eight],[zero,one,two],[two,four,six],[three,four,five],[six,seven,eight],[one,four,seven]]
    for win in winnner :
        if win[0]==" " or win[1]==" " or win[2]==" ":
            pass 
        elif win[0]=="#" and win[1]=="#" and win[2]=="#":
            print("player two wins:")
            k=False
            
    if k==False:
        break
 
    if tot_turns==6:
        tot_turns-=1 
