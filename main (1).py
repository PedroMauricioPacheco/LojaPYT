num_cracha = [] * 20
num_computador = [] * 20
cod_problema = [] * 20


def abrirchamado():
  num_cracha.append(int(input("numero do crachá:")))
  num_computador.append(int(input("numero do computador:")))
  cod_problema.append(int(input(" 1 - para computador não liga\n 2 - para computador lento\n 3 - para não consigo acessar internet:\n código do problema: ")))

def fecharchamado(x):
  posicao = num_computador.index(x)
  cod_problema[posicao] = 999

def listarchamados():
  index = cod_problema.index(999)
  print(num_cracha[-index],num_computador[-index],cod_problema[-index] )

  

def gerarestatistica():
  fechados = cod_problema.count(999)
  total = len(cod_problema)
  abertos = total - fechados
  porcentagem_abertos = abertos / total * 100
  print(porcentagem_abertos,"%")

while 1 > 0:

  print("Controle de chamados da TI\n 1 - Abrir Chamado\n 2 - Fechar Chamado\n 3 - Listar Chamados\n 4 - Gerar Estatística\n 5 - Sair")
  
  y = int(input("Qual Função deseja executar?"))
  
  if y == 1:
    abrirchamado()

  if y == 2:
    x = int(input("Qual o numero da máquina:"))
    fecharchamado(x)

  if y == 3:
    listarchamados()

  if y == 4:
    gerarestatistica()

  if y == 5:
    break