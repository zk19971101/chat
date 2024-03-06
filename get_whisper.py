import stable_whisper as whisper


class WhisperTranscriber(object):

    def __init__(self, model_name):
        self.model = whisper.load_model(model_name)

    def whisper_transcribe(self, audio_path):
        audio = self.model.transcribe(audio_path, fp16=False, language='Chinese')
        return audio['text']


def get_whisper(audio_path, model_para: str="large-v2"):
    transcriber = WhisperTranscriber(model_para)
    text = transcriber.whisper_transcribe(audio_path)
    return text


if __name__ == '__main__':
    transcriber = WhisperTranscriber("large-v2")
    text = transcriber.whisper_transcribe("output.wav")
    print(text)
