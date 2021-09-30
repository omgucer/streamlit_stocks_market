import yfinance as yf
import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

st.write("""
# Percent change in Stock Prices
## Shown the percentual change in the given timelapse
""")


#define the ticker symbol
tickers = ['TSLA', 'AMZN', 'GOOGL', 'MSFT']

drop= st.multiselect('Select assets', tickers)

start= st.date_input('Start', value= pd.to_datetime('2020-01-01'))
end= st.date_input('End', value = pd.to_datetime('today'))


def relative_return(df):
    rel = df.pct_change()
    cumult_ret = (1+rel).cumprod()-1
    cumult_ret = cumult_ret.fillna(0)
    return cumult_ret

if len(drop)>0:
    df_adjclose = relative_return(yf.download(drop, start, end)['Adj Close'])
    df_open = relative_return(yf.download(drop, start, end)['Open'])
    df_high = relative_return(yf.download(drop, start, end)['High'])
    df_low = relative_return(yf.download(drop, start, end)['Low'])
    df_close = relative_return(yf.download(drop, start, end)['Close'])
    df_vol = relative_return(yf.download(drop, start, end)['Volume'])
    
    st.header('Assets for {}'.format(drop))
    
    """
    # Percernt change in the Open Price 
    """
    st.line_chart(df_open)
    
    """
    # Percernt change in the High Price 
    """
    st.line_chart(df_high)
    """
    # Percernt change in the Low Price 
    """
    st.line_chart(df_low)
    """
    # Percernt change in the Close Price 
    """
    st.line_chart(df_close)
    """
    # Percernt change in the Volume 
    """
    st.line_chart(df_vol)
    """
    # Percernt change in the Adj Close Price 
    """
    st.line_chart(df_adjclose)
    
    
    @st.cache
    def convert_df(df):
     # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode('utf-8')

    
    st.write( """ 
    # Data for the prices on the selected timelapse
    ## Stock prices corresponding to: Open, High, Low, Close, Adj Close
    
    
    """)
    col1, col2 = st.columns(2)
    
    with col1:
        st.write('Data: Open')
        st.dataframe(df_open)
        open_csv = convert_df(df_open)
        st.download_button('Download Open CSV', open_csv, 'text/csv')
    
        st.write('Data: High')
        st.dataframe(df_high)
        high_csv = convert_df(df_high)
        st.download_button('Download High CSV', high_csv, 'text/csv')
    
        st.write('Data: Low')
        st.dataframe(df_low)
        low_csv = convert_df(df_low)
        st.download_button('Download Low CSV', low_csv, 'text/csv')
    
    with col2:
        st.write('Data: Close')
        st.dataframe(df_close)
        close_csv = convert_df(df_close)
        st.download_button('Download Close CSV', close_csv, 'text/csv')
    
        st.write('Data: Volume')
        st.dataframe(df_vol)
        vol_csv = convert_df(df_vol)
        st.download_button('Download Volume CSV', vol_csv, 'text/csv')
    
        st.write('Data: Adj Close')
        st.dataframe(df_adjclose)
        adjclose_csv = convert_df(df_adjclose)
        st.download_button('Download Adj Close CSV', adjclose_csv, 'text/csv')
    
    
hide_st_style = """ 
             <style>
             #MainMenu {visibility: hidden;}
             footer {visibility: hidden;}
             header {visibility: hidden;}
             </style>
             
             """
st.markdown(hide_st_style, unsafe_allow_html= True)