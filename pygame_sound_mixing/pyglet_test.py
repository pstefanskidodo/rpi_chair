import pyglet

#pyglet.options['audio'] = ('openal', 'pulse', 'alsa', 'silent')
pyglet.options['audio'] = ('alsa', 'openal', 'silent')
abc = pyglet.media.load('bullet_mono.WAV', streaming = False)
abc.play()
pyglet.app.run()