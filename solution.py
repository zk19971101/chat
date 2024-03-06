import os
import edge_tts
import asyncio
import stable_whisper as whisper

from pydub import AudioSegment
from pydub.playback import play
from get_audio import get_audio
from get_xinghuo import running


async def text2speech(text, output):
    voice = 'zh-CN-YunxiNeural'
    tts = edge_tts.Communicate(text=text, voice=voice)
    await tts.save(output)


class ChatModel:
    def __init__(self, model_name="large-v2"):
        self.audio_path = "tempt.wav"
        self.answer_path = "answer.wav"
        self.answer = "new_answer.wav"
        self.whisper = whisper.load_model(model_name)
        print("模型初始化成功！")


    def communication(self):
        pass

    def running(self):
        answer = ""
        res = ""
        while True:
            input_text = ""
            audio_frames = get_audio(5, self.audio_path)
            input_text = self.whisper.transcribe(self.audio_path, fp16=False, language='Chinese')['text']
            tempt = answer
            res_text = running(input_text)
            res = res_text[len(tempt):]

            asyncio.run(text2speech(res, self.answer_path))

            os.system(f"ffmpeg -i {self.answer_path} {self.answer}")
            answer = AudioSegment.from_wav(self.answer)
            play(answer)
            os.remove(self.answer)
            os.remove(self.answer_path)
            os.remove(self.audio_path)


if __name__ == '__main__':
    model = ChatModel()
    model.running()