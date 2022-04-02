from notion_client import Client
import streamlit as st
import time
import json


# file = open('info.json', 'r')
# info = json.load(file)

# NOTION_TOKEN = info['NOTION_TOKEN']
# notion = Client(auth=NOTION_TOKEN)
# # taskDB
# db_id = info['db_id']


NOTION_TOKEN = st.secrets['NOTION_TOKEN']
notion = Client(auth=NOTION_TOKEN)

# taskDB
db_id = st.secrets['db_id']

# inboxへタスク(思いついたこと)を登録
@st.cache
def add_inbox(task):
    property_name = {"title": [{"text": {"content": task}}]}
    notion.pages.create(
        **{'parent': {'database_id': db_id},
           'properties': {'task name': property_name}
           }
    )


# streamlitによるwebアプリ
st.title('Add Inbox Notion')

input_inbox = st.text_input('Task Name')
if input_inbox:
    add_inbox(input_inbox)
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
        latest_iteration.text(f'♻送信中... {i+1}')
        bar.progress(i+1)
        time.sleep(0.01)
    '✅ "', input_inbox, '" をinboxに登録しました'
    input_inbox = ''