## **Table of Contents**
- [E8 - Kenziegakure](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2b_e_02_kenziegakure.html&ref=master#mcetoc_1evd883pc0) 
- [Entrega](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2b_e_02_kenziegakure.html&ref=master#mcetoc_1esj4slvm0)
- [Estrutura de diretórios](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2b_e_02_kenziegakure.html&ref=master#mcetoc_1evd883pc1)
- [Kenziegakure - Etapa 1](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2b_e_02_kenziegakure.html&ref=master#mcetoc_1evd883pc0)
- [Kenziegakure - Etapa 2](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2b_e_02_kenziegakure.html&ref=master#mcetoc_1evd883pc0) 
- [Kenziegakure - Etapa 3](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2b_e_02_kenziegakure.html&ref=master#mcetoc_1evd883pc0) 
- [Entregáveis](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2b_e_02_kenziegakure.html&ref=master#mcetoc_1egvoav555j) 
  - [Repositório](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2b_e_02_kenziegakure.html&ref=master#mcetoc_1egvrpv6k1l4)
- [Critérios de aceitação](https://npepa32v9l.execute-api.us-east-1.amazonaws.com/v2/?project_id=19989138&filename=python/outubro-20/2b_e_02_kenziegakure.html&ref=master#mcetoc_1esj6ecle3)
# **E8 - Kenziegakure**
# **Entrega**
- Este é um projeto a ser desenvolvido em etapas.
- Estruture seus arquivos e diretórios seguindo o modelo da seção **Estrutura de diretórios**.
- Implemente as classes de acordo com as instruções.

**OBS:**

- ***Atenção:*** Os retornos em formato **string** devem ser **exatamente como o especificado ( atenção para os acentos e espaços )**

**Atençao -> Cada classe deverá estar em seu respectivo arquivo model, e todas as models devem estar no folder models, que por sua vez deverá estar dentro do folder src. Observe e crie atentamente o mesmo nome dos arquivos e diretórios demonstrados a seguir.**
# **Estrutura de diretórios**
Raiz

├── src

`     `├── \_\_init\_\_.py

`     `└── models

`         `├── \_\_init\_\_.py

`         `├── jounin\_model.py

`         `├── jutsu\_model.py

`         `└── ninja\_model.py

-----
# **Kenziegakure - Etapa 1**
Neste projeto, desenvolveremos as classes necessárias para montar uma estrutura sólida para o alvorecer dos ninjas da **vila da Kenzie** (e de outras vilas também) em um formato RPG simples. Hoje começaremos pela **classe Jutsu e classe Ninja**. Ao decorrer do projeto implementaremos algumas especificidades extras nestas classes, além de criar outras classes para relacionamento com elas.

Defina as seguinte classes, observando a chamada das instâncias (quando houver) de exemplo para interpretar quais atributos fazem parte do construtor e quais são diretamente inicializados pela classe.



**Classe** **Jutsu**

- **Atributo de classe:** 
  - jutsu\_ranks : Uma tupla de strings que recebe os possiveis ranks de um jutsu **( 'D', 'C', 'B', 'A', 'S',)**
- **Atributos de instância:** 
  - jutsu\_name : Uma **string** que recebe o nome do jutsu
  - jutsu\_type : Uma **string** que recebe o tipo elemental do jutsu
  - jutsu\_level : Uma **string** que recebe o level do jutsu, se o level passado não estiver compreendido em jutsu\_ranks, deverá então receber **'Unranked'** por padrão deverão ser consideradas **tanto letras maiúsculas como minúsculas** na comparação. **Exemplo**: 
    - A letra **Z** não entra no grupo jutsu\_ranks, logo o atributo seria inicializado como **'Unranked'**
    - A letra **a** entra no grupo jutsu\_ranks, mesmo sendo minúscula, mas a inicialização do atributo seria com a versão maiúscula **A**
  - jutsu\_damage : Um **inteiro** que recebe o dano do jutsu
  - chakra\_spend : Um **inteiro** **positivo** que recebe a quantidade de chakra gasta pelo jutsu. Se o inteiro passado for **negativo ou zero,** inicializar o atributo com o valor **100**

**Dica ninja:** Utilize o *magic method* **\_\_dict\_\_** para printar todos os atributos da instância e verificar se tudo foi criado corretamente  🐸 (Útil para testes)

\# Exemplo de criação de uma instância da classe Jutsu

rasengan = Jutsu('Rasengan', 'Vento', 'a', 20, -15)

print(rasengan.\_\_dict\_\_)

\>{

`        `'jutsu\_name': 'Rasengan', 

`        `'jutsu\_type': 'Vento', 

`        `'jutsu\_level': 'A', 

`        `'jutsu\_damage': 20, 

`        `'chakra\_spend': 100

}

- **Métodos** 
  - A classe não possui nenhum método



**Classe** **Ninja**

- **Atributos de instância:** 
  - name : Uma **string** que recebe o nome do ninja
  - clan : Uma **string** que recebe o clan do ninja
  - village : Uma **string** que recebe a vila do ninja
  - ninja\_level : Uma **string** que recebe o nivel do ninja. Atributo **opcional** no construtor, se não passada quando criada a instancia, deve receber o valor padrao **'Unranked'**
  - jutsu\_list : Uma **lista** que deverá ser inicializada como **vazia**
  - health\_pool : Um **inteiro** que deverá ser inicializado com o valor **100**
  - chakra\_pool : Um **inteiro** que deverá ser inicializado com o valor **100**
  - concious : Um **booleano** que deverá ser inicializado com o valor **True**

**Dica ninja:** Utilize o *magic method* **\_\_dict\_\_** para printar todos os atributos da instancia e verificar se tudo foi criado corretamente  🐸 (Útil para testes)

\# Exemplo de criação de instância da classe Ninja

naruto = Ninja('Naruto', 'Uzumaki', 'Konoha')

print(naruto.\_\_dict\_\_)

\> {

`        `'name': 'Naruto', 

`        `'ninja\_level': 'Unranked', 

`        `'clan': 'Uzumaki', 

`        `'village': 'Konoha', 

`        `'jutsu\_list': [], 

`        `'health\_pool': 100, 

`        `'chakra\_pool': 100, 

`        `'concious': True

}

- **Métodos de instância:** 
  - **learn\_jutsu(jutsu)** : 
    - **Parâmetros:** 
      - jutsu : Um objeto da classe **Jutsu**
    - **Procedimento:** 
      - O método learn\_jutsu deverá adicionar o parâmetro jutsu a jutsu\_list do ninja
    - **Retorno:** 
      - O método learn\_jutsu deverá retornar uma string **no exato formato** descrito no exemplo

\# Criação de uma instância da classe Jutsu

rasengan = Jutsu('Rasengan', 'Vento', 'a', 20, -15)

\# Criação de uma instância da classe Ninja

naruto = Ninja('Naruto', 'Uzumaki', 'Konoha')

#Chamada do método learn\_jutsu

res = naruto.learn\_jutsu(rasengan)

print(res)

\> 'O ninja Naruto Uzumaki acabou de aprender um novo jutsu: Rasengan'

-----
# **Kenziegakure - Etapa 2**
Agora que já criamos as classes **Ninja** e **Jutsu** na *etapa 1*, daremos continuidade ao nosso projeto adicionando uma nova classe chamada **Jounin** , que herdará as propriedades da classe **Ninja**. Siga as instruções descritas aqui para adicionar a **nova classe Jounin** ao arquivo **jounin\_model.py**.



**Classe** **Jounin**

A classe Jounin **herda** da classe Ninja, faça os imports corretamente e utilize o **método super** para ter acesso aos atributos da **classe pai** (Ninja)

- **Atributo de classe:** 
  - ninja\_level : Uma **string** que recebe o valor **Jounin**
- **Atributos de instância:** 
  - name : Uma **string** que recebe o nome do jounin
  - clan : Uma **string** que recebe o clan do jounin
  - village : Uma **string** que recebe a vila do jounin
  - proficiency : Um **dicionário** contendo a proeficiência do jounin nas 3 categorias de habilidade (**chaves**) : **taijutsu, ninjutsu e genjutsu ,** podendo estas conterem um **valor** numérico qualquer** cada (Observar o exemplo)
  - is\_in\_mission : Um **booleano** que deve ser inicializado como **False**

\# Exemplo de dicionário que será passado como proficiency

kakashi\_proficiency = {'taijutsu': 7, 'ninjutsu': 8, 'genjutsu': 4}

\# Criação de uma instância da classe Jounin

kakashi = Jounin('Kakashi', 'Hatake', 'Konoha', kakashi\_proficiency)

- **Métodos de instância:** 
  - **list\_best\_proficiency** : 
    - **Parâmetros:** 
      - Este método não recebe parâmetros na sua chamada
    - **Procedimento:** 
      - O método list\_best\_proficiency deve verificar qual a proficiência de **maior valor** do jounin (não se preocupe com empates) 
        - **Dica ninja:** Dê uma olhada na função *built-in* **max** 🐸
    - **Retorno:** 
      - O método list\_best\_proficiency deverá retornar uma string **no exato formato** descrito no exemplo

\# Exemplo utilizando o jounin Kakashi criado no exemplo anterior

res = kakashi.list\_best\_proficiency()

print(res)

\> 'Kakashi demonstra maior proficiência em ninjutsu'

- **start\_mission** : 
  - **Parâmetros:** 
    - Este método não recebe parâmetros na sua chamada
  - **Procedimento:** 
    - O método start\_mission deve verificar se o jounin está em missão (através do atributo is\_in\_mission). Caso **não esteja em missão**, mudar o atributo is\_in\_mission para **True** e retornar uma string no **exato formato** do exemplo. Caso **já esteja em missão**, somente retornar uma outra string no **exato formato** do exemplo
  - **Retorno:** 
    - O método start\_mission deverá retornar uma string **no exato formato** descrito no exemplo, dependendo do procedimento

\# Exemplo utilizando o jounin Kakashi criado no exemplo anterior

\# Se Kakashi JA ESTÁ em missão

res = kakashi.start\_mission()

print(res)

\> 'O ninja Kakashi Hatake já está em uma missão'

\# Se Kakashi NÃO ESTÁ em uma missão

res = kakashi.start\_mission()

print(res)

\> 'O ninja Kakashi Hatake saiu em missão'

- **return\_from\_mission** : 
  - **Parâmetros:** 
    - Este método não recebe parâmetros na sua chamada
  - **Procedimento:** 
    - O método return\_from\_mission deve verificar se o jounin está em missão (através do atributo is\_in\_mission). Caso **esteja em missão**, mudar o atributo is\_in\_mission para **False** e retornar uma string no **exato formato** do exemplo. Caso **não esteja** **em missão**, somente retornar uma outra string no **exato formato** do exemplo
  - **Retorno:** 
    - O método return\_from\_mission deverá retornar uma string **no exato formato** descrito no exemplo, dependendo do procedimento

\# Exemplo utilizando o jounin Kakashi criado no exemplo anterior

\# Se Kakashi NÃO ESTÁ em missão

res = kakashi.return\_from\_mission()

print(res)

\> 'O ninja Kakashi Hatake não está em nenhuma missão no momento'

\# Se Kakashi ESTÁ em uma missão

res = kakashi.return\_from\_mission()

print(res)

\> 'O ninja Kakashi Hatake retornou em segurança da missão'
# -----
# **Kenziegakure - Etapa 3**
Chegamos na reta final do nosso projeto, já desenvolvemos as classes **Jutsu**, **Ninja** e **Jounin** e alguns métodos para elas. Agora implementaremos mais **dois métodos** a nossa **classe Ninja,** um **estático** e um de **instância.**



**Classe** **Ninja**

Implemente mais **dois novos métodos** para a **classe Ninja**

- **Método estático (staticmethod):** 
  - **check\_health(ninja\_to\_check)** : 
    - **Parâmetros:** 
      - ninja\_to\_check : Um objeto da classe **Ninja**
    - **Procedimento:** 
      - O método check\_health deve verificar se a health\_pool do ninja passado por parâmetro é **menor que zero**. Caso **seja menor que zero**, deve alterar a health\_pool do ninja para **zero** e alterar o concious do ninja para **False**
    - **Retorno:** 
      - O método check\_health deverá retornar o concious do ninja passado por parâmetro
- **Método de instância:** 
  - **cast\_jutsu(jutsu, adversary)** : 
    - **Parâmetros:** 
      - jutsu : Um objeto da classe **Jutsu**
      - adversary : Um objeto da classe **Ninja**
    - **Procedimento:** 
      - O método cast\_jutsu deve:  
        - Verificar se o atributo concious do adversary é **True**. Caso **não for** , retornar **False imediatamente** 
          - ` `Caso concious do adversary seja **True**, fazer uma nova verificação para checar se o jutsu está na jutsu\_list da **instância que chamou o método** e se essa instância tem chakra suficiente na chakra\_pool para lançar o jutsu. Se essas duas condições forem verdadeiras, voce deve reduzir da health\_pool do adversary a quantidade de dano do jutsu e também reduzir da chakra\_pool da **instância que chamou o método** o **chakra gasto** pelo jutsu . Ao final desses processos, retornar **True** para sinalizar que o jutsu foi lançado
    - **Retorno:** 
      - Retornar um **booleano** representando se o jutsu **foi lançado ou não**, dependendo das condiçoes propostas no **Procedimento**

\# Criação de uma instância da classe Jutsu

rasengan = Jutsu('Rasengan', 'Vento', 'a', 20, -15)

\# Criação de uma instância da classe Ninja

naruto = Ninja('Naruto', 'Uzumaki', 'Konoha')

#Chamada do método learn\_jutsu

naruto.learn\_jutsu(rasengan)

\# Criação de uma outra instancia da classe Ninja

sasuke = Ninja('Sasuke', 'Uchiha', 'Konoha')

#Chamada do método cast\_jutsu

res = naruto.cast\_jutsu(rasengan, sasuke)

print(res)

\> True
## -----
# **Entregáveis**
## **Repositório**
- Link do **repositório** do **GitLab**
- **Código fonte:** 
  - arquivos com a mesma estrutura apresentada no inicio do projeto.
- **Privacidade** 
  - Incluir **ka-br-out-2020-correcoes** como reporter.
-----
# **Critérios de aceitação**

|**pts**|**Dado**|**Quando**|**É esperado**|
| :-: | :-: | :-: | :-: |
|1|Arvore de diretórios|Analisado os arquivos e nomeaçao|Que a estrutura de diretórios e nomeação de arquivo esteja de acordo com o proposto pela entrega|
|1|construtor da classe **Jutsu** |Executados os testes|**Todos os atributos** estejam sendo inicializados corretamente|
|1|construtor da classe **Ninja**|Executados os testes|**Todos os atributos** estejam sendo inicializados corretamente|
|1|método **learn\_jutsu**|Executados os testes|O método **adicione** corretamente um **jutsu** a **jutsu\_list** e retorne a **string** no **exato formato** citado no **Retorno**|
|1|construtor da classe **Jounin**|Executados os testes|**Todos os atributos** estejam sendo inicializados corretamente|
|1|método **list\_best\_proficiency**|Executados os testes|O método calcule qual a maior proficiencia baseado no **value** e retorne uma **string** no **exato formato** citado no **Retorno**|
|1|método **start\_mission**|Executados os testes|O método **verifica** se o jounin está em missão, e a partir disso retorna uma **string** no **exato formato** citado no **Retorno** , **dependendo do caso**|
|1|método **return\_from\_mission**|Executados os testes|O método **verifica** se o jounin está em missão, e a partir disso retorna uma **string** no **exato formato** citado no **Retorno** , **dependendo do caso**|
|1|método **check\_health**|Executados os testes|O método **verifica** a saúde do ninja e retorna um booleano de acordo com a saúde|
|1|método **cast\_jutsu**|Executados os testes|O método faz uma série de verificações e ao fim retorna um **booleano** sinalizando se o jutsu foi lançado ou não|


**Boa diversão Dev 🦊**






