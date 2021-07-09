tea,coffee={"Tea":{"1.lemon_tea":["1.tea_small 20 rs","2.tea_medium 30 rs","3.tea_large 40 rs"],"2.milk_tea":["1.tea_small 20 rs","2.tea_medium 30 rs","3.tea_large 40 rs"]}},{'coffee':{"1.cold_Coffee":["1.coffee_small 40 rs", "2.coffee_medium 60 rs", "3.coffee_large 80 rs"],"2.hot_Coffee2":["1.coffee_small 40 rs","2.coffee_medium 60 rs","3.coffee_large 80 rs"]}}
for i,z in zip(tea.values(),coffee.values()):
    print("\n1. Tea","\n2.Coffee")
    us =int(input("\nWhat do you want to drink? for Tea press 1 or for Coffee press 2 :"))
    if us==1 or us==2:
        print(f"\n{list(i.keys())[0]}\n{list(i.keys())[1]}") if us == 1 else print(f"\n{list(z.keys())[0]}\n{list(z.keys())[1]}")
        user = int(input("\nEnter your choice:"))
        if user == 1 or user==2:
            for k,x in zip(i.values(),z.values()):
                print(f"\n{k[0]}\n{k[1]}\n{k[2]}") if us==1 else print(f"\n{x[0]}\n{x[1]}\n{x[2]}")
                s=int(input("\nEnter your size : s,m or l"))
                if s=='s':
                    print("\nYou Have To Pay 20 rs") if us==1 else print("\nYou Have To Pay 40 rs")  
                    break    
                elif s=='m':
                    print("\nYou Have To Pay 30 rs") if us==d1 else print("\nYou Have To Pay 60 rs")
                    break
                elif s=='l':
                    print("\nYou Have To Pay 40 rs") if us==1 else print("\nYou Have To Pay 80 rs") 
                    break
                else:
                    print('\nYou Enter a Wrong Input')
                    break
