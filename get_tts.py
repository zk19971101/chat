import edge_tts
import asyncio

TEXT = ""

TEXT = "你好，很高兴见到你！"
voice = 'zh-CN-YunxiNeural'
output = './text2voicetest.wav'


async def my_function(text, output, voice):
    tts = edge_tts.Communicate(text=text, voice=voice)
    await tts.save(output)


def get_tts(text, save_path, voice='zh-CN-YunxiNeural'):
    asyncio.run(my_function(text, save_path, voice))


if __name__ == '__main__':
    get_tts(TEXT, output)