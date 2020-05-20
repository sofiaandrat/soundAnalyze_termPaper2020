from pydub import AudioSegment


def fromMp3ToWav(src):
    dst = str(src)[0: -3] + 'wav'
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")
    return dst