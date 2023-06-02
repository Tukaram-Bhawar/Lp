def columnar_transposition_encrypt(message, key):
    # Remove any spaces from the message
    message = message.replace(" ", "")

    # Calculate the number of rows based on the message length and key length
    rows = -(-len(message) // len(key))  # Ceiling division

    # Pad the message with spaces if necessary
    message += " " * (rows * len(key) - len(message))

    # Create the transposition grid
    grid = [message[i::len(key)] for i in range(len(key))]

    # Generate the encrypted message by reading the grid column by column
    encrypted_message = "".join(grid)

    return encrypted_message


def columnar_transposition_decrypt(ciphertext, key):
    # Calculate the number of rows based on the ciphertext length and key length
    rows = -(-len(ciphertext) // len(key))  # Ceiling division

    # Calculate the number of empty cells in the last row
    empty_cells = rows * len(key) - len(ciphertext)

    # Create the transposition grid
    grid = [ciphertext[i::rows] for i in range(rows)]

    # Remove the empty cells in the last row if present
    if empty_cells > 0:
        grid[-1] = grid[-1][:-empty_cells]

    # Generate the decrypted message by reading the grid row by row
    decrypted_message = "".join(grid)

    return decrypted_message


# Example usage
message = "HELLO WORLD"
key = "COLUMNAR"

encrypted_message = columnar_transposition_encrypt(message, key)
print("Encrypted message:", encrypted_message)

decrypted_message = columnar_transposition_decrypt(encrypted_message, key)
print("Decrypted message:", decrypted_message)
