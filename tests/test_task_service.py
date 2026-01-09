"""
Testes automatizados do CRUD.
Usa arquivo temporário para não mexer no data/tasks.json real.
"""

import os
import tempfile
import pytest

from src.task_service import criar_task, listar_tasks, atualizar_task, excluir_task


@pytest.fixture()
def db_temp():
    # Cria arquivo temporário
    fd, caminho = tempfile.mkstemp(suffix=".json")
    os.close(fd)

    # Inicializa vazio
    with open(caminho, "w", encoding="utf-8") as f:
        f.write("[]")

    yield caminho

    # Remove ao final
    os.remove(caminho)


def test_criar_task_exige_titulo(db_temp):
    with pytest.raises(ValueError):
        criar_task(db_temp, "")


def test_fluxo_crud_com_prioridade(db_temp):
    # CREATE
    t1 = criar_task(db_temp, "Tarefa 1", "Desc 1")
    assert t1["id"] == 1
    assert t1["prioridade"] == "MEDIA"

    # READ
    tasks = listar_tasks(db_temp)
    assert len(tasks) == 1

    # UPDATE
    t1_att = atualizar_task(db_temp, 1, status="Concluído", prioridade="ALTA")
    assert t1_att["status"] == "Concluído"
    assert t1_att["prioridade"] == "ALTA"

    # FILTER
    altas = listar_tasks(db_temp, prioridade="ALTA")
    assert len(altas) == 1

    # DELETE
    ok = excluir_task(db_temp, 1)
    assert ok is True

    # LIST vazio
    tasks2 = listar_tasks(db_temp)
    assert len(tasks2) == 0
