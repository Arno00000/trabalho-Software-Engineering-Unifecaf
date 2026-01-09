"""
models.py
---------
Constantes e regras básicas do sistema.

Mantemos aqui:
- Status válidos do Kanban
- Prioridades válidas (mudança de escopo)
"""

# Status do fluxo (equivalente às colunas do Kanban)
STATUS_A_FAZER = "A Fazer"
STATUS_EM_PROGRESSO = "Em Progresso"
STATUS_CONCLUIDO = "Concluído"

STATUS_VALIDOS = [STATUS_A_FAZER, STATUS_EM_PROGRESSO, STATUS_CONCLUIDO]

# Prioridade (mudança de escopo)
PRIORIDADE_BAIXA = "BAIXA"
PRIORIDADE_MEDIA = "MEDIA"
PRIORIDADE_ALTA = "ALTA"

PRIORIDADES_VALIDAS = [PRIORIDADE_BAIXA, PRIORIDADE_MEDIA, PRIORIDADE_ALTA]

# Nota: mantenha os textos dos status exatamente iguais para combinar com o Kanban.
