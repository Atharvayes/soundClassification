import sounddevice as sd
import numpy as np
import wave

# Parameters for the recording
duration = 10  # Duration of recording in seconds
sample_rate = 44100  # Sample rate (44100 samples per second)
channels = 1  # Mono audio (use 2 for stereo)

# File to save the recording
output_file = "recorded3.wav"

def record_audio():
    print("Recording started...")
    
    # Record audio
    recording = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=channels, dtype='int16')
    sd.wait()  # Wait for the recording to finish
    
    print("Recording finished...")
    
    # Save the recording to a file
    with wave.open(output_file, 'wb') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(2)  # Number of bytes per sample
        wf.setframerate(sample_rate)
        wf.writeframes(recording.tobytes())

    print(f"Recording saved as {output_file}")

# Call the function to start recording
record_audio()
