"""
cli.py
------
Interface de terminal (CLI) para utilizar o sistema.

Comandos:
- criar
- listar
- ver
- atualizar
- excluir

Exemplos:
python -m src.cli criar "Título" "Descrição"
python -m src.cli listar
python -m src.cli atualizar 1 --status "Concluído" --prioridade ALTA
"""

import argparse
from .task_service import (
    criar_task,
    listar_tasks,
    obter_task_por_id,
    atualizar_task,
    excluir_task
)

# Caminho do "banco" JSON
CAMINHO_DB = "data/tasks.json"


def print_tasks(tasks):
    """
    Exibe tarefas em um formato fácil de ler no terminal.
    """
    if not tasks:
        print("Nenhuma tarefa encontrada.")
        return

    for t in tasks:
        print(f"[{t['id']}] {t['titulo']} | {t['status']} | Prioridade: {t['prioridade']}")
        if t["descricao"]:
            print(f"    - {t['descricao']}")


def main():
    parser = argparse.ArgumentParser(prog="TechFlow Task Manager (CLI)")
    sub = parser.add_subparsers(dest="comando", required=True)

    # criar
    p_criar = sub.add_parser("criar", help="Cria uma nova tarefa")
    p_criar.add_argument("titulo", help="Título da tarefa")
    p_criar.add_argument("descricao", nargs="?", default="", help="Descrição (opcional)")

    # listar
    p_listar = sub.add_parser("listar", help="Lista tarefas")
    p_listar.add_argument("--status", default=None, help='Filtra por status: "A Fazer", "Em Progresso", "Concluído"')
    p_listar.add_argument("--prioridade", default=None, help="Filtra por prioridade: BAIXA/MEDIA/ALTA")

    # ver
    p_ver = sub.add_parser("ver", help="Mostra uma tarefa por ID")
    p_ver.add_argument("id", type=int)

    # atualizar
    p_att = sub.add_parser("atualizar", help="Atualiza campos de uma tarefa")
    p_att.add_argument("id", type=int)
    p_att.add_argument("--titulo", default=None)
    p_att.add_argument("--descricao", default=None)
    p_att.add_argument("--status", default=None)
    p_att.add_argument("--prioridade", default=None)

    # excluir
    p_exc = sub.add_parser("excluir", help="Exclui uma tarefa")
    p_exc.add_argument("id", type=int)

    args = parser.parse_args()

    if args.comando == "criar":
        t = criar_task(CAMINHO_DB, args.titulo, args.descricao)
        print("Tarefa criada:")
        print_tasks([t])

    elif args.comando == "listar":
        tasks = listar_tasks(CAMINHO_DB, status=args.status, prioridade=args.prioridade)
        print_tasks(tasks)

    elif args.comando == "ver":
        t = obter_task_por_id(CAMINHO_DB, args.id)
        print_tasks([t])

    elif args.comando == "atualizar":
        t = atualizar_task(
            CAMINHO_DB,
            args.id,
            titulo=args.titulo,
            descricao=args.descricao,
            status=args.status,
            prioridade=args.prioridade
        )
        print("Tarefa atualizada:")
        print_tasks([t])

    elif args.comando == "excluir":
        ok = excluir_task(CAMINHO_DB, args.id)
        print("Tarefa excluída." if ok else "Tarefa não encontrada.")


if __name__ == "__main__":
    main()



    # Parser dos comandos do terminal (CLI) e chamada do serviço.
