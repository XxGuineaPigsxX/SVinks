def n (gg):
    n = False
    for  i in a:
        if i <= "a" and i <= "z":
             n = True
             break
    return n
################################################################################
def m (gg):
    m = False
    for  i in a:
        if i <= "0" and i <= "9":
             m = True
             break
    return m
####################################################################################3
def b (gg):
    b = False
    for  i in a:
        if i <= "A" and i <= "Z":
            b = True
            break
    return b
#####################################################################################3
def v (gg):
    v = ["!", "?", "@", "#", "$", "%", "&", "^", "*", ".", ","]
    v = False
    for  i in a:
        if i in v:
            v = True
            break
    return v
###############################################################################################33333
gg = input("введите пароль: ")
if n (gg) == False:
    print("в пароле нет букв")
elif m (gg) == False:
    print("в пароле нет цифр")
elif b (gg) == False:
    print("в пароле нет больших букв")
elif v (gg) == False:
    print("в пароле нет спец. символов")
    




