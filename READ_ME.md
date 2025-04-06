# GameIntel Dashboard

GameIntel é um dashboard interativo desenvolvido com Streamlit e Plotly para analisar dados de vendas. Ele permite explorar vendas por região, publisher, gênero e ano, oferecendo uma visão abrangente sobre o mercado de games ao longo dos anos.


## 🛠️ Tecnologias Utilizadas
- Python
- Pandas
- Plotly
- Streamlit
- Jupyter Notebook

## 📂 Estrutura do Projeto
```
GameIntel/
├── data/
│   └── vg_sales.csv        # Arquivo CSV com dados de vendas de jogos
├── analysis.ipynb         # Jupyter Notebook com a Análise Exploratória de Dados (*EDA*)
├── app.py                 # Código fonte do dashboard
└── README.md              # Documentação do projeto
└── requirements.txt       # Dependências do projeto
```

## 💾 Dados
O arquivo CSV contém as seguintes colunas:
- **title**: Nome do jogo
- **console**: Plataforma (ex: PS4, Xbox One)
- **release_date**: Data de lançamento
- **publisher**: Empresa responsável pelo jogo
- **developer**: Empresa desenvolvedora
- **genre**: Gênero do jogo
- **region**: Região de vendas (JP, NA, PAL)
- **total_sales**: Vendas totais do jogo
- **jp_sales**: Vendas no Japão
- **na_sales**: Vendas na América do Norte
- **pal_sales**: Vendas na região PAL

## ⚙️ Funcionalidades
- **Filtro por Publisher**: Selecione um publisher específico para visualizar os dados.
- **Filtro por Região**: Escolha entre as regiões JP, NA, ou PAL para visualizar as vendas.
- **Filtro de Ano**: Defina um intervalo de tempo ou escolha um ano específico.
- **Gráficos Interativos**:
  - Barras: Vendas por console, jogos vendidos e top 10 best-sellers do ano
  - Pizza: Vendas por gênero
  - Linha: Receita ao longo dos anos
  - Top 10 Melhores Vendas do Ano
- **Métricas**: Receita total acumulada.

## 🚀 Como Executar
1. Clone o repositório:
   ```bash
   git clone https://github.com/usuario/gameintel.git
   cd gameintel
   ```
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Execute o dashboard:
   ```bash
   streamlit run app.py
   ```

