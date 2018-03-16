import time
import math
from openal.audio import SoundSink, SoundSource
from openal.loaders import load_wav_file

if __name__ == "__main__":
    sink = SoundSink()
    sink.activate()
    source = SoundSource(position=[0, 0, 0])
    source.looping = True
    data = load_wav_file("bullet_mono.WAV")
    source.queue(data)
    sink.play(source)
    t = 0
    while True:
        x_pos = 5*math.sin(math.radians(t))
        source.position = [x_pos, source.position[1], source.position[2]]
        sink.update()
        print("playing at %r" % source.position)
        time.sleep(0.1)
        t += 5