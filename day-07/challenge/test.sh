#!/bin/bash

#!/bin/bash

# Criar a primeira tarefa
echo "Criando a primeira tarefa..."
curl -X POST "http://localhost:8000/tasks" -H "Content-Type: application/json" -d '{"title": "Estudar Docker", "description": "Estudar como criar e usar containers Docker"}'
echo -e "\n"

# Criar a segunda tarefa
echo "Criando a segunda tarefa..."
curl -X POST "http://localhost:8000/tasks" -H "Content-Type: application/json" -d '{"title": "Estudar FastAPI", "description": "Estudar como criar APIs com FastAPI"}'
echo -e "\n"

# Listar todas as tarefas
echo "Listando todas as tarefas..."
curl -X GET "http://localhost:8000/tasks"
echo -e "\n"

# Obter a primeira tarefa
echo "Obtendo a primeira tarefa..."
curl -X GET "http://localhost:8000/tasks/1"
echo -e "\n"

# Atualizar a primeira tarefa
echo "Atualizando a primeira tarefa..."
curl -X PUT "http://localhost:8000/tasks/1" -H "Content-Type: application/json" -d '{"title": "Estudar Docker Avançado", "description": "Estudar como criar e gerenciar clusters Docker"}'
echo -e "\n"

# Listar todas as tarefas após atualização
echo "Listando todas as tarefas após atualização..."
curl -X GET "http://localhost:8000/tasks"
echo -e "\n"

# Deletar a primeira tarefa
echo "Deletando a primeira tarefa..."
curl -X DELETE "http://localhost:8000/tasks/1"
echo -e "\n"

# Listar todas as tarefas após exclusão
echo "Listando todas as tarefas após exclusão da primeira tarefa..."
curl -X GET "http://localhost:8000/tasks"
echo -e "\n"

# Obter a segunda tarefa para conferir se ainda existe
echo "Obtendo a segunda tarefa..."
curl -X GET "http://localhost:8000/tasks/2"
echo -e "\n"
