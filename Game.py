pl_ch: str = str(input("Напиши камень, ножницы или бумага: "))
pk_ch: str = "камень" 
if (pl_ch == "ножницы" and pk_ch == "бумага") or (pl_ch == "бумага" and pk_ch == "камень") or (pl_ch == "камень" and pk_ch == "ножницы"):
    print("Win")
elif pl_ch == pk_ch:
    print("Tie")
else:
    print("loss")