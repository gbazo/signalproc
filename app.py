import streamlit as st
import pandas as pd
import numpy as np
import base64

def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(sep='\t', decimal=',', index=False, header=False)
    b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
    href = f'<a href="data:file/csv;base64,{b64}">Download csv file</a>'
    return href

def main():
    st.title('Ferramenta para processamento automático de sinais')
    st.subheader('Remoção de outliers da pressão sistólica (PAS) e intervalo de pulso (IP)')
    file  = st.file_uploader('Escolha os dados que deseja analisar (.xlsx)', type = 'xlsx')
    if file is not None:
        st.subheader('Analisando os dados')
        df = pd.read_excel(file)
        df.columns = ['tempo', 'pas', 'ip']
        df2 = df[['tempo','pas', 'ip']]
        st.markdown('**Número de linhas:**')
        st.markdown(df.shape[0])
        st.markdown('**Número de colunas:**')
        st.markdown(df.shape[1])
        st.markdown('**Visualizando o dataframe (5 primeiras linhas)**')
        st.dataframe(df.head())
        st.markdown('**Caracteristicas dos dados:**')
        st.dataframe(df.describe())
        
        st.markdown('**Gráfico IP x Tempo:**')
        st.line_chart(df.ip)

        st.markdown('**Gráfico PAS x Tempo:**')
        st.line_chart(df.pas)

        st.markdown('**Pontos de limpeza sugeridos:**')
        st.markdown('IP (intervalo calculado por percentil):')
        
        Q1 = round(np.percentile(df['ip'],0.5), 3)
        Q2 = round(np.percentile(df['ip'],99.5), 3)

        st.markdown(Q1)
        st.markdown(Q2)

        st.markdown('PAS (intervalo calculado por percentil):')
        
        P1 = round(np.percentile(df['pas'],0.5), 3)
        P2 = round(np.percentile(df['pas'],99.5), 3)

        st.markdown(P1)
        st.markdown(P2)

        st.markdown('**Deseja alterar os pontos de limpeza?**')

        st.markdown('IP')

        values_IP = st.slider("Intervalo IP", float(df.ip.min()), float(df.ip.max()), (Q1, Q2))
        
        st.markdown('PAS')

        values_PAS = st.slider("Intervalo PAS", float(df.pas.min()), float(df.pas.max()), (P1, P2))

        tm = len(df2)

        for i in df2.index:
            if i > 1 and i < (tm-2):
                if (df2.ip[i] >= np.max(values_IP)):
                    c = ((df2.ip[i-1] + df2.ip[i-2]) / 2)
                    df2.ip[i] = c
                    i = i + 1
                elif (df2.ip[i] <= np.min(values_IP)):
                    c = ((df2.ip[i+1] + df2.ip[i+2]) / 2)
                    df2.ip[i] = c
                    i = i + 1
                else:
                    pass
            else:              
                pass

        for i in df2.index:
            if i > 1 and i < (tm-2):        
                if (df2.pas[i] >= np.max(values_PAS)):
                    c = ((df2.pas[i-1] + df2.pas[i-2]) / 2)
                    df2.pas[i] = c
                    i = i + 1
                elif (df2.pas[i] <= np.min(values_PAS)):
                    c = ((df2.pas[i+1] + df2.pas[i+2]) / 2)
                    df2.pas[i] = c
                    i = i + 1
                else:
                    pass
            else:              
                pass

        st.markdown('**Caracteristicas dos dados após o processamento:**')
        st.dataframe(df2.describe())

        st.markdown('**Novo Gráfico IP x Tempo:**')
        ip_ = pd.DataFrame({'ip':df['ip'], 'ip2':df2['ip']})
        st.line_chart(ip_)
        
        st.markdown('**Novo Gráfico PAS x Tempo:**')
        pas_ = pd.DataFrame({'pas':df['pas'], 'pas2':df2['pas']})
        st.line_chart(pas_)     

        st.subheader('Dados Inputados faça download abaixo : ')

        st.markdown(get_table_download_link(df2), unsafe_allow_html=True)

    st.markdown('-----------------------------------------------------')
    st.text('Desenvolvido por Gabriel Bazo')
    st.text('Livre para uso acadêmico')
    st.text('Dúvidas ou sugestões: bazot3@hotmail.com')

if __name__ == '__main__':
	main()