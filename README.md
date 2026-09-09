# cd-vyral-system

Sistema para gestão de leads, tarefas e acompanhamento de desempenho, construído com FastAPI.

## Funcionalidades
- Dashboard com métricas gerais
- Cadastro e consulta de leads
- Gestão de tarefas por status
- API REST pronta para extensão

## Requisitos
- Python 3.11+

## Como executar
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn src.main:app --reload
```

A API estará disponível em http://127.0.0.1:8000 e a documentação em http://127.0.0.1:8000/docs.
