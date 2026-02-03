# DO NOT UPDATE ANY CODE BELOW THIS LINE

import random as ran

tax_dct = {
    "national":(10,37),
    "state"   :(0,13.3),
    "local"   :(0,3.8)
}

def help(key):
    t = tax_dct[key]
    return f"{ran.randint(int(t[0]), int(t[1]))}.{ran.randint(0,99)}"

def get_tax_rate(flag=True):
    if flag:
        tax_type = ran.randint(0,2)
        tax = 0.0
       
        for i,e in enumerate(tax_dct):
            if i == tax_type:
                return help(e)
    else:
        nat_tax = help("national")
        ste_tax = help("state")
        loc_tax = help("local")
       
        zipLst = zip(tax_dct.keys(),[nat_tax,ste_tax,loc_tax])
        tax_lst = [f"{a} tax:{b}" for (a,b) in zipLst]
        return ",".join(tax_lst)

def get_cost():
    val = ['500', '5000', '50']
    val_type = ran.randint(0,2)
    cost = ran.randint(0, int(val[val_type]))
    return f"{cost}.{ran.randint(0,99)}"
