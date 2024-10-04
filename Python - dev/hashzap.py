# Título: Hashzap
# Botão de iniciar Chat
    # Popup (janela na frente da tela)
    # Título: Bem vindo ao Hashzap
    # Campo de nameo -> Escreva sue nome no chat
    # Botão: Entrar no chat
        # Sumir com o título hashzap
        # Fechar a janela (popup)
        # Carregar o chat
            # As mensagens que já foram enviadas (Chat)
            # Campo: Digite sua mensagem
            # Botão de enviar
# Pip install flet -> no seu terminal

# Importar o felt
import flet as ft

# Criar a função principal
def main(page):
    # Criar todas as funcionalidades

    # Cria o elemento
    title = ft.Text("Hashzap")

    title_popup = ft.Text("Bem vindo ao Hashzap")
    name_field = ft.TextField(label="Escreva seu nome no chat")

    chat = ft.Column()

    def chat_tunnel(text_message):
        text_chat = ft.Text(text_message)
        chat.controls.append(text_chat)
        page.update()

    page.pubsub.subscribe(chat_tunnel)

    def send_message(evento):
        message = message_field.value
        username = name_field.value
        text_message = f"{username}: {message}"
        page.pubsub.send_all(text_message)
        message_field.value = ""
        page.update()

    message_field = ft.TextField(label="Digite sua mensagem", on_submit = send_message)
    send_button = ft.ElevatedButton("Enviar", on_click= send_message)
    
    line = ft.Row([message_field, send_button])
    def enter_chat(evento):
        page.remove(title)
        page.remove(start_button)
        popup.open = False
        page.add(chat)
        page.add(line)
        text_message = f"{name_field.value} entrou no chat"
        page.pubsub.send_all(text_message)
        page.update()
    
    enter_button = ft.ElevatedButton("Entrar no chat", on_click= enter_chat)
    popup = ft.AlertDialog(title = title_popup, content = name_field, actions = [enter_button])

    def start_chat(evento):
        page.dialog = popup
        popup.open = True
        page.update()  
    
    start_button = ft.ElevatedButton("Iniciar Chat", on_click = start_chat)

    # Adiciona o elemento na página
    page.add(title)
    page.add(start_button)

    # Rodar seu aplicativo
ft.app(main, view =ft.WEB_BROWSER)