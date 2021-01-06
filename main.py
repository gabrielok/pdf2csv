import tabula, csv
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
    # reconstroi a tabela no caso de a coluna "código" ser lida junto à seguinte
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
    df.drop(columns = q32[0].columns[-1], inplace = True) # apagar a última coluna

# Quadro 30
q30 = tabula.read_pdf(filename, pages = 79, area = [16, 22, 26, 58], relative_area = True, silent = True, stream = True)
print('QUADRO 30')
print(q30[0])

with open('q30.csv', 'w') as f:
    writecsv(f, q30[0])

# Quadro 31
q31_1 = tabula.read_pdf(filename, pages = 79, area = [74, 22, 88, 84], relative_area = True, silent = True, stream = True)
cols = q31_1[0].columns
q31_1[0].rename(columns = {q31_1[0].columns[0]: q31_1[0].at[0,cols[0]], q31_1[0].columns[1]: q31_1[0].at[0,cols[1]]}, inplace = True)
q31_1[0].drop(0, inplace = True)
print('QUADRO 31')
print(q31_1[0])

# Quadro 32
q32 = tabula.read_pdf(filename, pages = 85, area = [15, 22, 24, 53], relative_area = True, silent = True, stream = True)
print('QUADRO 32')
print(q32[0])

parse1(q32[0])

with open('q32.csv', 'w') as f:
    writecsv(f, q32[0])
