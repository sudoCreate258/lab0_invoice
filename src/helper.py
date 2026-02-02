# DO NOT UPDATE ANY CODE BELOW THIS LINE

import random as ran

tax_dct = {
    "national":(10,37),
    "state":(0,13.3),
    "local":(0,3.8)
}

def help(dct, key, indx=0):
    t = dct[key][indx]
    return int(t)

def get_tax_rate(flag=True):
    if flag:
        tax_type = ran.randint(0,2)
        tax = 0.0
        
        for i,e in enumerate(tax_dct):
            if i == tax_type:
                tax = ran.randint(help(tax_dct,e), help(tax_dct,e,1) ) 
                return f"{tax}.{ran.randint(0,99)}"
    else:

            
        nat_tax = ran.randint( help(tax_dct,"national"), help(tax_dct,"national",1) )
        ste_tax = ran.randint( help(tax_dct,"state"),    help(tax_dct,"state",1)    )
        loc_tax = ran.randint( help(tax_dct,"local"),    help(tax_dct,"local",1)    )
        
        zipLst = zip([nat_tax,ste_tax,loc_tax], tax_dct.keys())
        
        tax_lst = [f"{a} tax:{b}.{ran.randint(0,99)}" for (b,a) in zipLst]
        return ",".join(tax_lst)
        

def get_cost():
    val = ['500', '5000', '50']
    val_type = ran.randint(0,2)
    cost = ran.randint(0, int(val[val_type]))
    return f"{cost}.{ran.randint(0,99)}"
