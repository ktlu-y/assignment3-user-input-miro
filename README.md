# assignment-template
# assignment-template
SD5913 - Lu Yao - Assignment 2

Introduction of Music bot Miro
I created a music bot named Miro. She is able to cheer you up when you are in your gloomy days; and celebrate for you when you are happy. All you have to do is to enter several keywords that can represent your emotions (3-4 keywords are suggested). Then Miro will generate multiple musics in (.wav) file type for you (how many keywords you enter, how many music you will finally get).
All the dialogue and commands will be conducted in the Terminal. No extra interface will appear. The (.wav) file will be saved in the current folder.

Required Libraries
torch: The core library for PyTorch, which torchaudio depends on.
torchaudio: The audio processing library for PyTorch.
audiocraft: The library for music generation (specifically for using the MAGNeT model).
numpy: Often required for numerical operations, even though it's not explicitly imported in your code.

Installation Commands
You can install the above packages using pip. Here’s a consolidated command to install them:
pip install torch torchaudio audiocraft numpy

Additional Considerations
CUDA Support: Ensure you install the correct version of PyTorch with CUDA support. 
You can find the appropriate command for your system on the PyTorch website.
