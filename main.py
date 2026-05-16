import platform
import socket
import uuid
from datetime import datetime
from tkinter import filedialog, messagebox

import customtkinter as ctk
import psutil

try:
    import wmi
except ImportError:
    wmi = None

try:
    import winreg
except ImportError:
    winreg = None

LANG = "es"
LANGUAGE_OPTIONS = {"English": "en", "Español": "es"}

TRANSLATIONS = {
    "en": {
        "window_title": "SysInfoHub",
        "app_title": "System Info Hub",
        "refresh": "Refresh",
        "copy_report": "Copy report",
        "save_report": "Save report",
        "save_success": "Report saved to {path}",
        "save_error": "Failed to save report: {error}",
        "language_label": "Language:",
        "english": "English",
        "spanish": "Spanish",
        "general_section": "General",
        "operating_system_section": "Operating System",
        "cpu_section": "CPU",
        "gpu_section": "GPU",
        "memory_section": "Memory",
        "storage_section": "Storage",
        "network_section": "Network",
        "motherboard_bios_section": "Motherboard / BIOS",
        "microsoft_office_section": "Microsoft Office",
        "system_time": "System time",
        "hostname": "Hostname",
        "local_ip": "Local IP",
        "mac_address": "MAC address",
        "platform": "Platform",
        "os": "OS",
        "architecture": "Architecture",
        "python": "Python",
        "build": "Build",
        "registered_user": "Registered User",
        "install_date": "Install Date",
        "physical_cores": "Physical cores",
        "logical_processors": "Logical processors",
        "max_frequency": "Max frequency",
        "current_frequency": "Current frequency",
        "cpu_utilization": "CPU utilization",
        "name": "Name",
        "manufacturer": "Manufacturer",
        "max_clock_speed": "MaxClockSpeed",
        "socket": "Socket",
        "l2_cache": "L2 Cache",
        "l3_cache": "L3 Cache",
        "total_ram": "Total RAM",
        "available_ram": "Available RAM",
        "used_ram": "Used RAM",
        "swap_total": "Swap total",
        "drive": "Drive",
        "mountpoint": "Mountpoint",
        "file_system": "File system",
        "total_size": "Total size",
        "used": "Used",
        "free": "Free",
        "driver_version": "Driver version",
        "ram": "RAM",
        "video_processor": "Video processor",
        "status": "Status",
        "gpu_not_available": "GPU information not available",
        "interface": "Interface",
        "unknown_adapter": "Unknown adapter",
        "ip_addresses": "IP addresses",
        "subnets": "Subnets",
        "gateway": "Gateway",
        "dns_servers": "DNS servers",
        "dhcp_enabled": "DHCP enabled",
        "dhcp_server": "DHCP server",
        "dns_host_name": "DNS host name",
        "network_not_available": "Network information not available",
        "serial_number": "Serial number",
        "bios_version": "BIOS version",
        "bios_release_date": "BIOS release date",
        "motherboard_not_available": "Motherboard/BIOS information not available",
        "office_windows_only": "Microsoft Office details available only on Windows.",
        "office_version": "Click-to-Run Office version",
        "office_not_found": "Office not found",
        "access_denied": "access denied",
    },
    "es": {
        "window_title": "SysInfoHub",
        "app_title": "Información del sistema",
        "refresh": "Actualizar",
        "copy_report": "Copiar informe",
        "save_report": "Guardar informe",
        "save_success": "Informe guardado en {path}",
        "save_error": "Error al guardar el informe: {error}",
        "language_label": "Idioma:",
        "english": "English",
        "spanish": "Español",
        "general_section": "General",
        "operating_system_section": "Sistema operativo",
        "cpu_section": "CPU",
        "gpu_section": "GPU",
        "memory_section": "Memoria",
        "storage_section": "Almacenamiento",
        "network_section": "Red",
        "motherboard_bios_section": "Placa base / BIOS",
        "microsoft_office_section": "Microsoft Office",
        "system_time": "Hora del sistema",
        "hostname": "Nombre del equipo",
        "local_ip": "IP local",
        "mac_address": "Dirección MAC",
        "platform": "Plataforma",
        "os": "SO",
        "architecture": "Arquitectura",
        "python": "Python",
        "build": "Compilación",
        "registered_user": "Usuario registrado",
        "install_date": "Fecha de instalación",
        "physical_cores": "Núcleos físicos",
        "logical_processors": "Procesadores lógicos",
        "max_frequency": "Frecuencia máxima",
        "current_frequency": "Frecuencia actual",
        "cpu_utilization": "Uso de CPU",
        "name": "Nombre",
        "manufacturer": "Fabricante",
        "max_clock_speed": "Velocidad máxima",
        "socket": "Socket",
        "l2_cache": "Caché L2",
        "l3_cache": "Caché L3",
        "total_ram": "RAM total",
        "available_ram": "RAM disponible",
        "used_ram": "RAM usada",
        "swap_total": "Intercambio total",
        "drive": "Unidad",
        "mountpoint": "Punto de montaje",
        "file_system": "Sistema de archivos",
        "total_size": "Tamaño total",
        "used": "Usado",
        "free": "Libre",
        "driver_version": "Versión del controlador",
        "ram": "RAM",
        "video_processor": "Procesador de video",
        "status": "Estado",
        "gpu_not_available": "Información de GPU no disponible",
        "interface": "Interfaz",
        "unknown_adapter": "Adaptador desconocido",
        "ip_addresses": "Direcciones IP",
        "subnets": "Subredes",
        "gateway": "Puerta de enlace",
        "dns_servers": "Servidores DNS",
        "dhcp_enabled": "DHCP habilitado",
        "dhcp_server": "Servidor DHCP",
        "dns_host_name": "Nombre de host DNS",
        "network_not_available": "Información de red no disponible",
        "serial_number": "Número de serie",
        "bios_version": "Versión del BIOS",
        "bios_release_date": "Fecha de lanzamiento del BIOS",
        "motherboard_not_available": "Información de placa base/BIOS no disponible",
        "office_windows_only": "Los detalles de Microsoft Office están disponibles solo en Windows.",
        "office_version": "Versión de Office Click-to-Run",
        "office_not_found": "Office no encontrado",
        "access_denied": "acceso denegado",
    },
}


