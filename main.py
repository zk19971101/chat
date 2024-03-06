import os
import asyncio
import edge_tts
import stable_whisper as whisper

from pydub import AudioSegment
from pydub.playback import play

from get_audio import get_audio
from get_xinghuo import running


async def text2speech(text, output):
    voice = 'zh-CN-YunxiNeural'
    tts = edge_tts.Communicate(text=text, voice=voice)
    await tts.save(output)


if __name__ == '__main__':
    audio_path = "./test.wav"
    res_audio_path = "./tempt.wav"
    answer = ""
    res = ""
    whisper = whisper.load_model("large-v2")
    while True:
        audio_frames = get_audio(5, audio_path)
        input_text = whisper.transcribe(audio_path, fp16=False, language='Chinese')['text']

        tempt = answer
        answer = running(input_text)
        res_text = answer[len(tempt):]

        asyncio.run(text2speech(res_text, res_audio_path))
        os.system(f"ffmpeg -i {res_audio_path} t.wav")
        song = AudioSegment.from_wav("t.wav")
        play(song)
        os.remove("t.wav")
        os.remove(audio_path)
        os.remove(res_audio_path)


