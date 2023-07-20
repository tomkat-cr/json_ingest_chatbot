img_width = "28px"
img_height = "28px"
img_basse_path = "https://github.com/tomkat-cr/json_ingest_chatbot/raw/main"
icon_chatbot = f"{img_basse_path}/assets/icon_chatbot.jpeg"
icon_human = f"{img_basse_path}/assets/icon_human.jpeg"

css = '''
<style>
.chat-message {
    padding: 1.5rem; border-radius: 0.5rem; margin-bottom: 1rem; display: flex
}
.chat-message.user {
    background-color: #2b313e
}
.chat-message.bot {
    background-color: #475063
}
.chat-message .avatar {
  width: 5%;
}
.chat-message .avatar img {
  max-width: ''' + img_width + ''';
  max-height: ''' + img_height + ''';
  border-radius: 50%;
  object-fit: cover;
}
.chat-message .message {
  width: 95%;
  padding: 0 0.5rem;
  color: #fff;
}
'''

bot_template = '''
<div class="chat-message bot">
    <div class="avatar">
        <img
            src="''' + icon_chatbot + '''"
            style="max-height: ''' + img_height + ''';
            max-width: ''' + img_width + ''';''' + \
            ''' border-radius: 50%; object-fit: cover;"
        >
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''

user_template = '''
<div class="chat-message user">
    <div class="avatar">
        <img
            src="''' + icon_human + '''"
            style="max-height: ''' + img_height + ''';
            max-width: ''' + img_width + ''';''' + \
            ''' border-radius: 50%; object-fit: cover;"
        >
    </div>
    <div class="message">{{MSG}}</div>
</div>
'''
