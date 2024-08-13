import tkinter as tk
from tkinter import filedialog, messagebox
import os

def load_file_content(file_name):
    with open(file_name, 'r') as file:
        return file.readlines()

def process_files_to_lists(servidores, pensao):
    tipo_registro_pos_servidores = 18
    tipo_registro_pos_pensao = 25
    
    registros_servidores = {str(i): [] for i in range(10)}
    registros_pensao = {str(i): [] for i in range(10)}
    
    for line in servidores:
        tipo_registro = line[tipo_registro_pos_servidores - 1]
        if tipo_registro in registros_servidores:
            registros_servidores[tipo_registro].append(line)
    
    for line in pensao:
        tipo_registro = line[tipo_registro_pos_pensao - 1]
        if tipo_registro in registros_pensao:
            registros_pensao[tipo_registro].append(line)

    return registros_servidores, registros_pensao

def create_extrat2(output_servidores_tipo_3, output_servidores_tipo_0, output_servidores_tipo_1, output_dir):
    dict_servidores_tipo_1 = {
        line[9:17].strip(): {
            "pos_81_91": line[80:91].strip(),
            "pos_196_201": line[195:201].strip()
        } 
        for line in output_servidores_tipo_1
    }
    
    output_content = []
    
    for line in output_servidores_tipo_3:
        combined_line = [' '] * 72
        combined_line[0] = '1'

        # Preencher a posição 52 com '0'
        combined_line[51] = '0'

        # Inserir a vírgula na posição 69
        combined_line[68] = ','

        # Mapeamento específico
        mappings = [
            (10, 17, 12, 20), 
            (28, 36, 54, 68),  # Novo mapeamento com zeros à esquerda
            (37, 38, 70, 71),  # Mapeamento para 70-71 em extrat2
            (21, 21, 72, 72)   # Mapeamento para 72 em extrat2
        ]

        for start_src, end_src, start_dest, end_dest in mappings:
            extracted_data = line[start_src-1:end_src].strip()
            padded_data = extracted_data.zfill(end_dest-start_dest+1)
            combined_line[start_dest-1:end_dest] = list(padded_data)
        
        # Preencher campo 44-51 com dados específicos
        extracted_data_22_26 = line[21:26].strip()
        combined_line[43:51] = list(extracted_data_22_26.zfill(8))

        # Inserir o valor da Posição [27, 27] em `output_servidores_tipo_3` na Posição [53, 53] em `extrat2`
        combined_line[52] = line[26:27]

        # Inserir valores de `output_servidores_tipo_1` nas posições [21, 31] e [32, 37]
        key_to_match = ''.join(combined_line[12:20]).strip()
        if key_to_match in dict_servidores_tipo_1:
            combined_line[20:31] = list(dict_servidores_tipo_1[key_to_match]["pos_81_91"].zfill(11))
            combined_line[31:37] = list(dict_servidores_tipo_1[key_to_match]["pos_196_201"].zfill(6))

        # Inserir dados de `output_servidores_tipo_0` nas posições [38, 43]
        if output_servidores_tipo_0:
            combined_line[37:43] = list(output_servidores_tipo_0[0][45:51].strip().zfill(6))

        # Garantir que o trecho [2, 12] esteja preenchido com espaços em branco
        combined_line[1:12] = [' '] * 11
        
        output_content.append(''.join(combined_line))
    
    output_path = os.path.join(output_dir, "extrat2.txt")
    with open(output_path, 'w') as file:
        file.write('\n'.join(output_content))
    
    return output_path

