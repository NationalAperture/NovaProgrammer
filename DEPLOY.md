# Deployment Guide

This document explains how to build the Nova MC-6 Programmer with PyInstaller and share the resulting executables through GitHub Releases or a custom download domain.

## 1. Prepare the Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
PyInstaller uses your current Python environment to capture dependencies, so ensure the version matches your target platform (e.g., build on Windows for Windows executables).

## 2. Build with PyInstaller
The repository already includes `mainwindow.spec`, which defines the entry point, resources, and bundling options. To generate fresh artifacts:
```bash
python -m PyInstaller mainwindow.spec
```
Key outputs:
- `dist/mainwindow/` — folder containing the standalone `mainwindow` executable plus `values.json` and shared libraries.
- `build/mainwindow/` — PyInstaller work directory; safe to delete after a successful build.

### Updating the Spec File
If you add new data files or modules:
1. Edit `mainwindow.spec` to include them in the `datas` or `hiddenimports` lists.
2. Re-run PyInstaller with the command above.

## 3. Testing the Bundle
Before distributing:
```bash
./dist/mainwindow/mainwindow
```
On Windows this is typically `dist\mainwindow\mainwindow.exe`. Confirm the app launches, loads `styles.qss`, and communicates with a test controller or loopback port.

## 4. Publishing via GitHub Releases
1. Create a versioned release branch / tag (`git tag v1.0.0`).
2. Build on the target OS.
3. Zip the executable folder:
   ```bash
   cd dist
   zip -r nova-mc6-programmer-windows.zip mainwindow
   ```
4. Open **GitHub → Releases → Draft a new release**, attach the ZIP (or `.exe` if you prefer a single file build via `--onefile`), and include release notes.
5. Publish; GitHub will host the asset at a predictable URL you can share with users.

## 5. Hosting on a Custom Domain
If you need a branded download link:
1. Upload the ZIP/EXE to your hosting provider (S3, Azure Blob, static web host).
2. Configure your DNS (e.g., `download.example.com`) to point to the hosting endpoint.
3. Provide the HTTPS link to users.
4. (Optional) Mirror the same asset on GitHub Releases to take advantage of GitHub’s CDN and version history.

## 6. Keeping Users Updated
- Document changes in `CHANGELOG.md` (create if absent) and include upgrade notes in each release.
- Use versioned filenames (`nova-mc6-programmer-v1.0.0.zip`) so users can see when an update is available.
- Consider adding an update notification in the app that checks for new release tags via the GitHub API or your custom endpoint.
