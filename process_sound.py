import speech_recognition as sr


def transcript_mic(mic: sr.Microphone, noise_filter_duration: int = 0, phrase_time_limit: int = 10) -> str:
    r"""
    Extracte words from a voice stream

    Parameters
    ----------
    mic : sr.Microphone
        The microphone to work with
    noise_filter_duration : int, default 0
        The time used to calibrate the noise filtering
    phrase_time_limit : int, default 10
        How long to keep the microphone on

    Returns
    -------
    str
        The extracte words
    """
    recognizer = sr.Recognizer()
    with mic as source:
        recognizer.adjust_for_ambient_noise(
            source, duration=noise_filter_duration)
        audio = recognizer.listen(source, phrase_time_limit=phrase_time_limit)
    return recognizer.recognize_google(audio)