def t(key: str, **kwargs) -> str:
    text = TRANSLATIONS.get(LANG, TRANSLATIONS["en"]).get(key, key)
    return text.format(**kwargs)


def format_bytes(value: int) -> str:
    units = ["B", "KB", "MB", "GB", "TB"]
    for unit in units:
        if value < 1024:
            return f"{value:.2f} {unit}"
        value /= 1024
    return f"{value:.2f} PB"


def get_wmi_connection():
    if wmi is None:
        return None
    try:
        return wmi.WMI()
    except Exception:
        return None


def get_os_info() -> str:
    info = []
    system = platform.system()
    release = platform.release()
    version = platform.version()
    info.append(f"{t('os')}: {system} {release} ({version})")
    info.append(f"{t('architecture')}: {platform.machine()}")
    info.append(f"{t('python')}: {platform.python_version()} ({platform.python_implementation()})")

    if system == "Windows":
        c = get_wmi_connection()
        if c:
            try:
                os_list = c.Win32_OperatingSystem()
                if os_list:
                    os_obj = os_list[0]
                    info.append(f"{t('build')}: {os_obj.BuildNumber}")
                    info.append(f"{t('registered_user')}: {os_obj.RegisteredUser}")
                    info.append(f"{t('install_date')}: {os_obj.InstallDate}")
            except Exception:
                pass

    return "\n".join(info)


