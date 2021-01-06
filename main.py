import tabula, csv, zipfile
filename = 'Componente Organizacional 12.2020.pdf'

def writecsv(file, df):
    writer = csv.writer(file, delimiter=';', quotechar='"', lineterminator='\n')
    header = [df.columns[0], df.columns[1]]
    writer.writerow(header)
    writer.writerows(df.values)
    return

def readcsv(file):
    reader = csv.reader(file, delimiter=';', quotechar='"')
    for row in reader:
        print(row)

def parse1(df):
    # reconstrói a tabela no caso de a coluna "código" ser lida junto à seguinte
    # e os cabeçalhos serem interpretados como dados
    newcols = [[],[]]
    for idx, row in enumerate(df.values):
        # separar as colunas
        sp = row[0].split()
        newcols[0].append(sp[0])
        newcols[1].append(' '.join(sp[1:]))

    headers = []
    for col in newcols:
        # separar os cabeçalhos
        headers.append(col.pop(0))
        col.append('NaN')

    for idx, col in enumerate(newcols):
        # inserir as novas colunas
        df.insert(idx, headers[idx], newcols[idx], True)

    nrows = df.shape[0]
    df.drop(nrows - 1, inplace = True) # apagar a última linha
    df.drop(columns = df.columns[-1], inplace = True) # apagar a última coluna

def parse2(df):
    # reconstrói a tabela no caso de os cabeçalhos serem interpretados como dados
    cols = df.columns
    df.rename(columns = {df.columns[0]: df.iloc[0,0], df.columns[1]: df.iloc[0,1]}, inplace = True)
    df.drop(0, inplace = True)
    return

def parse3(df):
    # reconstrói a tabela no caso de algumas linhas serem duplas
    nuls = df.isnull()
    nrows = df.shape[0]
    i = 0
    while i < nrows:
        if nuls.iloc[i, 1]:
            df.iloc[i-1, 0] = df.iloc[i, 0]
            df.iloc[i-1, 1] = df.iloc[i-1, 1] + ' ' + df.iloc[i+1, 1]
            df.drop(i, inplace = True)
            df.drop(i+1, inplace = True)
            df.reset_index(drop = True, inplace = True)
            nuls.drop(i, inplace = True)
            nuls.drop(i+1, inplace = True)
            nuls.reset_index(drop = True, inplace = True)
            nrows = nrows - 2
        i = i + 1

def append_dfs(df1, df2):
    df2.columns = df1.columns
    df1 = df1.append(df2)
    df1.reset_index(inplace = True, drop = True)
    return df1

# Quadro 30
q30 = tabula.read_pdf(filename, pages = 79, area = [16, 22, 26, 58], relative_area = True, silent = True, stream = True)
print('QUADRO 30')
print(q30[0])
with open('q30.csv', 'w') as f:
    writecsv(f, q30[0])

# Quadro 31
# ler cada página isoladamente
q31_1 = tabula.read_pdf(filename, pages = 79, area = [74, 22, 88, 84], relative_area = True, silent = True, stream = True)
parse2(q31_1[0])

q31_2 = tabula.read_pdf(filename, pages = '80-84',  silent = True, stream = True, pandas_options = {'columns': ['A', 'B']})
for df in q31_2:
    if df.isnull().values.any():
        parse3(df)

for df in q31_2:
    # juntar as páginas
    q31_1[0] = append_dfs(q31_1[0], df)
    q31_1[0]
q31 = q31_1[0]

print('QUADRO 31')
print(q31.to_string())
with open('q31.csv', 'w') as f:
    writecsv(f, q31)

# Quadro 32
q32 = tabula.read_pdf(filename, pages = 85, area = [15, 22, 24, 53], relative_area = True, silent = True, stream = True)
parse1(q32[0])
print('QUADRO 32')
print(q32[0])
with open('q32.csv', 'w') as f:
    writecsv(f, q32[0])

# Zip dos arquivos
filename = 'Teste_Intuitive_Care_Gabriel_Okamoto.zip'
with zipfile.ZipFile(filename, 'w') as file:
    file.write('q30.csv')
    file.write('q31.csv')
    file.write('q32.csv')
