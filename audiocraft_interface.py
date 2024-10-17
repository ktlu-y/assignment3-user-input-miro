import torchaudio
from audiocraft.models import MAGNeT
from audiocraft.data.audio import audio_write

# Load a pretrained MAGNeT model
model = MAGNeT.get_pretrained('facebook/magnet-small-10secs')

# User enters keywords
user_input = input("Hello, I am music bot, Miro. Enter a music description (keyword), How many emotions you want put into? Separated them by commas:")
descriptions = [desc.strip() for desc in user_input.split(',')]  # Split user input string into list

# Generate music samples
wav = model.generate(descriptions)  # Generate audio samples

# Save the generated audio file
for idx, one_wav in enumerate(wav):
    # Save the resulting audio as a {idx}.wav file, with a loudness normalization of -14 db LUFS
    audio_write(f'{idx}.wav', one_wav.cpu(), model.sample_rate, strategy="loudness", loudness_compressor=True)

print("Completed. The file has been saved.")
