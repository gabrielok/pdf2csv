import tabula
filename = 'Componente Organizacional 12.2020.pdf'

# Quadro 30
q30 = tabula.read_pdf(filename, pages = 79, area = [16, 22, 26, 58], relative_area = True, silent = True, stream = True)
print('QUADRO 30')
print(q30[0])

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
