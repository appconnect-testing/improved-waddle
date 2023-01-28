import streamlit as st


if __name__ == "__main__":
    st.set_page_config(page_title="Streamlit Template",
                    page_icon='✅',
                    initial_sidebar_state='collapsed')
    st.title('🔨 Streamlit Template')
    st.line_chart([[1, 1, 1, 1], [1, 1, 1, 1]])
    import os
    import ibm_db
    import ibm_db_dbi as dbi
    import pandas as pd
    BergenKommune_DB2_Frankfurt_dsn = 'DATABASE={};HOSTNAME={};PORT={};PROTOCOL=TCPIP;UID={uid};PWD={pwd};SECURITY=SSL'.format(
    'bludb',
    'ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud',
    31321,
    uid='sdy37069',
    pwd="""T0UHbErcCaXx3uGF""")
    BergenKommune_DB2_Frankfurt_connection = dbi.connect(BergenKommune_DB2_Frankfurt_dsn)

    st.markdown("""
        This app is only a template for a new Streamlit project. <br>

        ---
        """, unsafe_allow_html=True)

    st.balloons()
