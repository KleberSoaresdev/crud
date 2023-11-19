import mysql.connector
conexao = mysql.connector.connect(
    host="seu_host",
    user="seu_usuario",
    password="sua_senha",
    database="sua_base_de_dados"
)

cursor = conexao.cursor()

def criar_tabela():
    tabela_sql = """
    CREATE TABLE IF NOT EXISTS playlist (
        id INT AUTO_INCREMENT PRIMARY KEY,
        titulo VARCHAR(255) NOT NULL,
        artista VARCHAR(255) NOT NULL,
        album VARCHAR(255),
        duracao INT
    )
    """
    cursor.execute(tabela_sql)
    conexao.commit()

def adicionar_musica(titulo, artista, album, duracao):
    inserir_sql = "INSERT INTO playlist (titulo, artista, album, duracao) VALUES (%s, %s, %s, %s)"
    valores = (titulo, artista, album, duracao)
    cursor.execute(inserir_sql, valores)
    conexao.commit()

def visualizar_playlist():
    selecionar_sql = "SELECT * FROM playlist"
    cursor.execute(selecionar_sql)
    resultados = cursor.fetchall()

    if not resultados:
        print("Playlist vazia.")
    else:
        for musica in resultados:
            print(musica)

def atualizar_musica(musica_id, novo_titulo, novo_artista, novo_album, nova_duracao):
    atualizar_sql = "UPDATE playlist SET titulo=%s, artista=%s, album=%s, duracao=%s WHERE id=%s"
    valores = (novo_titulo, novo_artista, novo_album, nova_duracao, musica_id)
    cursor.execute(atualizar_sql, valores)
    conexao.commit()

def excluir_musica(musica_id):
    excluir_sql = "DELETE FROM playlist WHERE id=%s"
    valores = (musica_id,)
    cursor.execute(excluir_sql, valores)
    conexao.commit()

criar_tabela()

adicionar_musica("Chop Suey!", "System of a Down", "Toxicity", 210)
adicionar_musica("Aerials", "System of a Down", "Toxicity", 237)
adicionar_musica("B.Y.O.B.", "System of a Down", "Mezmerize", 244)

print("Playlist inicial:")
visualizar_playlist()

atualizar_musica(1, "Chop Suey! (Remix)", "System of a Down", "Toxicity", 215)

# Visualizar a playlist após a atualização
print("\nPlaylist após atualização:")
visualizar_playlist()

excluir_musica(2)

print("\nPlaylist após exclusão:")
visualizar_playlist()

cursor.close()
conexao.close()
