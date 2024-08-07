# Classe para manipulação dos arquivos 
class ManipuladorDeArquivos:
    def __init__(self, nome_arquivo): # método construtor inicializa o objeto
        self.nome_arquivo = nome_arquivo

    def criar_arquivo(self): # método para criação de arquivos
        with open(self.nome_arquivo, 'w') as arquivo:
            arquivo.write('')
        print('\nArquivo criado com sucesso.')

    def ler_arquivo(self, modo='r'): # método para leitura de arquivos, com exceção para arquivos não encontrados no diretório
        try:
            with open(self.nome_arquivo, modo) as arquivo:
                return arquivo.read()
        except FileNotFoundError:
            raise FileNotFoundError(f"\nArquivo {self.nome_arquivo} não encontrado.")

    def editar_arquivo(self, novo_conteudo, modo='a'): # método para edição do arquivo, sem apagar o conteúdo pré-existente; cria arquivo se o mesmo não existir
        with open(self.nome_arquivo, modo) as arquivo:
            arquivo.write(novo_conteudo)
        print(f"\nConteúdo do arquivo {self.nome_arquivo} atualizado.")
        
    def reescrever_arquivo(self, novo_conteudo): # método para reescrever arquivo, apaga conteúdo existente se houver; cria arquivo se o mesmo não existir
        self.editar_arquivo(novo_conteudo, modo='w')


try:
    while True: # loop para menu de opções
        print('')
        menu = int(input('Digite o número da opção:\n \
            1- Criar arquivo\n \
            2- Ler Arquivo\n \
            3- Editar Arquivo\n \
            4- Reescrever arquivo\n \
            5- Sair \n'))
        
        
        if menu == 5: # condição para encerramento do programa
            exit()

        caminho_arquivo = input('Digite o caminho e/ou nome do arquivo: \n') # variável que recebe o caminho e/ou nome do arquivo
            
        arquivo = ManipuladorDeArquivos(caminho_arquivo) # variável que recebe a classe e o caminho do arquivo
        
        match menu: # controle de fluxo para variável menu do menu principal
            case 1:
                arquivo.criar_arquivo()
            case 2:
                conteudo = arquivo.ler_arquivo()
                print(conteudo)
            case 3:
                texto = input('\nDigite o texto que deseja adicionar: ')
                arquivo.editar_arquivo(texto)
            case 4:
                texto = input('\nDigite o texto que deseja adicionar: ')
                arquivo.reescrever_arquivo(texto)
            case _:
                print('\nOpção Inválida')
                
except Exception as e: # para exceções não tratadas
    print(f'Ocorreu um erro: {e}')