def get_cpu_info() -> str:
    info = []
    cpu_count = psutil.cpu_count(logical=False)
    cpu_count_logical = psutil.cpu_count(logical=True)
    info.append(f"{t('physical_cores')}: {cpu_count}")
    info.append(f"{t('logical_processors')}: {cpu_count_logical}")
    info.append(f"{t('max_frequency')}: {psutil.cpu_freq().max:.2f} MHz")
    info.append(f"{t('current_frequency')}: {psutil.cpu_freq().current:.2f} MHz")
    info.append(f"{t('cpu_utilization')}: {psutil.cpu_percent(interval=1)}%")

    if platform.system() == "Windows":
        c = get_wmi_connection()
        if c:
            try:
                processors = c.Win32_Processor()
                for processor in processors:
                    info.append(f"{t('name')}: {processor.Name}")
                    info.append(f"{t('manufacturer')}: {processor.Manufacturer}")
                    info.append(f"{t('max_clock_speed')}: {processor.MaxClockSpeed} MHz")
                    info.append(f"{t('socket')}: {processor.SocketDesignation}")
                    info.append(f"{t('l2_cache')}: {processor.L2CacheSize} KB")
                    info.append(f"{t('l3_cache')}: {processor.L3CacheSize} KB")
                    break
            except Exception:
                pass

    return "\n".join(info)


def get_memory_info() -> str:
    vm = psutil.virtual_memory()
    info = [
        f"{t('total_ram')}: {format_bytes(vm.total)}",
        f"{t('available_ram')}: {format_bytes(vm.available)}",
        f"{t('used_ram')}: {format_bytes(vm.used)} ({vm.percent}%)",
        f"{t('swap_total')}: {format_bytes(psutil.swap_memory().total)}",
    ]
    return "\n".join(info)


def get_disk_info() -> str:
    info = []
    partitions = psutil.disk_partitions(all=False)
    for partition in partitions:
        try:
            usage = psutil.disk_usage(partition.mountpoint)
            info.append(f"{t('drive')}: {partition.device}")
            info.append(f"  {t('mountpoint')}: {partition.mountpoint}")
            info.append(f"  {t('file_system')}: {partition.fstype}")
            info.append(f"  {t('total_size')}: {format_bytes(usage.total)}")
            info.append(f"  {t('used')}: {format_bytes(usage.used)} ({usage.percent}%)")
            info.append(f"  {t('free')}: {format_bytes(usage.free)}")
        except PermissionError:
            info.append(f"{t('drive')}: {partition.device} | {t('access_denied')}")
    return "\n".join(info)


def get_gpu_info() -> str:
    info = []
    if platform.system() == "Windows":
        c = get_wmi_connection()
        if c:
            try:
                adapters = c.Win32_VideoController()
                for adapter in adapters:
                    info.append(f"{t('name')}: {adapter.Name}")
                    info.append(f"  {t('driver_version')}: {adapter.DriverVersion}")
                    info.append(f"  {t('ram')}: {format_bytes(int(adapter.AdapterRAM or 0))}")
                    info.append(f"  {t('video_processor')}: {adapter.VideoProcessor}")
                    info.append(f"  {t('status')}: {adapter.Status}")
                    info.append("")
            except Exception:
                pass
    if not info:
        info.append(t('gpu_not_available'))
    return "\n".join(info)


