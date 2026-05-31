class Livro:
    # Construtor da classe Livro
    def __init__(self, titulo):
        self.titulo = titulo
        self.disponivel = True
    
    # Função emprestar
    def emprestar(self):
        if not self.disponivel:
            raise Exception("Livro indisponível") # Gera erro se livro estiver indisponível
        
        self.disponivel = False #Indisponibiliza livro emprestado
    
    def devolver(self):
         #Gera erro se o livro já estiver disponível para evitar redundâncias
        if self.disponivel:
            raise Exception("Este livro já foi retornado")
        
        #Disponibiliza livro
        self.disponivel = True
