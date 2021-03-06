from aubio import source, notes

filename = input("Ingres la ruta")

downsample = 1
samplerate = 44100 // downsample

win_s = 512 // downsample # fft size
hop_s = 256 // downsample # hop size

s = source(filename, samplerate, hop_s)
samplerate = s.samplerate

tolerance = 0.8

notes_o = notes("default", win_s, hop_s, samplerate)

print("%8s" % "time","[ start","vel","last ]")

# total number of frames read
total_frames = 0
while True:
    samples, read = s()
    new_note = notes_o(samples)
    if (new_note[0] != 0):
        note_str = ' '.join(["%.2f" % i for i in new_note])
        print(("%.6f" % (total_frames/float(samplerate)))+">>" +str(int(new_note[0]))
    total_frames += read
    if read < hop_s: break
