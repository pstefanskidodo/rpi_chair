from openal import al, alc    # imports all relevant AL and ALC functions

def main():
    source = al.ALuint()
    device = alc.alcOpenDevice(None)
    if not device:
        error = alc.alcGetError()
        # do something with the error, which is a ctypes value
        return -1
    # Omit error checking
    context = alc.alcCreateContext(device, None)
    alc.alcMakeContextCurrent(context)

    # Do more things
    al.alGenSources(1, source)
    al.alSourcef(source, al.AL_PITCH, 1)
    al.alSourcef(source, al.AL_GAIN, 1)
    al.alSource3f(source, al.AL_POSITION, 10, 0, 0)
    al.alSource3f(source, al.AL_VELOCITY, 0, 0, 0)
    al.alSourcei(source, al.AL_LOOPING, 1)

    al.alDeleteSources(1, source)
    alc.alcDestroyContext(context)
    alc.alcCloseDevice(device)
    return 0

if __name__ == "__main__":
    raise SystemExit(main())