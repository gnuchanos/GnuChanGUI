import psutil

def check_program_running(program_name):
    # Tüm çalışan işlemleri kontrol ediyoruz
    for proc in psutil.process_iter(['name']):
        try:
            if program_name in proc.info['name']:
                print(f"{program_name} is currently running.")
                return
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            continue
    print(f"{program_name} is not running.")

# firefox'un açık olup olmadığını kontrol edelim
check_program_running("firefox")