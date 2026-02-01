import streamlit as st

pages = {
    'Главная':[
        st.Page('./src/pages/main_page.py',title='Главная страница',icon='👋'),
        st.Page('./src/pages/settings_page.py',title='Настройки',icon='⚙️')
    ],
    'Агент':[
        st.Page('./src/pages/agent_page.py',title='Агент',icon='🦾')
    ],
    'Остальное':[
        st.Page('./src/pages/links_page.py',title='Контакты',icon='🔗'),
        st.Page('./src/pages/version_page.py',title='Версии',icon='🗂️')
    ]
}

pg = st.navigation(pages=pages,position='top')
pg.run()