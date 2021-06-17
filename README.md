# Numbers

A partir de qualquer número inteiro, você saberá se ele é primo, ímpar, qual a raiz quadrada, número binário, octal, antecessor e sucessor!

Método | Rota |	Descrição |
-----| ------- | --------- |
GET |`/numbers/:number` |	Consulta informações sobre um número inteiro.
GET |`/numbers/consts` |	Informações de algumas constantes matemáticas registradas.


## Estrutura da resposta

`/numbers/7901`

```python
{"id": 7901,
"proximo": 7902,
"anterior": 7900,
"impar": true,
"primo": true,
"raiz": 88.88756943465155,
"binario": "1111011011101",
"octal": "17335"}
```

## Executando o projeto
Instale as dependências:
```python
pip install -r requirements.txt
```
Coloque a aplicação no ar:
```python
uvicorn main:app --reload
```
