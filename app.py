import streamlit as st

pages = {
    'Главная':[
        st.Page('./src/pages/main_pages/main_page.py',title='Главная страница',icon='👋'),
    ],
    'Настройки':[
        st.Page('./src/pages/settings_pages/settings_agent_page.py',title='Настройки агента',icon='⚙️'),
    ],
    'Агент':[
        st.Page('./src/pages/agent_pages/agent_page.py',title='Агент',icon='🦾')
    ],
    'Остальное':[
        st.Page('./src/pages/other_pages/links_page.py',title='Контакты',icon='🔗'),
    ]
}

pg = st.navigation(pages=pages,position='top')
pg.run()