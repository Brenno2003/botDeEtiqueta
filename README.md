Tem que ter o BarTender Designer

Primeiro passo: Colocar o caminho até o seu arquivo, workbook = openpyxl.load_workbook(r'caminho do arquivo')

O bot pega o cod, nome e valor do produto:

cod = sheet['C']
produto = sheet['B']    
valor = sheet['D']
Na sua planilha pode ser colunas diferentes, então altere se precisar

for i in range(x, y): 
x = O número da linha do seu primeiro produto
y = O número da linha do seu último item

Importante:
Crie uma pasta para as etiquetas
Antes de começar a rodar o bot deixe a pasta das etiquetas berta, e como segunda opção na aba do alt + tab
Antnes de comerçar a rodar o bot lembre de dar um crtl + c na etiqueta de teste, se quiser pode redimensionar.

Se for alterar a etiqueta de teste:
01-O primeiro campo selecionavel tem que ser sempre o nome do produto.
02- O segundo campo deve ser sempre o R$.
03- O terceiro deve ser o valor do produto.
04- O quarto deser ser o cod.

Oque vai acontecer quando comerçar a rodar o bot:

Primeiro arquivo criado:
O bot vai dar uma alt + tab, para ter acesso a pasta de etiquetas.
Depois vai dar um ctrl + C para criar/copiar a etiqueta de teste.
Vai alterar o nome do arquivo criado/copiado.
Em seguida vai entar na etiqueta mudar o nome, valor e cod, na respectiva ordem salvar e sair.

Proximos arquivos criados: Vai acontecer a mesma coisa, menos o alt + tab do começo. ficando: 
Depois vai dar um ctrl + C para criar/copiar a etiqueta de teste.
Vai alterar o nome do arquivo criado/copiado.
Em seguida vai entar na etiqueta mudar o nome, valor e cod, na respectiva ordem salvar e sair.

Importante: 
O primeiro loop sempre será o primeiro produto do excel, o segundo loop sempre será o primeiro produto do excel e etc... Se não quiser deixar o pc ligado até terminar todas as etiquetas tem duas escolhas.

01- Alterar na tabela: Tirar os itens já criados, excluindo as linhas. Para assim o próximo item a ser criado se tone o primeiro da tabela.
02- Alterar o loop: for i in range(x, y): O x deve ser agora o número da linha do próximo item a ser criado e o y o último item da tabela.

Tem que ter o BarTender Designer


