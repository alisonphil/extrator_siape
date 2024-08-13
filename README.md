# Extrator de Dados SIAPE
Este projeto consiste em um script Python que extrai e processa dados de arquivos de servidores e pensionistas, gerando relatórios formatados (extrat2.txt e extrat6.txt). A aplicação utiliza a biblioteca tkinter para fornecer uma interface gráfica simples para carregamento dos arquivos e execução das transformações.
---------------------------------------------------------------------------------------------------------------------------------------------------

Glossário Básico:

UPAG: Unidade Pagadora, identificada por um código de 9 dígitos.
Matrícula SIAPE: Número de matrícula do servidor ou pensionista no sistema SIAPE.
DV Matrícula: Dígito Verificador da Matrícula.
Tipo de Registro: Identificador numérico que indica o tipo de dados contidos no registro. Pode variar de 0 a 9, conforme especificado nos arquivos de layout.
Tipo 0: Header do arquivo, identificando o órgão processado.
Tipo 1: Dados pessoais do servidor ou instituidor.
Tipo 2: Dados funcionais do servidor ou dados cadastrais do instituidor (Pensão Legal).
Tipo 3: Dados financeiros do servidor ou dados cadastrais do pensionista.
Tipo 4: Dados cadastrais do benefício.
Tipo 5: Dados financeiros do instituidor (servidor falecido).
Tipo 6: Totalização dos dados financeiros do servidor ou instituidor.
Tipo 7: Dados financeiros do pensionista.
Tipo 8: Totalização dos dados financeiros do pensionista.
Tipo 9: Trailler do arquivo, contendo contagem de registros.
CPF: Cadastro de Pessoa Física, número que identifica o servidor ou pensionista.
Filler: Espaço em branco usado para preencher campos de tamanho fixo que não possuem dados.
---------------------------------------------------------------------------------------------------------------------------------------------------


Funcionalidades
Carregamento de Arquivos: Permite o carregamento de arquivos de servidores e pensionistas em formato de texto.
Processamento de Dados: Extrai informações específicas dos arquivos carregados e as organiza em listas separadas por tipo de registro.
Geração de Relatórios: Cria arquivos de saída (extrat2.txt e extrat6.txt) formatados de acordo com as especificações fornecidas.
Interface Gráfica: Fornece uma interface gráfica simples para facilitar o uso da ferramenta.
Instalação
Clone o repositório:
---------------------------------------------------------------------------------------------------------------------------------------------------


Instale as dependências:
Este projeto utiliza a biblioteca tkinter, que geralmente já está incluída na instalação padrão do Python. Se necessário, você pode instalá-la utilizando pip:

pip install tk
Execute a aplicação:
Basta rodar o script Extrator_Siape.py:

---------------------------------------------------------------------------------------------------------------------------------------------------


Uso
Carregamento dos Arquivos:


Ao iniciar o aplicativo, use os botões "Carregar Servidores" e "Carregar Pensionistas" para carregar os arquivos de texto respectivos.
Processamento e Salvamento:

Após carregar os arquivos, clique no botão "Processar e Salvar". O aplicativo irá gerar os arquivos extrat2.txt e extrat6.txt e salvar na pasta de sua escolha.
---------------------------------------------------------------------------------------------------------------------------------------------------


Estrutura do Código
O código está dividido em várias funções que desempenham tarefas específicas:

load_file_content(file_name): Carrega o conteúdo de um arquivo de texto em uma lista de strings.
process_files_to_lists(servidores, pensao): Processa os arquivos de servidores e pensionistas, separando os registros por tipo.
create_extrat2(output_servidores_tipo_3, output_servidores_tipo_0, output_servidores_tipo_1, output_dir): Gera o arquivo extrat2.txt a partir dos dados processados.
create_extrat6(output_pensao_tipo_7, output_pensao_tipo_3, output_servidores_tipo_0, output_dir): Gera o arquivo extrat6.txt a partir dos dados processados.
transform_and_save(): Função principal que coordena o processo de carregamento, transformação, e salvamento dos arquivos.
load_file(file_type): Carrega o arquivo de servidores ou pensionistas conforme o tipo especificado.

Exemplo de Execução
python
Copiar código
# Inicie a aplicação
python Extrator_Siape.py
# Siga as instruções na interface gráfica para carregar os arquivos e processar os dados.

Faça bom uso!
