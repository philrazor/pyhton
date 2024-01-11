# passing a whole dictionary as an argument
def football(player , positon = 'striker'  , action  = 'shoot'):
    print(f'--peolpe ask about {player} and i tell them he\'s the goat ')
    print(f'if you put {player} in {positon} he\'s deadly')
    print(f"when he {action} with his left foot he\'s if unstoppable")

dictionary_arg = {'player': 'messi' , 'positon' : 'RW , CF' ,'action':'shoots ,finesse'}

football(**dictionary_arg)

# testing passing multiple arguments
players = ['messi','ronaldo' ,'salah']
def footballers(*players):
    print("palyers are :" ,players)

footballers(*players)    


