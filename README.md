# README

Este script é usado para acessar um conjunto de URLs de artigos públicos da ENAP, extrair links para páginas de artigos e baixar arquivos PDF dessas páginas. Ele utiliza a biblioteca `requests` para fazer solicitações HTTP, `BeautifulSoup` para fazer o parsing de conteúdo HTML e `os` para operações de arquivos e caminhos.

Os artigos baixados neste script estão localizados em: https://repositorio.enap.gov.br/handle/1/6939

## Pré-requisitos

Antes de executar este script, certifique-se de ter as seguintes dependências instaladas:

- requests
- BeautifulSoup

Essas dependências podem ser instaladas usando o pip:

```
pip install requests
pip install beautifulsoup4
```

## Uso

Para usar este script, siga estas etapas:

1. Defina os caminhos de saída e de log modificando as variáveis `OUTPUT_PATH` e `LOG_PATH`. Por padrão, os arquivos de saída serão salvos em um diretório `data` e os logs serão salvos em um diretório `log`.

2. Modifique a lista `urls` para conter as URLs de onde deseja extrair os links dos artigos. Você pode adicionar ou remover URLs conforme necessário. O script suporta paginação, então você pode incluir várias URLs se os artigos estiverem distribuídos em diferentes páginas.

3. Execute o script usando um interpretador Python:

```
python script.py
```

4. O script executará as seguintes etapas:

   - Acessará as URLs fornecidas e extrairá o conteúdo de cada página, armazenando-o em uma lista.
   - Extrairá os links para as páginas de artigos a partir do conteúdo coletado.
   - Acessará cada página de artigo e extrairá o link para o arquivo PDF.
   - Baixará cada arquivo PDF e o salvará no caminho de saída especificado.
   - Criará um arquivo de log (`log.txt`) no caminho de log para registrar o código de status e o nome do arquivo de cada PDF baixado.

Observação: O script inclui um atraso de 2 segundos entre cada solicitação para evitar sobrecarregar o servidor. Você pode ajustar esse atraso conforme necessário, modificando as chamadas de `time.sleep()`.

## Personalização

Sinta-se à vontade para modificar o script de acordo com seus requisitos específicos. Você pode alterar os caminhos de saída e de log, ajustar o atraso entre as solicitações ou adicionar funcionalidades adicionais de acordo com suas necessidades.

## Aviso

Observe que este script é fornecido "como está". É recomendado revisar o código e entender suas implicações antes de executá-lo.