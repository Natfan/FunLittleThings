import ffmpeg

def tone(hz1, hz2):
    stream1 = ffmpeg.input("sine=frequency=" + hz1 + ":duration=1")
    stream2 = ffmpeg.input("sine=frequency=" + hz2 + ":duration=1")
    stream = ffmpeg.filter_('amerge', stream1, stream2)
    stream = ffmpeg.output(stream, 'test.wav')
    #ffmpeg.run(stream)

tone('1209', '697')
