# Flow control file
import speech_recognition as sr
from process_sound import transcript_mic
from metronome import metronome


MIC_RUN_TIME = 100


if __name__ == "__main__":
    # Get the default microphone
    microphone = sr.Microphone()
    # Getting the input from the microphone
    ret_str: str = transcript_mic(microphone, phrase_time_limit=MIC_RUN_TIME)
    # Print the returned string
    print(ret_str)
    # Print the number of words and WPM
    print(metronome(ret_str), metronome(ret_str, MIC_RUN_TIME))
