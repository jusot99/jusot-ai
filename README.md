# Linux Assistant (Jusot AI)

![Python](https://img.shields.io/badge/python-3.x-blue.svg)
![Pygame](https://img.shields.io/badge/pygame-2.x-green.svg)
![Colorama](https://img.shields.io/badge/colorama-0.4.4-yellow.svg)
![NLTK](https://img.shields.io/badge/nltk-3.5-orange.svg)
![GitHub](https://img.shields.io/github/license/jusot99/jusot-ai)
![Contributions](https://img.shields.io/badge/contributions-welcome-brightgreen.svg)

Welcome to the Linux Assistant (Jusot AI) by Elimane! This AI-powered assistant can help you with various Linux-related tasks and answer general questions.

## Features

- **Greetings:** Responds to basic greetings.
- **Owner Information:** Provides the name of the owner.
- **Capabilities:** Describes what the assistant can do.
- **Port Scanning:** Scans ports on a specified IP address.
- **Sound Effects:** Plays sounds for certain interactions.
- **Help Command:** Lists available commands and provides assistance.

## Getting Started

### Prerequisites

Make sure you have the following installed:

- Python 3.x
- Required Python packages (install using the command below)
- Git (for cloning the repository)
- Pygame (for sound effects)
- Colorama (for colored terminal output)
- NLTK (for chat utilities)

### Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/jusot99/jusot-ai.git
   cd jusot-ai
   ```

2. **Install Required Packages:**

   ```bash
   pip install pygame colorama nltk
   ```

3. **Download NLTK Data:**

   ```python
   import nltk
   nltk.download('punkt')
   ```

4. **Add Sound Files:**

   Ensure you have a `sounds` directory in the same location as `jusot_ai.py`, containing the necessary sound files like `wake.mp3`, `thinking.mp3`, and `shutdown.mp3`.

### Running the Assistant

Run the script using Python:

```bash
python jusot_ai.py
```

### Usage

- **Greet the Assistant:**
  ```
  Elimane: Hi
  ```
- **Ask for the Assistant's Name:**
  ```
  Elimane: What is your name?
  ```
- **Ask for Owner's Information:**
  ```
  Elimane: Who is your owner?
  ```
- **Scan Ports on an IP Address:**
  ```
  Elimane: Scan ports on 192.168.1.1
  ```
- **Get Help:**
  ```
  Elimane: Help
  ```

## Contributing

Feel free to fork this repository, make improvements, and submit pull requests. Contributions are always welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- **Python:** For the programming language.
- **Pygame:** For sound effects.
- **Colorama:** For colored terminal output.
- **NLTK:** For natural language processing utilities.

## Author

- **Elimane** - Creator and maintainer of the project.
