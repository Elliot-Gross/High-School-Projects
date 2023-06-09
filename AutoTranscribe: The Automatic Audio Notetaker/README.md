# AutoTranscribe: The Automatic Audio Notetaker

This project is a simple yet powerful application designed to transcribe and summarize audio files. The application is a valuable tool aimed to aid students and teachers in generating efficient, organized notes without the hassle of manual typing. It leverages the OpenAI API for transcribing audio, which is subsequently summarized based on custom prompts. The resulting transcription summary can be conveniently downloaded as a markdown file. The user-friendly GUI of the application is designed using Tkinter. The summarized notes are output in the Markdown format to ensure well-structured, visually appealing presentation.

## Getting Started

Follow these instructions to get the application running on your local machine.

### Prerequisites

The application requires the following dependencies:

- Python 3
- OpenAI Python library
- PyDub library
- Tkinter library
- dotenv library

These dependencies can be installed via pip:

``` bash
pip install openai pydub tkinter python-dotenv
```

Additionally, an OpenAI API key is necessary to use the application. After obtaining the key, replace `YOUR API KEY` in the `.env` file:

```plaintext
OPENAI_API_KEY = YOUR API KEY
```

### Installation

Clone the repository to your local machine, or download the individual files.

### Running the Application

First, navigate to the directory where main.py is located.

To run the application, execute the following command:

``` bash
python main.py
```

If you've made `main.py` executable, you can run it by simply double-clicking the file.

## Usage

To use the application, follow these steps:

1. Click the 'Upload Audio File' button to select an audio file for transcription.
2. Click the 'Transcribe' button to transcribe and summarize the audio file.
3. Once the transcription is complete, you can download the summarized notes by clicking the 'Download Notes' button.

Note: You can customize the summarization prompts by modifying the `user_prompt.txt` and `example_prompt.txt` files to suit your needs.

## Contributing

If you wish to contribute to this project, feel free to fork the repository, make your changes, and open a pull request. For questions or discussions, kindly open an issue or contact me directly.