def create_extrat6(output_pensao_tipo_7, output_pensao_tipo_3, output_servidores_tipo_0, output_dir):
    # Criar dicionário para busca rápida em output_pensao_tipo_3
    dict_pensao_tipo_3 = {
        line[16:24].strip(): line[80:91].strip()
        for line in output_pensao_tipo_3
    }
    
    output_content = []
    
    for line in output_pensao_tipo_7:
        combined_line = [' '] * 72
        combined_line[0] = '7'  # Define o tipo de registro como 7 para extrat6

        # Preencher a posição 52 com '0'
        combined_line[51] = '0'

        # Inserir a vírgula na posição 69
        combined_line[68] = ','

        # Mapeamento específico para extrat6
        mappings = [
            (17, 24, 13, 20),  # Posição de Origem [17, 24] -> Posição de Destino [13, 20]
            (29, 33, 44, 51),  # Posição de Origem [29, 33] -> Posição de Destino [44, 51]
            (38, 46, 54, 68),  # Posição de Origem [38, 46] -> Posição de Destino [54, 68]
            (47, 48, 70, 71),  # Posição de Origem [47, 48] -> Posição de Destino [70, 71]
            (28, 28, 72, 72),  # Posição de Origem [28, 28] -> Posição de Destino [72, 72]
            (37, 37, 53, 53)   # Posição de Origem [37, 37] -> Posição de Destino [53, 53]
        ]

        for start_src, end_src, start_dest, end_dest in mappings:
            extracted_data = line[start_src-1:end_src].strip()
            padded_data = extracted_data.zfill(end_dest-start_dest+1)
            combined_line[start_dest-1:end_dest] = list(padded_data)

        # Verificar correspondência de chave e inserir dados de output_pensao_tipo_3
        key_to_match = ''.join(combined_line[12:20]).strip()
        if key_to_match in dict_pensao_tipo_3:
            combined_line[20:31] = list(dict_pensao_tipo_3[key_to_match].zfill(11))
        
        # Inserir dados de output_servidores_tipo_0 nas posições [38, 43]
        if output_servidores_tipo_0:
            combined_line[37:43] = list(output_servidores_tipo_0[0][45:51].strip().zfill(6))

        # Garantir que o trecho [2, 12] esteja preenchido com espaços em branco
        combined_line[1:12] = [' '] * 11

        output_content.append(''.join(combined_line))
    
    output_path = os.path.join(output_dir, "extrat6.txt")
    with open(output_path, 'w') as file:
        file.write('\n'.join(output_content))
    
    return output_path

def transform_and_save():
    if not servidores or not pensao:
        messagebox.showwarning("Erro", "Por favor, carregue ambos os arquivos antes de continuar.")
        return
    
    registros_servidores, registros_pensao = process_files_to_lists(servidores, pensao)
    output_dir = filedialog.askdirectory(title="Selecione a pasta para salvar o arquivo")
    if not output_dir:
        return

    # Criação do extrat2.txt
    output_path_extrat2 = create_extrat2(registros_servidores['3'], registros_servidores['0'], registros_servidores['1'], output_dir)
    
    # Criação do extrat6.txt
    output_path_extrat6 = create_extrat6(registros_pensao['7'], registros_pensao['3'], registros_servidores['0'], output_dir)
    
    if output_path_extrat2 and output_path_extrat6:
        messagebox.showinfo("Sucesso", f"Arquivos 'extrat2.txt' e 'extrat6.txt' salvos com sucesso em {output_dir}")

def load_file(file_type):
    file_path = filedialog.askopenfilename()
    if file_path:
        if file_type == 1:
            global servidores
            servidores = load_file_content(file_path)
            lbl_file1.config(text=f"Arquivo 1: {os.path.basename(file_path)} carregado")
        else:
            global pensao
            pensao = load_file_content(file_path)
            lbl_file2.config(text=f"Arquivo 2: {os.path.basename(file_path)} carregado")

        if servidores and pensao:
            messagebox.showinfo("Carregamento Completo", "Ambos os arquivos foram carregados com sucesso!")

# Criação da Janela Principal
root = tk.Tk()
root.title("Extrator de Dados")

servidores = None
pensao = None

# Labels e Botões
lbl_file1 = tk.Label(root, text="Arquivo de Servidores: Não carregado")
lbl_file1.pack(pady=10)

btn_file1 = tk.Button(root, text="Carregar Servidores", command=lambda: load_file(1))
btn_file1.pack(pady=5)

lbl_file2 = tk.Label(root, text="Arquivo de Pensionistas: Não carregado")
lbl_file2.pack(pady=10)

btn_file2 = tk.Button(root, text="Carregar Pensionistas", command=lambda: load_file(2))
btn_file2.pack(pady=5)

btn_transform = tk.Button(root, text="Processar e Salvar", command=transform_and_save)
btn_transform.pack(pady=20)

# Inicia a Interface Gráfica
root.mainloop()
