from pydub import AudioSegment
from pydub.silence import split_on_silence

# AudioSegment.converter = r"D:\Program Files\ffmpeg_cuda\ffmpeg-4.4-full_build\bin\ffmpeg.exe"
# AudioSegment.ffmpeg = r"D:\Program Files\ffmpeg_cuda\ffmpeg-4.4-full_build\bin\ffmpeg.exe"
# AudioSegment.ffprobe =r"D:\Program Files\ffmpeg_cuda\ffmpeg-4.4-full_build\bin\ffprobe.exe"

sound = AudioSegment.from_mp3(r'c:\test\ZOOM0003.MP3')
chunks = split_on_silence(
    sound,

    # split on silences longer than 1000ms (1 sec)
    min_silence_len=500,

    # anything under -16 dBFS is considered silence
    silence_thresh=-50 #, 

    # keep 200 ms of leading/trailing silence
    #keep_silence=20
)


#AudioSegment.export()

# now recombine the chunks so that the parts are at least 90 sec long
#target_length = 90 * 1000
#output_chunks = [chunks[0]]
#chk =0
for i, chunk in enumerate(chunks): #chunks[1:]:
    #mp3name = "chnk" + str(i)
    print("Exporting chunk{0}.mp3.".format(i))
    chunk.export("c:/test/chunk{0}.mp3".format(i),
        bitrate = "192k",
        format = "mp3")
    

    # if len(output_chunks[-1]) < target_length:
    #     output_chunks[-1] += chunk
    # else:
    #     # if the last output chunk is longer than the target length,
    #     # we can start a new one
    #     output_chunks.append(chunk)

# now your have chunks that are bigger than 90 seconds (except, possibly the last one)