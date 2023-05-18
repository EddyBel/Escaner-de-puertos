import socket
import psutil
import asyncio
import timeit


class FileManager:
    """ Esta clase maneja los metodos que se encargan de leer y escribir archivos. """

    @staticmethod
    def read_file(path):
        with open(path, mode="r", encoding="utf-8") as file:
            content = file.read()
        return content

    @staticmethod
    def write_file(path, content):
        with open(path, "a") as file:
            file.write(content)

    @staticmethod
    def clear_log_file(path):
        with open(path, "w") as log_file:
            log_file.write("")


class ViewsManager:
    """ Esta clase se encarga de manejar algunos aspectos que el usuario ve en la terminal como imprimir la barra de progreso. """

    @staticmethod
    def print_time(time: float) -> None:
        data = f"""
        
        Hours: {round((time / 60) / 60, 2)} h
        Minutes: {round(time / 60, 2)} m
        Seconds: {round(time , 2)} s
        """
        print(data)

    @staticmethod
    def progress_bar(total: float, i: float, length: int, fill_char: str = "*", contact="") -> None:
        # Calcula el porcentaje de completado
        # Muestra el número de puertos escaneados
        # Calcula la longitud de la barra de progreso
        percent = int((i) / total * 100)
        count = f"{i} / {total}"
        filled_length = int(length * (i) // total)

        # Crea la barra de progreso
        bar = fill_char * filled_length + '.' * (length-filled_length)
        print(f"Scanning: {percent}% |{bar}| {count} {contact}|", end="\r")


class Scanner (FileManager, ViewsManager):

    def __init__(self, ports=65535, breaks=500, sleep=0, length_bar=40, progress_container="█", path_file="log.txt") -> None:
        # Propieades a utilizar
        self.PORTS = ports
        self.BREAKS = breaks
        self.SLEEP = sleep
        self.PROGRESS_CONTAINER = progress_container
        self.LENGTH_BAR = length_bar
        self.PATH_FILE = path_file

        # Condifiones a tomar en cuenta
        self.SAVE_DATA = True
        self.PRINT_TIME = True
        self.PRINT_RESULT = True
        self.PRINT_IP = True

    def get_local_ip(self, dns: str = "8.8.8.8"):
        """ Esta funcion obtiene la IP del dispositivo local """
        # Se conecta temporalmente a un servidor DNS para obtener la dirección IP local
        # Obtiene la dirección IP local del equipo
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((dns, 80))
        ip_address = s.getsockname()[0]
        s.close()
        return ip_address

    def _get_process_name(self, port: int):
        """ Esta funcion obtiene el nombre del procesao que esta usando ese puerto """
        # Utiliza la biblioteca psutil para obtener todas las conexiones de red TCP activas en el equipo
        for conn in psutil.net_connections(kind="tcp"):
            # Si encuentra una conexión que utiliza el puerto específico
            if conn.laddr.port == port:
                # Obtiene el nombre del proceso, el ID de proceso y el estado del proceso que está utilizando el puerto
                return {
                    "name": psutil.Process(conn.pid).name(),
                    "code": psutil.Process(conn.pid).pid,
                    "status": psutil.Process(conn.pid).status()
                }

    async def _scan_port(self, ip_address: str, port: int) -> (dict or None):
        """ Esta funcion escanea un puerto y reviza si tiene una conexión """
        try:
            # Intenta conectar con la dirección IP y el puerto específicos
            # Obtiene el nombre del proceso que está utilizando el puerto
            # Retorna un objeto con todas las propiedades necesarias
            reader, writer = await asyncio.open_connection(ip_address, port)
            process_name = self._get_process_name(port)
            name = process_name["name"]
            code = process_name["code"]
            status = process_name["status"]
            writer.close()

            # Guarda los resultados en un archivo de registro si asi se quiere
            if self.SAVE_DATA:
                self.write_file(
                    self.PATH_FILE, f"{ip_address}:{port} - {name} - {status} - {code}\n")
            return {
                "port": port,
                "name": name,
                "code": code,
                "status": status
            }
        except:
            return None

    async def run(self) -> (str or None):
        """ Esta función inicia el escaneo de todos los puertos del equipo """

        # Obten la IP del dispositivo
        # Muestra que IP sera escaneada
        IP_ADDRESS = self.get_local_ip()
        if self.PRINT_IP:
            print(f"IP: {IP_ADDRESS}\n")

        # Variables que se utilizaran a lo largo de la ejecución
        tasks = []
        counter_blocks = 0

        # Si se quiere guardar el contenido del escaneo entonces borra el contenido del archivo de log
        if self.SAVE_DATA:
            self.clear_log_file(self.PATH_FILE)

        # Obten la fecha actual que servira para contar el tiempo de ejecución del programa
        start_time = timeit.default_timer()

        # Inicia el bucle de código que va a escanear los puertos
        # Cada bucle divide el rango que se usara para escanear puertos
        for value in range(0, self.PORTS, self.BREAKS):
            counter_blocks += 1  # Suma el bloque transcurrido

            # Este bucle recorre los datos en cada bloque
            # Crea una tarea por cada puerto a escanear para que se escanee de manera independiente y sea mas veloz
            # Guarda la tarea en la lista de tareas
            for port in range(value, value + self.BREAKS):
                tasks.append(asyncio.create_task(
                    self._scan_port(IP_ADDRESS, port)))

            # Espera a que todas las tareas hayan sido concluidas
            # Crea una lista que contenga las tareas terminadas
            # Imprime la barra de tareas con referencia a la lista de tareas termiadas
            await asyncio.gather(*tasks)
            completed_tasks = [task for task in tasks if task.done()]
            self.progress_bar(self.PORTS, len(completed_tasks), self.LENGTH_BAR,
                              self.PROGRESS_CONTAINER, f"Block: {counter_blocks}")

        # Obten el tiempo al finalizar todos los puertos
        end_time = timeit.default_timer()
        for task in tasks:
            task.cancel()  # Una vez el proceso de escaneo haya finalizado eliminaremos las tareas

        # Muestra el tiempo que le tomo ejecutarse si asi se indica
        if self.PRINT_TIME:
            self.print_time(end_time - start_time)

        # Muestra el resultado si asi se indica
        if self.PRINT_RESULT:
            content = self.read_file(self.PATH_FILE)
            print(content)


if __name__ == "__main__":
    scanner = Scanner()
    asyncio.get_event_loop().run_until_complete(scanner.run())
