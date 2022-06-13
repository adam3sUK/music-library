from ui.interface import Interface, ConsoleIO
import subprocess
import eyed3

interface = Interface(ConsoleIO(), subprocess, eyed3)
interface.run()
