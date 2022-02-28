import speech_recognition as sr
import metronome

print(metronome.transcript_mic(sr.Microphone(), 5, 10))

