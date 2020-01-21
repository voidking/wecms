from django.conf import settings
import werobot
from werobot.replies import ImageReply

robot = werobot.WeRoBot(token=settings.TOKEN)
robot.config['APP_ID'] = settings.APP_ID
robot.config['APP_SECRET'] = settings.APP_SECRET
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

@robot.subscribe
def subscribe(event):
    print('用户' + event.source + '关注了公众号')
    return '感谢关注voidking，您的ID为：' + event.source

@robot.unsubscribe
def unsubscribe(event):
    print('用户' + event.source + '取消了关注')
    return ''
