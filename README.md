Teste 2 - pdf para csv

Lógica do programa:
1. Extrai as tabelas do pdf através da biblioteca tabula, utilizando a posição na tela quando necessário
2. Corrige as tabelas no caso de serem mal interpretadas
3. Salva uma por uma no formato .csv
4. Compacta todos os .csv em um arquivo .zip

Devido à grande quantidade de erros ao ler as tabelas do pdf (possivelmente devido a formatação inconsistente), elaborei uma coleção de funções _parse_ para padronizar a saída antes de exportar os dados. Caso mais quadros precisem ser extraídos no futuro, é possível reutilizar essas funções.

Próximos passos:
1. Converter os dados em float para int
2. Obter automaticamente as coordenadas de tabelas no pdf para usar como argumento na leitura
3. Obter automaticamente a quantidade de arquivos a serem zipados e seus nomes

Referências:
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html
https://nbviewer.jupyter.org/github/chezou/tabula-py/blob/master/examples/tabula_example.ipynb
https://tabula-py.readthedocs.io/en/latest/tabula.html
