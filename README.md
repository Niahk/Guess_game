# Guessing game
This is a simple gussesing game web application built with Flask.The game challenges users to guess a randomly generated number between 1 and 100.It will give the result as too low ,too high or correct.

## Features

- Random number generation
- user-friendly interface
- secure with flask's 'Secret_key'

## Prerequisities

- Python3.x
- Flask

### Running the application

1. You can generate a `SECRET_KEY` using the following Python script:

    ```python
    import secrets
    print(secrets.token_hex(16))
    ```
2. Run the application:

    ```bash
    python app.py
    ```
## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
