from biblioteca import Livro
import pytest

# Testa se Livro é criado corretamente
def test_livro_criado():
    livro = Livro("Harry Potter")

    assert livro.titulo == "Harry Potter"
    assert livro.disponivel is True

# Testa se função de empréstimo altera estado corretamente
def test_livro_emprestado():
    livro = Livro("Narnia")
    livro.emprestar()

    assert livro.disponivel is False

# Testa se função de empréstimo funciona corretamente para livros indisponíveis
def test_livro_ja_emprestado():
    livro = Livro("Jogos Vorazes")
    livro.emprestar()

    with pytest.raises(Exception):
        livro.emprestar()

# Testa se função de devolução funciona corretamente
def test_devolucao_correta():
    livro = Livro("Percy Jackson")
    livro.emprestar()
    assert livro.disponivel is False

    livro.devolver()
    assert livro.disponivel is True