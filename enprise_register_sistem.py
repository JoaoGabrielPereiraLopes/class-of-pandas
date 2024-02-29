#in this code I chaleng my ability of in dictionaries making one emprise register sistem

leave=False# while false don't finish code
sistem={}#criate a sistem of regist itens
money=0

while not leave:
    trys=0#received 0 in all executions in "for"
    
    for item in sistem:# item received all keys in sistem
        trys+=1
        print(trys,'-',item,':',sistem[item])#print all information in sistem
    
    action=input("write your action: ")#decide the action of sistem
    print('your money is ',money)
    if action.upper()=="REGISTER" or action.upper()=='SWITCH':#if action equal register regist item
        name=input('write the name product: ')#receive name of product
        price=float(input(f'write the price of {name}: '))#received price of product
        quantity=int(input(f'write the quantity of {name}: '))#received quantity of product
        sistem[name]={'price':price,'quantity':quantity}#register in sistem
    
    if action.upper()=='SELL':#if action equal sell make a  need alteracion in sistem
        name=input('what product you sell: ')#received name of product
        quantity=int(input("why product you sell: "))#received quatity of product
        
        if name in sistem:# verify if sell is possible
            
            if sistem[name]['quantity'] >= quantity:
                sistem[name]['quantity']-=quantity
                money+=sistem[name]['price']*quantity
            
            else:# if verification is false print sell is imposible
                print('sell is imposible')
        
        else:# if verification is false print sell is imposible
            print('sell is imposible')
    
    if action.upper()=='LEAVE':#if action equal 'leave' finish the program
        leave=True