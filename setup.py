from cx_Freeze import setup, Executable


setup(
    name="Pynarp",
    version="0.1",
    description="A simple installer to configure Python, PostgreSQL, Nginx and Nginx Unit on Debian-based systems.",
    executables=[Executable("pynarp.py")],
)
