import werobot
robot = werobot.WeRoBot(token='vkwechat')

@robot.handler
def index(message):
    return 'Today is wonderful day!'