def get_network_info() -> str:
    info = []
    if platform.system() == "Windows":
        c = get_wmi_connection()
        if c:
            try:
                configs = c.Win32_NetworkAdapterConfiguration(IPEnabled=True)
                for cfg in configs:
                    description = cfg.Description or t('unknown_adapter')
                    info.append(f"{t('interface')}: {description}")
                    info.append(f"  {t('mac_address')}: {cfg.MACAddress or t('unknown_adapter')}")
                    dns = cfg.DNSServerSearchOrder or []
                    ip_addresses = cfg.IPAddress or []
                    subnet = cfg.IPSubnet or []
                    gateway = cfg.DefaultIPGateway or []
                    info.append(f"  {t('ip_addresses')}: {', '.join(ip_addresses) or 'None'}")
                    info.append(f"  {t('subnets')}: {', '.join(subnet) or 'None'}")
                    info.append(f"  {t('gateway')}: {', '.join(gateway) or 'None'}")
                    info.append(f"  {t('dns_servers')}: {', '.join(dns) or 'None'}")
                    info.append(f"  {t('dhcp_enabled')}: {cfg.DHCPEnabled}")
                    info.append(f"  {t('dhcp_server')}: {cfg.DHCPServer or 'None'}")
                    info.append(f"  {t('dns_host_name')}: {cfg.DNSHostName or 'None'}")
                    info.append("")
            except Exception:
                pass
    if not info:
        for name, addrs in psutil.net_if_addrs().items():
            info.append(f"{t('interface')}: {name}")
            for addr in addrs:
                info.append(f"  {addr.family.name}: {addr.address}")
            info.append("")
    return "\n".join(info) if info else t('network_not_available')


def get_motherboard_info() -> str:
    info = []
    if platform.system() == "Windows":
        c = get_wmi_connection()
        if c:
            try:
                boards = c.Win32_BaseBoard()
                if boards:
                    board = boards[0]
                    info.append(f"{t('manufacturer')}: {board.Manufacturer}")
                    info.append(f"{t('name')}: {board.Product}")
                    info.append(f"{t('serial_number')}: {board.SerialNumber}")
                bios = c.Win32_BIOS()
                if bios:
                    info.append(f"{t('bios_version')}: {bios[0].SMBIOSBIOSVersion}")
                    info.append(f"{t('bios_release_date')}: {bios[0].ReleaseDate}")
            except Exception:
                pass
    return "\n".join(info) if info else t('motherboard_not_available')


