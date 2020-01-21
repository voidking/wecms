import werobot
from werobot.replies import ImageReply

robot = werobot.WeRoBot(token='vkwechat')
robot.config['APP_ID'] = 'app_id'
robot.config['APP_SECRET'] = 'app_secret'
client = robot.client

@robot.handler
def index(message):
    return 'Today is wonderful day!'

@robot.filter('image')
def media(message):
    media_id = client.upload_permanent_media('image', open(r'C:\Users\haojin\Desktop\favicon.png', 'rb'))['media_id']
    reply = ImageReply(message=message, media_id=media_id)
    return reply

@robot.text
def text(message):
    return '您发送了文本消息，内容为：' + message.content

@robot.image
def image(message):
    return '您发送了图片消息，图片为：' + message.img

@robot.link
def link(message):
    return '您发送了链接消息，链接为：' + message.url

@robot.location
def location(message):
    return '您发送了位置消息，位置为：' + message.label

@robot.voice
def voice(message):
    return '您发送了声音消息，media_id为：' + message.media_id

@robot.video
def video(message):
    return '您发送了视频消息，media_id为：' + message.media_id