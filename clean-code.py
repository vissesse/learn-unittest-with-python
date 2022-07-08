### Variaveis ######
"""
Use nome de variaveis pronciaveis e significativas
"""

#import datetime
#current_date: str = datetime.date().today("%y-%m-%d")

"""
USE O MESMO VOCABULARIO PARA OS MESMO TIPO DE VARIAVEL
"""
def get_user_info(): pass
def get_user_data(): pass
def get_user_record(): pass

""" USE NOMES PESQUISAVEIS
""" 

fullname = "Carlos Vissesse"
def split_into_first_and_last_name()-> None:
    global fullname
    fullname = fullname.split()
    
split_into_first_and_last_name()

"""
EVITE EFEITOS COLATERAIS
"""
from dataclasses import dataclass
from typing import Text

@dataclass
class Person:
    name: Text
    
    @property
    def fullname(self, other="No one"):
        return self.name.split()
    
    
    def onter(self, outro ='carlos'):
        return outro
    
    #A razão pelo qual criamos instancia da classe é para 

pessoa = Person("Carlos Vissesse")
print(pessoa.onter())
