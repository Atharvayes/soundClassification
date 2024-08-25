import librosa
import numpy as np 


def extract_features(audio_file):
  y, sr = librosa.load(audio_file)
  mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
  return mfccs

def calculate_similarity(audio_file1, audio_file2):
  mfccs1 = extract_features(audio_file1)
  mfccs2 = extract_features(audio_file2)
  min_length = min(mfccs1.shape[1], mfccs2.shape[1])
  mfccs1 = mfccs1[:, :min_length]
  mfccs2 = mfccs2[:, :min_length]
  
  # Normalize MFCCs
  mfccs1 = mfccs1 / np.linalg.norm(mfccs1)
  mfccs2 = mfccs2 / np.linalg.norm(mfccs2)
  
  similarity = np.dot(mfccs1.flatten(), mfccs2.flatten())
  return similarity

def find_closest_audio(audio_file1, audio_file2, audio_file3):
  similarity1 = calculate_similarity(audio_file1, audio_file3)
  similarity2 = calculate_similarity(audio_file2, audio_file3)
  
  if similarity1 > similarity2:
    return audio_file1
  else:
    return audio_file2

# Example usage
audio1 = '/content/footsteps-1.wav'
audio2 = '/content/truck-departing-01.wav'
audio3 = '/content/truck-departing-02.wav'

closest_audio = find_closest_audio(audio1, audio2, audio3)
print(f"Audio file closest to {audio3} is: {closest_audio}")
