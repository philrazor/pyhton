def annotations(arg1 : str , agr2 : str = 'eggs') -> str:
    print('annotations are: '  ,annotations.__annotations__)
    print(f'argument required:{arg1}' ,f'argument keyword:{agr2}')

annotations('first argument') 

def integer(num1 : int , num2 : int = 2)-> int:
    print('annotations are:' ,integer.__annotations__)
    print(int(num1 + num2))
    
integer(1)    