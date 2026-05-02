import streamlit as st
import sqlite3

#--- 1. FUNÇÃO DO BANCO DE DADOS---

#inicia o banco
def inicializar_banco():
#conecta o banco de dados ao arquivo(cria se não existir)
    conexao = sqlite3.connect("agenda_mamae.db")
    cursor = conexao.cursor()

#Cria a tabela
    cursor.execute('''import streamlit as st
import sqlite3

#--- 1. FUNÇÃO DO BANCO DE DADOS---

#inicia o banco
def inicializar_banco():
#conecta o banco de dados ao arquivo(cria se não existir)
    conexao = sqlite3.connect("agenda_mamae.db")
    cursor = conexao.cursor()

#Cria a tabela
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS agendamentos(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       cliente TEXT NOT NULL,
       data TEXT NOT NULL,
       servico TEXT NOT NULL
             )          
    ''')

    conexao.commit()
    conexao.close()

#Já chama a função para garantir que o banco existe
inicializar_banco()

#--- 2. INTERFACE DO USUÁRIO ---
st.title("🌸 Agenda da Mamãe")

#Adiciona colunas, campos de entrada
col1, col2 = st.columns(2)

with col1:
     nome = st.text_input("👤 Cliente")
     servico = st.selectbox("💅 Serviço", ["Manicure", "Pedicure" , "Manicure e Pedicure"])

with col2:
     data = st.date_input("📆 Data")
     horario = st.text_input("⏰ Horário")


#--- 3.BOTÃO DE SALVAR AGENDAMENTO ---

if st.button("✔️ Salvar agendamento"):
     if data and horario:
          #abrindo conexão do banco de dados para salvar
          conn = sqlite3.connect("agenda_mamae.db")
          cursor = conn.cursor()
           
          #juntando data e horário
          data_completa = f"{data} às {horario}"
          cursor.execute("INSERT INTO agendamentos(cliente, data, servico) VALUES(?, ?, ?)",
                         (nome, data_completa, servico))
          
          conn.commit()
          conn.close()

          st.success(f"Agendamento de {nome} feito com sucesso!")

     else:
        st.error("Preencha o nome e o horário novamente") 

    
st.divider()
st.subheader("🗒 Próximos Agendamentos")
     
conn = sqlite3.connect("agenda_mamae.db")
cursor = conn.cursor()

cursor.execute(" SELECT cliente, data, servico , id FROM agendamentos ORDER BY id DESC ")
dados = cursor.fetchall()
conn.close()

# Mostra a lista de agendamentos
for agendamento in dados:
     id_agendamento =  agendamento[3]
#--- TIRANDO O PADRÃO DE DATA AMERICANO
     try:
#inverte o padrão(AAAA/MM/DD) para (DD/MM/AAAA)
        partes = agendamento[1].split(" às ")
        data_bruta = partes[0]
        hora_bruta = partes[1]
        ano, mes, dia = data_bruta.split("-")
        data_formatada = f"{dia}/{mes}/{ano}  às {hora_bruta}"
     except:
        data_formatada = agendamento[1] #se der erro a data volta a estar no padrão anterior    


     col_nome, col_btn = st.columns([4, 1])# É pra coluna do nome ser maior que o botão
     with col_nome:
            st.write(f"🌹**{agendamento[0]}** - {agendamento[2]} em {data_formatada}")


     with col_btn:
    #criação do botão de excluir com uma chave única
        if st.button("🗑️", key=f"excluir_{id_agendamento}"):
            conn = sqlite3.connect("agenda_mamae.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM agendamentos WHERE id= ?", (id_agendamento,))
            conn.commit()
            conn.close()
            st.rerun() # Recarrega a pagina para sumir da lista


             
    CREATE TABLE IF NOT EXISTS agendamentos(
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       cliente TEXT NOT NULL,
       data TEXT NOT NULL,
       servico TEXT NOT NULL
             )          
    ''')

    conexao.commit()
    conexao.close()

#Já chama a função para garantir que o banco existe
inicializar_banco()

#--- 2. INTERFACE DO USUÁRIO ---
st.title("🌸 Agenda da Mamãe")

#Adiciona colunas, campos de entrada
col1, col2 = st.columns(2)

with col1:
     nome = st.text_input("👤 Cliente")
     servico = st.selectbox("💅 Serviço", ["Manicure", "Pedicure" , "Manicure e Pedicure"])

with col2:
     data = st.date_input("📆 Data")
     horario = st.text_input("⏰ Horário")


#--- 3.BOTÃO DE SALVAR AGENDAMENTO ---

if st.button("✔️ Salvar agendamento"):
     if data and horario:
          #abrindo conexão do banco de dados para salvar
          conn = sqlite3.connect("agenda_mamae.db")
          cursor = conn.cursor()
           
          #juntando data e horário
          data_completa = f"{data} às {horario}"
          cursor.execute("INSERT INTO agendamentos(cliente, data, servico) VALUES(?, ?, ?)",
                         (nome, data_completa, servico))
          
          conn.commit()
          conn.close()

          st.success(f"Agendamento de{nome} feito com sucesso!")

     else:
        st.error("Preencha o nome e o horário novamente") 

    
st.divider()
st.subheader("🗒 Próximos Agendamentos")
     
conn = sqlite3.connect("agenda_mamae.db")
cursor = conn.cursor()

cursor.execute(" SELECT cliente, data, servico , id FROM agendamentos ORDER BY id DESC ")
dados = cursor.fetchall()
conn.close()

# Mostra a lista de agendamentos
for agendamento in dados:
     id_agendamento =  agendamento[3]
     col_nome, col_btn = st.columns([4, 1])# É pra coluna do nome ser maior que o botão

     with col_nome:
          st.write(f"🌹 **{agendamento[0]}** - {agendamento[2]} em {agendamento[1]}")


     with col_btn:
    #criação do botão de excluir com uma chave única
        if st.button("🗑️", key=f"excluir_{id_agendamento}"):
            conn = sqlite3.connect("agenda_mamae.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM agendamentos WHERE id= ?", (id_agendamento,))
            conn.commit()
            conn.cursor()
            st.rerun() # Recarrega a pagina para sumir da lista


             
