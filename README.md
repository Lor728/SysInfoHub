# SysInfoHub

[**English**](#english) | [**Español**](#español)

---

## English

### 📋 Overview

**SysInfoHub** is a comprehensive system information viewer application for Windows. It provides detailed insights into your computer's hardware and software specifications, including CPU, GPU, memory, storage, network configuration, BIOS information, and more. The application features a user-friendly graphical interface with support for multiple languages.

### ✨ Features

- **General Information**: System time, hostname, local IP, MAC address, and platform details
- **Operating System Details**: OS version, architecture, build number, registered user, and installation date
- **CPU Information**: Physical cores, logical processors, frequencies, utilization, and detailed specifications
- **GPU Information**: Video adapter details and driver versions
- **Memory Information**: Total, available, and used RAM; swap memory details
- **Storage Information**: Disk drives with capacity, usage, and file system details
- **Network Configuration**: Network interfaces, IP addresses, DNS servers, DHCP status, and gateway information
- **BIOS/Motherboard Information**: Serial numbers, BIOS version, and release dates
- **Microsoft Office Detection**: Identifies installed Office versions (Windows only)
- **Multi-Language Support**: English and Spanish
- **Export Functionality**: Copy reports to clipboard or save as text files
- **Real-Time Refresh**: Update system information on demand

### 🛠️ Requirements

- **Python 3.7+**
- **Windows OS** (primary support; some features Windows-specific)
- **Dependencies**:
  - `customtkinter` - Modern GUI framework
  - `psutil` - System and process utilities
  - `pywin32` (optional) - Windows Registry access for Office detection
  - `wmi` (optional) - Windows Management Instrumentation

### 📦 Installation

#### Option 1: Using the Installer (Recommended)
Download the latest installer from the releases section and run `SysInfoHubInstaller.exe` to install the application.

#### Option 2: Running from Source
1. Clone or download this repository
2. Create a virtual environment:
   ```bash
   python -m venv env
   env\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install customtkinter psutil pywin32 wmi
   ```
4. Run the application:
   ```bash
   python main.py
   ```

### 🚀 Usage

Simply launch the application to view all system information. The interface provides:

- **Refresh Button**: Update all information with current system data
- **Copy Report Button**: Copy the formatted system report to your clipboard
- **Save Report Button**: Export the report to a text file in your preferred location
- **Language Selector**: Switch between English and Spanish

### 📝 License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

### 🤝 Contributing

Contributions are welcome! Feel free to submit issues or pull requests to help improve SysInfoHub.

---

## Español

### 📋 Descripción General

**SysInfoHub** es una aplicación completa de visualización de información del sistema para Windows. Proporciona información detallada sobre las especificaciones de hardware y software de su computadora, incluyendo CPU, GPU, memoria, almacenamiento, configuración de red, información de BIOS y más. La aplicación cuenta con una interfaz gráfica fácil de usar con soporte para múltiples idiomas.

### ✨ Características

- **Información General**: Hora del sistema, nombre del host, IP local, dirección MAC y detalles de la plataforma
- **Detalles del Sistema Operativo**: Versión del SO, arquitectura, número de compilación, usuario registrado y fecha de instalación
- **Información de CPU**: Núcleos físicos, procesadores lógicos, frecuencias, utilización y especificaciones detalladas
- **Información de GPU**: Detalles del adaptador de video y versiones de controladores
- **Información de Memoria**: RAM total, disponible y utilizada; detalles de memoria de intercambio
- **Información de Almacenamiento**: Unidades de disco con capacidad, uso y detalles del sistema de archivos
- **Configuración de Red**: Interfaces de red, direcciones IP, servidores DNS, estado de DHCP e información de puerta de enlace
- **Información de BIOS/Placa Base**: Números de serie, versión de BIOS y fechas de lanzamiento
- **Detección de Microsoft Office**: Identifica versiones de Office instaladas (solo en Windows)
- **Soporte Multiidioma**: Inglés y Español
- **Funcionalidad de Exportación**: Copiar reportes al portapapeles o guardar como archivos de texto
- **Actualización en Tiempo Real**: Actualizar la información del sistema bajo demanda

### 🛠️ Requisitos

- **Python 3.7+**
- **Sistema Operativo Windows** (soporte principal; algunas características específicas de Windows)
- **Dependencias**:
  - `customtkinter` - Marco moderno de interfaz gráfica
  - `psutil` - Utilidades del sistema y procesos
  - `pywin32` (opcional) - Acceso al Registro de Windows para detección de Office
  - `wmi` (opcional) - Instrumentación de Administración de Windows

### 📦 Instalación

#### Opción 1: Usando el Instalador (Recomendado)
Descargue el instalador más reciente de la sección de versiones y ejecute `SysInfoHubInstaller.exe` para instalar la aplicación.

#### Opción 2: Ejecutar desde el Código Fuente
1. Clone o descargue este repositorio
2. Cree un entorno virtual:
   ```bash
   python -m venv env
   env\Scripts\activate
   ```
3. Instale las dependencias:
   ```bash
   pip install customtkinter psutil pywin32 wmi
   ```
4. Ejecute la aplicación:
   ```bash
   python main.py
   ```

### 🚀 Uso

Simplemente inicie la aplicación para ver toda la información del sistema. La interfaz proporciona:

- **Botón Actualizar**: Actualizar toda la información con los datos actuales del sistema
- **Botón Copiar Reporte**: Copiar el reporte del sistema formateado al portapapeles
- **Botón Guardar Reporte**: Exportar el reporte a un archivo de texto en su ubicación preferida
- **Selector de Idioma**: Cambiar entre inglés y español

### 📝 Licencia

Este proyecto está licenciado bajo la Licencia MIT - consulte el archivo [LICENSE.txt](LICENSE.txt) para obtener más detalles.

### 🤝 Contribuyendo

¡Las contribuciones son bienvenidas! No dude en enviar problemas o solicitudes de extracción para ayudar a mejorar SysInfoHub.
