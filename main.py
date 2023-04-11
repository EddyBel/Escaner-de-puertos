import socket
import psutil
import asyncio
import timeit

PORTS = 65535
BLOCKS = 131
SLEEP = 0
FILE = "log.txt"


def read_file(path):
    with open(path, mode="r", encoding="utf-8") as file:
        return file.read()


def clear_log_file(path):
    with open(path, "w") as log_file:
        log_file.write("")


def write_file(path, content):
    with open(path, "a") as file:
        file.write(content)

# Función que obtiene la dirección IP local del equipo


def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Se conecta temporalmente a un servidor DNS para obtener la dirección IP local
    s.connect(("8.8.8.8", 80))
    # Obtiene la dirección IP local del equipo
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address

# Función que obtiene el nombre del proceso que está utilizando un puerto específico


def get_process_name(port):
    # Utiliza la biblioteca psutil para obtener todas las conexiones de red TCP activas en el equipo
    for conn in psutil.net_connections(kind="tcp"):
        if conn.laddr.port == port:  # Si encuentra una conexión que utiliza el puerto específico
            # Obtiene el nombre del proceso, el ID de proceso y el estado del proceso que está utilizando el puerto
            return {
                "name": psutil.Process(conn.pid).name(),
                "code": psutil.Process(conn.pid).pid,
                "status": psutil.Process(conn.pid).status()
            }

# Función asíncrona que escanea un puerto en una dirección IP específica y guarda el resultado en un archivo de registro


async def scan_port(ip_address, port):
    try:
        # Intenta conectar con la dirección IP y el puerto específicos
        reader, writer = await asyncio.open_connection(ip_address, port)
        # Obtiene el nombre del proceso que está utilizando el puerto
        process_name = get_process_name(port)
        name = process_name["name"]
        code = process_name["code"]
        status = process_name["status"]
        # Guarda los resultados en un archivo de registro llamado "log.txt"
        write_file(FILE, f"{ip_address}:{port} - {name} - {status} - {code}\n")
        writer.close()
    except:
        pass

# Función que muestra una barra de progreso mientras se escanean los puertos


def progress_bar(total, i, length, fill_char, contact=""):
    percent = int((i)/total*100)  # Calcula el porcentaje de completado
    count = f"{i} / {total}"  # Muestra el número de puertos escaneados
    # Calcula la longitud de la barra de progreso
    filled_length = int(length*(i)//total)
    bar = fill_char*filled_length + ' ' * \
        (length-filled_length)  # Crea la barra de progreso
    # Muestra la barra de progreso y el número de puertos escaneados
    print(f"Progress: {percent}% |{bar}| {count} {contact}", end="\r")


# Funcion principal que ejecuta el escaneo
async def main():
    ip_address = get_local_ip()
    print(f"IP: {ip_address}")

    tasks = []
    count = 1
    count_block = 0

    clear_log_file(FILE)
    start_time = timeit.default_timer()
    progress_bar(PORTS, 0, 50, "*", f"Block: {count_block}")
    for x in range(0, PORTS, int(PORTS/BLOCKS)):
        count_block += 1
        # print(f"Fragmento {x} a {x + int(PORTS/BLOCKS)}\n")

        for port in range(x, x + int(PORTS/BLOCKS)):
            scan_task = asyncio.create_task(scan_port(ip_address, port))
            tasks.append(scan_task)

        while True:
            all_tasks_completed = True

            for task in tasks:
                if not task.done():
                    all_tasks_completed = False
                    break

            if all_tasks_completed:
                break

            completed_tasks = [task for task in tasks if task.done()]
            progress_bar(PORTS, len(completed_tasks), 50,
                         "*", f"Block: {count_block}")

            await asyncio.sleep(SLEEP)

    end_time = timeit.default_timer()
    await asyncio.gather(*tasks)

    print()
    print("+--------------------------------------------------+")
    print(f"Time: {round(((end_time - start_time)/60)/60, 2)} hour")
    print(f"Time: {round((end_time - start_time)/60, 2)} min")
    print(f"Time: {round(end_time - start_time, 2)} sec")
    print("+--------------------------------------------------+")
    print()

    content = read_file(FILE)
    print(content)

if __name__ == "__main__":
    asyncio.run(main())
