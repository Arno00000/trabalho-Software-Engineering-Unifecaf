"""
task_service.py
---------------
Aqui está a lógica principal do sistema (CRUD + validações).

Funções principais:
- criar_task (CREATE)
- listar_tasks (READ)
- obter_task_por_id (READ por ID)
- atualizar_task (UPDATE)
- excluir_task (DELETE)

Mudança de escopo:
- adicionar prioridade e permitir filtro por prioridade
"""

from typing import List, Dict, Optional
from .storage import ler_json, salvar_json
from .models import (
    STATUS_VALIDOS,
    STATUS_A_FAZER,
    PRIORIDADES_VALIDAS,
    PRIORIDADE_MEDIA,
)


def _proximo_id(tasks: List[Dict]) -> int:
    """
    Retorna o próximo ID disponível (auto-incremento).
    """
    if not tasks:
        return 1
    return max(t["id"] for t in tasks) + 1


def carregar_tasks(caminho_db: str) -> List[Dict]:
    """
    Carrega tarefas do arquivo JSON.
    """
    return ler_json(caminho_db)


def salvar_tasks(caminho_db: str, tasks: List[Dict]) -> None:
    """
    Salva tarefas no arquivo JSON.
    """
    salvar_json(caminho_db, tasks)


def criar_task(caminho_db: str, titulo: str, descricao: str = "") -> Dict:
    """
    CREATE: cria uma tarefa com status padrão "A Fazer"
    e prioridade padrão "MEDIA" (mudança de escopo).
    """
    titulo = (titulo or "").strip()
    if not titulo:
        raise ValueError("O título é obrigatório.")

    tasks = carregar_tasks(caminho_db)

    nova = {
        "id": _proximo_id(tasks),
        "titulo": titulo,
        "descricao": (descricao or "").strip(),
        "status": STATUS_A_FAZER,
        "prioridade": PRIORIDADE_MEDIA,
    }

    tasks.append(nova)
    salvar_tasks(caminho_db, tasks)
    return nova


def listar_tasks(
    caminho_db: str,
    status: Optional[str] = None,
    prioridade: Optional[str] = None
) -> List[Dict]:
    """
    READ: lista tarefas.
    Permite filtro por status e/ou prioridade.
    """
    tasks = carregar_tasks(caminho_db)

    # Filtra por status
    if status:
        if status not in STATUS_VALIDOS:
            raise ValueError(f"Status inválido. Use: {STATUS_VALIDOS}")
        tasks = [t for t in tasks if t["status"] == status]

    # Filtra por prioridade
    if prioridade:
        prioridade = prioridade.upper()
        if prioridade not in PRIORIDADES_VALIDAS:
            raise ValueError(f"Prioridade inválida. Use: {PRIORIDADES_VALIDAS}")
        tasks = [t for t in tasks if t["prioridade"] == prioridade]

    return tasks


def obter_task_por_id(caminho_db: str, task_id: int) -> Dict:
    """
    READ por ID: retorna uma tarefa específica.
    """
    tasks = carregar_tasks(caminho_db)
    for t in tasks:
        if t["id"] == task_id:
            return t
    raise KeyError("Tarefa não encontrada.")


def atualizar_task(
    caminho_db: str,
    task_id: int,
    titulo: Optional[str] = None,
    descricao: Optional[str] = None,
    status: Optional[str] = None,
    prioridade: Optional[str] = None
) -> Dict:
    """
    UPDATE: atualiza campos de uma tarefa.
    """
    tasks = carregar_tasks(caminho_db)

    # Busca a tarefa
    task = None
    for t in tasks:
        if t["id"] == task_id:
            task = t
            break

    if not task:
        raise KeyError("Tarefa não encontrada.")

    # Atualiza título
    if titulo is not None:
        titulo = titulo.strip()
        if not titulo:
            raise ValueError("O título não pode ficar vazio.")
        task["titulo"] = titulo

    # Atualiza descrição
    if descricao is not None:
        task["descricao"] = descricao.strip()

    # Atualiza status
    if status is not None:
        if status not in STATUS_VALIDOS:
            raise ValueError(f"Status inválido. Use: {STATUS_VALIDOS}")
        task["status"] = status

    # Atualiza prioridade
    if prioridade is not None:
        prioridade = prioridade.upper()
        if prioridade not in PRIORIDADES_VALIDAS:
            raise ValueError(f"Prioridade inválida. Use: {PRIORIDADES_VALIDAS}")
        task["prioridade"] = prioridade

    salvar_tasks(caminho_db, tasks)
    return task


def excluir_task(caminho_db: str, task_id: int) -> bool:
    """
    DELETE: remove tarefa pelo ID.
    Retorna True se removeu, False se não encontrou.
    """
    tasks = carregar_tasks(caminho_db)
    antes = len(tasks)

    tasks = [t for t in tasks if t["id"] != task_id]

    if len(tasks) == antes:
        return False

    salvar_tasks(caminho_db, tasks)
    return True


# Validação simples para manter o quadro organizado: título não pode ser vazio.
