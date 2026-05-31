class Livro:
    def __init__(self, titulo):
        self.titulo = titulo
        self.disponivel = True
    
    def emprestar(self):
        if not self.disponivel:
            raise Exception("Livro indisponível")
        
        self.disponivel = False
    
    def devolver(self):
        if self.disponivel:
            raise Exception("Este livro já foi retornado")
        
        self.disponivel = True
