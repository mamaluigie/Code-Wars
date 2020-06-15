dic = {'a':'1', 'e':'2', 'i':'3', 'o':'4', 'u':'5'}
def encode(st):
    
    new_string = st.replace('a', dic['a'])
    new_string = new_string.replace('e', dic['e'])
    new_string = new_string.replace('i', dic['i'])
    new_string = new_string.replace('o', dic['o'])
    new_string = new_string.replace('u', dic['u'])
    return new_string
    
def decode(st):
    new_string = st.replace(dic['a'], 'a')
    new_string = new_string.replace(dic['e'], 'e')
    new_string = new_string.replace(dic['i'], 'i')
    new_string = new_string.replace(dic['o'], 'o')
    new_string = new_string.replace(dic['u'], 'u')
    return new_string
