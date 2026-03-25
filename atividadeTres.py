#questao 1
logs = [
    "2023-10-01 10:00:00 INFO User 105 logged in",
    "2023-10-01 10:05:23 ERROR Database connection failed",
    "2023-10-01 10:07:00 INFO User 105 requested /home",
    "2023-10-01 10:15:00 WARNING Memory usage above 80%",
    "2023-10-01 10:20:00 ERROR Timeout on API gateway",
    "2023-10-01 10:22:00 INFO User 202 logged in"
]

def analisar_logs(lista_logs):
    contagem = {}
    for entrada in lista_logs:
    
        partes = entrada.split()
        severidade = partes[2]
    
        contagem[severidade] = contagem.get(severidade, 0) + 1
    
    return contagem

print(analisar_logs(logs))


#questao 2
transacoes = [
    (1, "Infraestrutura", 1500.50),
    (2, "Licenças", 450.00),
    (3, "Infraestrutura", 3200.00),
    (4, "Marketing", 800.00),
    (5, "Licenças", 150.00)
]

categorias_unicas = {t[1] for t in transacoes}
print(f"Categorias: {categorias_unicas}")

resumo = {}
for _, categoria, valor in transacoes:
    resumo[categoria] = resumo.get(categoria, 0) + valor

print(f"Gasto por categoria: {resumo}")



#questao 3 
class Usuario:
    def __init__(self, id_user, nome, email):
        self.__id = id_user
        self.__nome = nome
        self.email = email 

    @property
    def id(self): return self.__id

    @property
    def nome(self): return self.__nome

    @property
    def email(self): return self.__email

    @email.setter
    def email(self, valor):
        if "@" in valor:
            self.__email = valor
        else:
            print("Erro: E-mail inválido")
            self.__email = None

class GerenciadorUsuarios:
    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def remover_usuario_por_id(self, id_busca):
        self.usuarios = [u for u in self.usuarios if u.id != id_busca]

    def listar_usuarios(self):
        for u in self.usuarios:
            print(f"ID: {u.id} | Nome: {u.nome} | Email: {u.email}")



#questao 4
class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [[" " for _ in range(3)] for _ in range(3)]
        self.turno = "X"

    def mostrar_tabuleiro(self):
        print("\n  0 1 2")
        for i, linha in enumerate(self.tabuleiro):
            print(f"{i} {'|'.join(linha)}")
            if i < 2: print("  -----")

    def fazer_jogada(self, linha, col):
        if 0 <= linha < 3 and 0 <= col < 3 and self.tabuleiro[linha][col] == " ":
            self.tabuleiro[linha][col] = self.turno
            self.turno = "O" if self.turno == "X" else "X"
            return True
        print("Jogada inválida!")
        return False

    def verificar_vencedor(self):
        t = self.tabuleiro
        vitorias = (
            t[0], t[1], t[2],
            [t[0][0], t[1][0], t[2][0]],
            [t[0][1], t[1][1], t[2][1]],
            [t[0][2], t[1][2], t[2][2]],
            [t[0][0], t[1][1], t[2][2]],
            [t[0][2], t[1][1], t[2][0]]
        )

        for v in vitorias:
            if v[0] == v[1] == v[2] != " ":
                return v[0]
        return None

    def verificar_empate(self):
        for linha in self.tabuleiro:
            if " " in linha:
                return False
        return True

    def jogar(self):
        while True:
            self.mostrar_tabuleiro()
            print(f"Vez do jogador: {self.turno}")
            try:
                l = int(input("Linha: "))
                c = int(input("Coluna: "))

                if self.fazer_jogada(l, c):

                    vencedor = self.verificar_vencedor()

                    if vencedor:
                        self.mostrar_tabuleiro()
                        print(f"Parabéns! {vencedor} venceu!")
                        break

                    if self.verificar_empate():
                        self.mostrar_tabuleiro()
                        print("Empate!")
                        break

            except ValueError:
                print("Digite números válidos!")
