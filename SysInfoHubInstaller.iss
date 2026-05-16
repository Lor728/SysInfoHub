[Setup]
AppName=SysInfoHub
AppVersion=1.0
DefaultDirName={pf}\SysInfoHub
DefaultGroupName=SysInfoHub
OutputBaseFilename=SysInfoHubInstaller
SetupIconFile=app_icon.ico
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"
Name: "spanish"; MessagesFile: "compiler:Languages\Spanish.isl"

[Files]
Source: "dist\SysInfoHub.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "app_icon.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\SysInfoHub"; Filename: "{app}\SysInfoHub.exe"; IconFilename: "{app}\app_icon.ico"
Name: "{userdesktop}\SysInfoHub"; Filename: "{app}\SysInfoHub.exe"; IconFilename: "{app}\app_icon.ico"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a desktop icon"; GroupDescription: "Additional icons:"; Flags: unchecked

[Code]
// Nothing extra needed here for this simple installer.
