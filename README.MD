TechFlow Task Manager

Projeto acadêmico desenvolvido para simular a criação e gestão de um **sistema de gerenciamento de tarefas**, aplicando conceitos de **Engenharia de Software**, **Metodologias Ágeis**, **versionamento com Git/GitHub**, **testes automatizados** e **integração contínua**.

O projeto representa uma solução simples para uma empresa fictícia chamada **TechFlow Solutions**, contratada por uma startup do setor de logística.

---
1. Objetivo do Projeto
Desenvolver um sistema básico que permita:
- Criar, listar, atualizar e excluir tarefas (CRUD)
- Acompanhar o status das tarefas em um fluxo ágil
- Simular a organização do trabalho usando Kanban
- Aplicar boas práticas de versionamento, testes e CI

---

2. Escopo Inicial
No início do projeto, o sistema contemplava:
- Cadastro de tarefas com título e descrição
- Status da tarefa:
  - A Fazer  
  - Em Progresso  
  - Concluído
- Persistência simples em arquivo JSON
- Execução via terminal (CLI)
- Testes automatizados com Pytest
- Pipeline de integração contínua com GitHub Actions

---

3. Mudança de Escopo
Durante o desenvolvimento, foi simulada uma **mudança de escopo**, comum em projetos ágeis.

 Alteração realizada:
- Inclusão do campo **prioridade** na tarefa:
  - BAIXA
  - MEDIA
  - ALTA
- Possibilidade de **filtrar tarefas críticas** por prioridade

 Justificativa:
Em sistemas logísticos, algumas tarefas possuem impacto maior no negócio. A priorização permite melhor tomada de decisão e foco nas atividades mais importantes.

---

 4. Metodologia Ágil Utilizada
Foi adotado o **Kanban**, utilizando o **GitHub Projects**, com as colunas:
- A Fazer
- Em Progresso
- Concluído

As tarefas foram organizadas em cards e movimentadas conforme a evolução do projeto.

---

 5. Estrutura do Projeto

techflow-task-manager/
├── src/ # Código-fonte
│ ├── cli.py # Interface de linha de comando
│ ├── task_service.py
│ ├── storage.py
│ ├── models.py
│ └── init.py
├── tests/ # Testes automatizados
├── data/ # Arquivo JSON das tarefas
├── docs/uml/ # Diagramas UML
├── .github/workflows # GitHub Actions (CI)
├── requirements.txt
├── pytest.ini
└── README.md

 6. Tecnologias Utilizadas
- **Python 3.12**
- **Git e GitHub**
- **Pytest** (testes automatizados)
- **GitHub Actions** (integração contínua)
- **PlantUML** (diagramas UML)

---

 7. Como Executar o Projeto

 7.1 Criar ambiente virtual
```bash
python -m venv .venv

 7.2 Criar ambiente virtual
Windows (CMD):
.venv\Scripts\activate.bat

7.3 Instalar dependências
python -m pip install -r requirements.txt

7.4 Executar os testes
python -m pytest -q

8. Utilizando o Sistema (CLI)
Criar tarefa
python -m src.cli criar "Título da tarefa" "Descrição opcional"

Listar tarefas
python -m src.cli listar

Atualizar tarefa
python -m src.cli atualizar 1 --status "Concluído" --prioridade ALTA

Filtrar tarefas críticas
python -m src.cli listar --prioridade ALTA

Excluir tarefa
python -m src.cli excluir 1


9. Controle de Qualidade

O projeto utiliza GitHub Actions para:

Instalar dependências

Executar os testes automatizados a cada push ou pull request

Isso garante maior confiabilidade e evita regressões no código.

10. Diagramas UML

Os diagramas solicitados na atividade estão disponíveis na pasta:

docs/uml/

Diagrama de Casos de Uso
Diagrama de Classes

11. Histórico de Commits

O desenvolvimento foi registrado com commits frequentes e descritivos, permitindo acompanhar a evolução do projeto e as decisões tomadas ao longo do processo.

12. Observações Finais

Este projeto tem finalidade exclusivamente acadêmica, com foco na aplicação prática dos conceitos de Engenharia de Software, metodologias ágeis, testes automatizados e controle de versão.

Evidencia de execucao do CI com GitHub Actions.
