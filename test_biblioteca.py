from biblioteca import Livro
import pytest

def test_livro_criado():
    livro = Livro("Harry Potter")

    assert livro.titulo == "Harry Potter"
    assert livro.disponivel is True

def test_livro_emprestado():
    livro = Livro("Narnia")
    livro.emprestar()

    assert livro.disponivel is False

def test_livro_ja_emprestado():
    livro = Livro("Jogos Vorazes")
    livro.emprestar()

    with pytest.raises(Exception):
        livro.emprestar()

def test_devolucao_correta():
    livro = Livro("Percy Jackson")
    livro.emprestar()
    assert livro.disponivel is False

    livro.devolver()
    assert livro.disponivel is True