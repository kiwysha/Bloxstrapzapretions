import ctypes

def show_native_error():
    title = "Error"
    message = (
        "Roblox encountered an unexpected error.\n"
        "Click 'OK' to create support files, then please share it on our site: "
        "https://roblox.com/support"
    )

    # Флаги: MB_OKCANCEL (кнопки OK и Отмена) + MB_ICONERROR (красный крест)
    MB_OKCANCEL = 0x00000001
    MB_ICONERROR = 0x00000010
    flags = MB_OKCANCEL | MB_ICONERROR

    # Вызов MessageBoxW из user32.dll
    ctypes.windll.user32.MessageBoxW(0, message, title, flags)

if __name__ == "__main__":
    show_native_error()