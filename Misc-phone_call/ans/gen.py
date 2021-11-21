import sys
import argparse
import numpy as np
import scipy.io.wavfile as wav


class DtmfGenerator:
    DTMF_TABLE = {
        "1": np.array([1209, 697]),
        "2": np.array([1336, 697]),
        "3": np.array([1477, 697]),
        "A": np.array([1633, 697]),
        "4": np.array([1209, 770]),
        "5": np.array([1336, 770]),
        "6": np.array([1477, 770]),
        "B": np.array([1633, 770]),
        "7": np.array([1209, 852]),
        "8": np.array([1336, 852]),
        "9": np.array([1477, 852]),
        "C": np.array([1633, 852]),
        "*": np.array([1209, 941]),
        "0": np.array([1336, 941]),
        "#": np.array([1477, 941]),
        "D": np.array([1633, 941]),
    }

    def __init__(
        self,
        phone_number: str,
        Fs: np.float = 20000,
        time: np.float = 0.2,
        delay: np.float = 0.2,
        amp: np.float = 0.5,
    ):
        self.signal = self.compose(phone_number, Fs, time, delay, amp)

    def __dtmf_function(
        self, number: str, Fs: np.float, time: np.float, delay: np.float, amp: np.float
    ) -> np.array:
        time_tone = np.arange(0, time, (1 / Fs))
        time_delay = np.arange(0, delay, (1 / Fs))

        tone_samples = amp * (
            np.sin(2 * np.pi * self.DTMF_TABLE[number][0] * time_tone)
            + np.sin(2 * np.pi * self.DTMF_TABLE[number][1] * time_tone)
        )
        delay_samples = np.sin(2 * np.pi * 0 * time_delay)

        return np.append(tone_samples, delay_samples)

    def compose(
        self,
        phone_number: str,
        Fs: np.float,
        time: np.float,
        delay: np.float,
        amp: np.float,
    ) -> np.array:
        signal = np.array([])
        for number in phone_number:
            tone_delay_signal = self.__dtmf_function(number, Fs, time, delay, amp)
            signal = np.append(signal, tone_delay_signal)
        return signal

if __name__ == "__main__":
    freq = 20000
    dtmf = DtmfGenerator(
        '133562619159396'
    )
    wav.write('out.wav', freq, dtmf.signal)

