"""
storage.py
----------
Responsável por persistir as tarefas em um arquivo JSON.

Separar persistência (storage) da regra de negócio (task_service)
deixa o projeto mais organizado e fácil de testar.
"""

import json
from pathlib import Path


def ler_json(caminho_arquivo: str):
    """
    Lê um arquivo JSON e retorna os dados como objeto Python.
    Se não existir ou estiver vazio, retorna lista vazia.
    """
    path = Path(caminho_arquivo)

    if not path.exists():
        return []

    conteudo = path.read_text(encoding="utf-8").strip()
    if not conteudo:
        return []

    return json.loads(conteudo)


def salvar_json(caminho_arquivo: str, dados):
    """
    Escreve 'dados' em JSON, formatado, no arquivo.
    """
    path = Path(caminho_arquivo)
    path.parent.mkdir(parents=True, exist_ok=True)

    texto = json.dumps(dados, ensure_ascii=False, indent=2)
    path.write_text(texto, encoding="utf-8")
