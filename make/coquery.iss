; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

[Setup]
; NOTE: The value of AppId uniquely identifies this application.
; Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{42204621-F37F-40C3-96E2-886FFF94D497}
AppName=Coquery
AppVersion=0.9
;AppVerName=Coquery 0.9
AppPublisherURL=http://www.coquery.org
AppSupportURL=http://www.coquery.org
AppUpdatesURL=http://www.coquery.org
DefaultDirName={pf}\Coquery
DisableProgramGroupPage=yes
LicenseFile=C:\Users\dadasd\coquery\make\gpl-3.0.txt
OutputBaseFilename=setup
SetupIconFile=C:\Users\dadasd\coquery\coquery\icons\artwork\logo.ico
Compression=lzma
SolidCompression=yes

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\dadasd\coquery\make\dist\coquery\coquery.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\dadasd\coquery\make\dist\coquery\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{commonprograms}\Coquery"; Filename: "{app}\coquery.exe"
Name: "{commondesktop}\Coquery"; Filename: "{app}\coquery.exe"; Tasks: desktopicon

[Run]
Filename: "{app}\coquery.exe"; Description: "{cm:LaunchProgram,Coquery}"; Flags: nowait postinstall skipifsilent

