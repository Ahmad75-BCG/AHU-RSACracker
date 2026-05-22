#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# https://github.com/Ahmad75-BCG 

from Crypto.Util.number import long_to_bytes
from colorama import Fore, Style, init
import sys
import time

init(autoreset=True)

def banner():
    print(Fore.CYAN + r"""

    █████╗ ██╗  ██╗██╗   ██╗
   ██╔══██╗██║  ██║██║   ██╗
   ███████║███████║██║   ██║
   ██╔══██║██╔══██║██║   ██╗
   ██║  ██║██║  ██║╚██████╔╝
   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝

██████╗ ███████╗ █████╗  ██████╗██████╗  █████╗  ██████╗██╗  ██╗███████╗██████╗
██╔══██╗██╔════╝██╔══██╗██╔════╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝██╔════╝██╔══██╗
██████╔╝███████╗███████║██║     ██████╔╝███████║██║     █████╔╝ █████╗  ██████╔╝
██╔══██╗╚════██║██╔══██║██║     ██╔══██╗██╔══██║██║     ██╔═██╗ ██╔══╝  ██╔══██╗
██║  ██║███████║██║  ██║╚██████╗██║  ██║██║  ██║╚██████╗██║  ██╗███████╗██║  ██║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝

         RSA Factorization Framework
        Developed By AhmadAbugaith_75
        GitHub: https://github.com/Ahmad75-BCG
        Al Hussein Bin Talal University - AHU
              Cyber Security Department

""" + Style.RESET_ALL)

def loading(message):
    print(Fore.YELLOW + f"\n[*] {message}..." + Style.RESET_ALL)
    time.sleep(1)

def success(message):
    print(Fore.GREEN + f"[+] {message}" + Style.RESET_ALL)

def error(message):
    print(Fore.RED + f"[!] {message}" + Style.RESET_ALL)

def info(message):
    print(Fore.CYAN + f"[-] {message}" + Style.RESET_ALL)

def separator():
    print(Fore.BLUE + "\n" + "=" * 70 + Style.RESET_ALL)

banner()

try:

    info("Enter RSA Public Parameters")

    n_input = input(
        Fore.WHITE +
        "Enter Modulus (n): " +
        Style.RESET_ALL
    )

    e_input = input(
        Fore.WHITE +
        "Enter Public Exponent (e) [Default: 65537]: " +
        Style.RESET_ALL
    )

    c_input = input(
        Fore.WHITE +
        "Enter Ciphertext (c): " +
        Style.RESET_ALL
    )

    n = int(n_input.strip())

    e = int(e_input.strip()) if e_input.strip() else 65537

    c = int(c_input.strip())

    loading("Loading RSA Parameters")

    success("RSA public parameters loaded successfully")

    separator()

    print(
        Fore.MAGENTA +
        "[ Factordb Recovered Prime Factors ]" +
        Style.RESET_ALL
    )

    p_input = input(
        Fore.WHITE +
        "Enter Prime Factor (p): " +
        Style.RESET_ALL
    )

    q_input = input(
        Fore.WHITE +
        "Enter Prime Factor (q): " +
        Style.RESET_ALL
    )

    p = int(p_input.strip())
    q = int(q_input.strip())

    separator()

    loading("Verifying factorization")

    if p * q != n:
        error("Factorization verification failed")
        error("The product of p and q does not equal n")
        sys.exit()

    success("Prime factors verified successfully")

    separator()

    loading("Calculating Euler Totient Function")

    phi = (p - 1) * (q - 1)

    success("Phi(n) calculated successfully")

    loading("Recovering RSA private key")

    d = pow(e, -1, phi)

    success("Private key recovered successfully")

    print(
        Fore.GREEN +
        "\n[ PRIVATE KEY d ]\n" +
        Style.RESET_ALL
    )

    print(Fore.WHITE + str(d) + Style.RESET_ALL)

    separator()

    loading("Decrypting ciphertext")

    decrypted_integer = pow(c, d, n)

    success("Ciphertext decrypted successfully")

    print(
        Fore.YELLOW +
        "\n[ DECRYPTED INTEGER ]\n" +
        Style.RESET_ALL
    )

    print(Fore.WHITE + str(decrypted_integer) + Style.RESET_ALL)

    separator()

    decrypted_bytes = long_to_bytes(decrypted_integer)

    print(
        Fore.CYAN +
        "\n[ RAW BYTES ]\n" +
        Style.RESET_ALL
    )

    print(Fore.WHITE + str(decrypted_bytes) + Style.RESET_ALL)

    print(
        Fore.CYAN +
        "\n[ HEX OUTPUT ]\n" +
        Style.RESET_ALL
    )

    print(Fore.WHITE + decrypted_bytes.hex() + Style.RESET_ALL)

    separator()

    try:

        flag = decrypted_bytes.decode("utf-8")

        print(
            Fore.GREEN +
            "\n[ FLAG FOUND SUCCESSFULLY ]\n" +
            Style.RESET_ALL
        )

        print(
            Fore.GREEN +
            f">>> {flag}\n" +
            Style.RESET_ALL
        )

    except UnicodeDecodeError:

        error("Unable to decode UTF-8 text")
        info("The decrypted content may be binary data")

except KeyboardInterrupt:

    error("Operation cancelled by user")

except ValueError:

    error("Invalid numeric input detected")

except Exception as ex:

    error(f"Unexpected Error: {ex}")