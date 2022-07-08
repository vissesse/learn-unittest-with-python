APLICAÇÃO DE ALERTA DE STOCK


INFORMATION:
    A aplicação vai escutar as actualizações do stoke dem uma fonte.
    A fonte pode ser qualquer coisa-- um servidor na internet, um 
    arquivo no disco duro, ou qualquer coisa. Estaremos capacitados
    para definir regras, e quando as regras forem atingidias, a aplicação
    mandará uma menssagem ou um email.

    por exemplo:

    Podemos definir um regra 'caso a aplicação cruse a $550 nivel então mande-me 
    um email'. Uma vez definida, a aplicação vai monitorar as actualizações e 
    manar um email quando a regra for atingida


Definição de modulos:

    * Alguma maneira de ler os precos actulizados do stoque, vindo da internet ou
    d eum arquivo.

    * Alguma meira de manipular a informação e processar elas

    * Uma maniera de definir regras e atingir elas apartir da actual informação 
    do stoque

    * alguma maneira de enciar uma sms ou email
    quando aregra for atingida


Update_method:
    * deve receber a data e o preco no parametro e setar no objecto
    * o preco não pode ser negativo 
    * depois de multiplas actualização deve retorna o ultimo preco


Guiar de como pensar como developer test brinlhante:
  * Se em todas as possibilidade, não devolver  o uso do detalhes na implementação do test,
  e apenas usar cilco publico da interdace esposta. Iso inclui unsando apenas metotod da interface
  no metodo setUp e no metodo assertions

  * caso o teste precisar verificar funcionalidade q são internas da unidade sendo testada,e esta
  seja uma funcinalidade importante, então faz sentido verificar as acções da implementações

  * Se 

  https://www.youtube.com/watch?v=t7vQF0ynF9g