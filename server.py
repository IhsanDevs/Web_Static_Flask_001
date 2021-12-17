#Project Flask MVC

__author__ = "Ihsan Devs"
__version__ = "1"
__email__ = "ihsan_devs@pm.me"

from project import app

if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
