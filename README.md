# Automatic signal processing tool
## (Ferramenta para processamento automático de sinais)

Aplicação para remoção automatica de outliers da pressão sistólica (PAS) e intervalo de pulso (IP) de acordo com intervalos pré defenidos.

Para utilização é necessário que os dados estejam em um arquivo de excel com as colunas sem nome e na seguinte ordem: Tempo, Pas e IP.

Após o processamento, o arquivo final já estara pronto para importação direta no software CardioSeries. Os testes de integração foram realizados na versão 2.7.

Desenvolvido em Python 3.7

Para executar o aplicativo de forma local, no terminal:

> streamlit run app.py

Para acessar o aplicativo online:

https://signalproc.herokuapp.com/

Dúvidas por favor entre em contato.

Exemplo de funcionamento:

![Grafico](https://github.com/gbazo/signalproc/blob/master/grafico.png)

Azul - antes do processamento
Laranja - depois
