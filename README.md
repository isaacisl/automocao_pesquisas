
# Projeto Automação de Pesquisas

Este projeto foi desenvolvido para automatizar o processo de coleta, transformação e consolidação de dados de pesquisas da **CNM (Confederação Nacional de Municípios)**. Ele realiza o **ETL (Extract, Transform, Load)** de bases de dados obtidas em um portal específico, agilizando o processo de análise e consolidação das informações.

---

## Tecnologias Utilizadas

- **Python**: Linguagem de programação principal para a automação e manipulação de dados.
- **Pandas**: Biblioteca para manipulação e análise de dados, utilizada para transformar e consolidar as bases de dados.
- **Selenium**: Framework para automação de navegadores, utilizado para interagir com o portal e baixar as bases de dados.
- **Outras bibliotecas**: Bibliotecas como `openpyxl`, `os`, `time`, entre outras, para auxiliar na manipulação de arquivos e no controle de fluxo do processo.

---

## Funcionalidades

1. **Automação do Download**:
   - Utiliza o **Selenium** para acessar o portal, realizar login (se necessário) e baixar as bases de dados de forma automatizada.

2. **Transformação dos Dados**:
   - Usa o **Pandas** para ler, limpar e transformar os dados baixados, garantindo que estejam no formato adequado para análise.

3. **Consolidação das Pesquisas**:
   - Consolida múltiplas bases de dados em um único arquivo estruturado, pronto para análise ou compartilhamento.

4. **Automatização Completa**:
   - O processo é executado de ponta a ponta, desde o download até a geração do arquivo final, sem necessidade de intervenção manual.

---

## Como Funciona

1. **Configuração Inicial**:
   - O script é configurado com as credenciais de acesso ao portal (se necessário) e os parâmetros para download das bases de dados.

2. **Execução**:
   - O script inicia o navegador, acessa o portal, baixa os arquivos e os salva em uma pasta local.

3. **Processamento**:
   - Os arquivos baixados são lidos, transformados e consolidados em um único arquivo estruturado (por exemplo, um arquivo Excel ou CSV).

4. **Saída**:
   - O arquivo final é salvo em um local pré-definido, pronto para uso.

---

## Pré-requisitos

- Python 3.x instalado.
- Bibliotecas Python: `pandas`, `selenium`, `openpyxl`, etc.
- WebDriver compatível com o navegador utilizado (ex: ChromeDriver para o Google Chrome).

Para instalar as dependências, execute:
```bash
pip install pandas selenium openpyxl
```

---

## Como Executar

1. Clone o repositório:
   ```bash
   git clone https://github.com/isaacisl/automocao_pesquisas.git
   ```

2. Navegue até o diretório do projeto:
   ```bash
   cd automocao_pesquisas
   ```

3. Configure as credenciais e parâmetros no script (se necessário).

4. Execute o script principal:
   ```bash
   python main.py
   ```

## Licença

Este projeto está sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