def get_office_info() -> str:
    if platform.system() != "Windows" or winreg is None:
        return t('office_windows_only')

    results = []
    hives = [
        (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Office\ClickToRun\Configuration"),
        (winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Office\ClickToRun\Configuration"),
    ]

    for hive, path in hives:
        for view in [winreg.KEY_WOW64_64KEY, winreg.KEY_WOW64_32KEY]:
            try:
                key = winreg.OpenKey(hive, path, 0, winreg.KEY_READ | view)
                version = winreg.QueryValueEx(key, "VersionToReport")[0]
                install_path = winreg.QueryValueEx(key, "ClientFolder")[0]
                results.append(f"{t('office_version')}: {version} ({install_path})")
            except OSError:
                continue

    if not results:
        uninstall_paths = [
            (winreg.HKEY_LOCAL_MACHINE, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"),
            (winreg.HKEY_CURRENT_USER, r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall"),
        ]
        keywords = ["office", "microsoft 365", "office 16", "office 15", "office 14"]
        for hive, path in uninstall_paths:
            for view in [winreg.KEY_WOW64_64KEY, winreg.KEY_WOW64_32KEY]:
                try:
                    key = winreg.OpenKey(hive, path, 0, winreg.KEY_READ | view)
                except OSError:
                    continue
                for i in range(0, 2000):
                    try:
                        subkey_name = winreg.EnumKey(key, i)
                    except OSError:
                        break
                    try:
                        subkey = winreg.OpenKey(key, subkey_name, 0, winreg.KEY_READ | view)
                        display_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                        if any(keyword in display_name.lower() for keyword in keywords):
                            display_version = ""
                            try:
                                display_version = winreg.QueryValueEx(subkey, "DisplayVersion")[0]
                            except OSError:
                                pass
                            results.append(f"{display_name} {display_version}".strip())
                    except OSError:
                        continue
    return "\n".join(results) if results else t('office_not_found')


def get_general_info() -> str:
    info = []
    info.append(f"{t('system_time')}: {datetime.now()}")
    info.append(f"{t('hostname')}: {socket.gethostname()}")
    info.append(f"{t('local_ip')}: {socket.gethostbyname(socket.gethostname())}")
    info.append(f"{t('mac_address')}: {':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xFF) for ele in range(0, 8 * 6, 8)][::-1])}")
    info.append(f"{t('platform')}: {platform.platform()}")
    return "\n".join(info)


def build_report() -> str:
    sections = [
        (t('general_section'), get_general_info()),
        (t('operating_system_section'), get_os_info()),
        (t('cpu_section'), get_cpu_info()),
        (t('gpu_section'), get_gpu_info()),
        (t('memory_section'), get_memory_info()),
        (t('storage_section'), get_disk_info()),
        (t('network_section'), get_network_info()),
        (t('motherboard_bios_section'), get_motherboard_info()),
        (t('microsoft_office_section'), get_office_info()),
    ]

    report_lines = []
    for title, body in sections:
        report_lines.append(f"=== {title} ===")
        report_lines.append(body)
        report_lines.append("")
    return "\n".join(report_lines)


class SystemInfoApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title(t('window_title'))
        self.geometry("980x780")
        self.resizable(True, True)

        self.label = ctk.CTkLabel(self, text=t('app_title'), font=ctk.CTkFont(size=24, weight="bold"))
        self.label.pack(padx=20, pady=(18, 10))

        self.button_frame = ctk.CTkFrame(self)
        self.button_frame.pack(fill="x", padx=20, pady=(0, 10))

        self.refresh_button = ctk.CTkButton(self.button_frame, text=t('refresh'), command=self.refresh)
        self.refresh_button.pack(side="left", padx=(0, 10))

        self.copy_button = ctk.CTkButton(self.button_frame, text=t('copy_report'), command=self.copy_report)
        self.copy_button.pack(side="left", padx=(0, 10))

        self.save_button = ctk.CTkButton(self.button_frame, text=t('save_report'), command=self.save_report)
        self.save_button.pack(side="left")

        self.language_label = ctk.CTkLabel(self.button_frame, text=t('language_label'))
        self.language_label.pack(side="left", padx=(20, 4))

        self.language_menu = ctk.CTkOptionMenu(
            self.button_frame,
            values=list(LANGUAGE_OPTIONS.keys()),
            command=self.change_language,
        )
        self.language_menu.set("English" if LANG == "en" else "Español")
        self.language_menu.pack(side="left")

        self.textbox = ctk.CTkTextbox(self, width=940, height=660, wrap="word")
        self.textbox.pack(fill="both", expand=True, padx=20, pady=(0, 18))
        self.textbox.configure(state="disabled")

        self.refresh()

    def change_language(self, value: str) -> None:
        global LANG
        LANG = LANGUAGE_OPTIONS.get(value, "en")
        self.update_texts()
        self.refresh()

    def update_texts(self) -> None:
        self.title(t('window_title'))
        self.label.configure(text=t('app_title'))
        self.refresh_button.configure(text=t('refresh'))
        self.copy_button.configure(text=t('copy_report'))
        self.language_label.configure(text=t('language_label'))
        self.language_menu.set("English" if LANG == "en" else "Español")

    def refresh(self):
        report = build_report()
        self.textbox.configure(state="normal")
        self.textbox.delete("0.0", "end")
        self.textbox.insert("0.0", report)
        self.textbox.configure(state="disabled")

    def copy_report(self):
        report = self.textbox.get("0.0", "end")
        self.clipboard_clear()
        self.clipboard_append(report)
        self.update()

    def save_report(self):
        report = self.textbox.get("0.0", "end").strip()
        if not report:
            return

        filename = datetime.now().strftime("SysInfoHub_%Y%m%d_%H%M%S.txt")
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")],
            initialfile=filename,
            title=t('save_report'),
        )
        if path:
            try:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(report)
                messagebox.showinfo(t('save_report'), t('save_success', path=path))
            except Exception as exc:
                messagebox.showerror(t('save_report'), t('save_error', error=str(exc)))


if __name__ == "__main__":
    ctk.set_appearance_mode("System")
    ctk.set_default_color_theme("blue")
    app = SystemInfoApp()
    app.mainloop()
