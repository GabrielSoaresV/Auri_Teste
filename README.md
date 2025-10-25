# Auri - Sistema de Demonstração com CustomTkinter

## Pré-requisitos

Antes de rodar o projeto, você precisa:

1. Ter o **Python 3.10+** instalado.
2. Instalar as bibliotecas necessárias:

```bash
pip install customtkinter pillow
```

## Como rodar

Abra o seu editor de codigo ou pront de comando

1. Clone o repositório:

```bash
git clone https://github.com/GabrielSoaresV/Auri_Teste.git
```

2. Entre na pasta do projeto:

```bash
cd Auri_teste
```

3. Execute o arquivo principal:

```bash
python main.py
```

## Estrutura do projeto

```
Auri/
│
├── main.py             # Arquivo principal para rodar a aplicação
├── interfaces/         # Pasta das telas da aplicação
│   ├── home.py         # Tela principal de navegação
│   ├── config.py       # Tela de configurações
│   ├── detector.py     # Tela de detector de som
│   ├── notificacao.py  # Tela de notificações
│   └── popup.py        # Janela popup de GIF
│
├── theme/              # Configurações globais de estilo
│   └── colors.py       # Paleta de cores usada no projeto
│
├── assets/             # Recursos visuais
│   ├── LogoAuri.png    # Logo principal da aplicação
│   └── gifs/           # GIFs usados nos popups
│
└── README.md           # Este arquivo
```

### Detalhes das pastas

- **interfaces/**: Contém todas as telas da aplicação. Cada arquivo representa uma tela diferente, organizada em classes.  
- **theme/**: Armazena configurações globais de estilização, como cores, fontes e temas.  
- **assets/**: Contém imagens, GIFs e outros recursos visuais usados na interface.

## Observações

- A aplicação usa `CustomTkinter` para criar uma interface moderna e responsiva.
- As imagens são carregadas via Pillow (`PIL`), então certifique-se que os arquivos estão no caminho correto.
- Para adicionar novas telas, basta criar uma nova classe dentro de `interfaces/` e adicioná-la ao `App` no `main.py`.
